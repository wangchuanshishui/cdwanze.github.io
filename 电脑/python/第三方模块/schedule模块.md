<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline8">1. 分析源码</a>
<ul>
<li><a href="#orgheadline1">1.1. every函数</a></li>
<li><a href="#orgheadline2">1.2. Job对象的do方法</a></li>
<li><a href="#orgheadline3">1.3. Job对象的at方法</a></li>
<li><a href="#orgheadline4">1.4. Scheduler对象的run_pending方法</a></li>
<li><a href="#orgheadline5">1.5. should_run属性</a></li>
<li><a href="#orgheadline6">1.6. Job对象的run方法</a></li>
<li><a href="#orgheadline7">1.7. Job取消机制</a></li>
</ul>
</li>
</ul>
</div>
</nav>

schedule模块是一个很简单但很有用的模块，实际上其源代码是如此之简单，我下面会把核心部分全部贴出来然后分析之。其github地址在 [这里](https://github.com/dbader/schedule) 。

我们可以在远程计算机那边开一个screen后台，然后运行这么一个你希望系统周期性运行的任务。实际上linux可以安装所谓的cron后台服务，不过其不可测试不可扩展，对于python爱好者来说，还是推荐用 schedule 模块来管理系统后台周期性任务。

就一般安装就简单用 pip安装之，就一般使用如下所示:

```python
import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

然后我们看到其就一个 `every` 函数，后面是seconds, minutes, hour, day, monday, tuesday, wednesday, thursday, friday, saturday, sunday, weeks等等。

然后 `at` 还可以设置具体的时间点。schedule对象这样设置之后叫做注册，实际执行需要调用schedule对象的 `run_pending` 方法，具体你需要如上面例子一样设置一个循环和一个time.sleep计时机制。需要注意的是如果你这个sleep设置为睡眠1个小时，那么哪怕你的schdule对象有一个每一秒钟执行一次的动作，其也将只执行一次。可以把这个外部内省计时时间调得稍微小点，那么才有会我们预期的效果。

此外还有 `run_all` 方法，立即执行所有动作， `clear` 删除所有动作， `cancel_job` ，具体删除某一个动作。 

下面分析这个模块的源码。

# 分析源码<a id="orgheadline8"></a>

模块就一个文件，在该模块文件中，创建了一个默认的Scheduler对象。

    default_scheduler = Scheduler()
    jobs = default_scheduler.jobs  # todo: should this be a copy, e.g. jobs()?

    class Scheduler(object):
        def __init__(self):
            self.jobs = []

## every函数<a id="orgheadline1"></a>

    def every(interval=1):
        """Schedule a new periodic job."""
        return default_scheduler.every(interval)

其实际上就是执行的默认scheduler的every方法。

```python
def every(self, interval=1):
    """Schedule a new periodic job."""
    job = Job(interval)
    self.jobs.append(job)
    return job
```

其就是新建的一个Job对象，然后将其添加到self.jobs这个列表中。其将返回一个Job对象，然后填入的interval参数默认是1。

```python
class Job(object):
    """A periodic job as used by `Scheduler`."""
    def __init__(self, interval):
        self.interval = interval  # pause interval * unit between runs
        self.job_func = None  # the job job_func to run
        self.unit = None  # time units, e.g. 'minutes', 'hours', ...
        self.at_time = None  # optional time at which this job runs
        self.last_run = None  # datetime of the last run
        self.next_run = None  # datetime of the next run
        self.period = None  # timedelta between runs, only valid for
        self.start_day = None  # Specific day of the week to start on
```

Job对象有很多属性:

```python
@property
def second(self):
    assert self.interval == 1, 'Use seconds instead of second'
    return self.seconds

@property
def seconds(self):
    self.unit = 'seconds'
    return self

@property
def minute(self):
    assert self.interval == 1, 'Use minutes instead of minute'
    return self.minutes

@property
def minutes(self):
    self.unit = 'minutes'
    return self

@property
def hour(self):
    assert self.interval == 1, 'Use hours instead of hours'
    return self.hours

@property
def hours(self):
    self.unit = 'hours'
    return self

@property
def day(self):
    assert self.interval == 1, 'Use days instead of day'
    return self.days

@property
def days(self):
    self.unit = 'days'
    return self

@property
def week(self):
    assert self.interval == 1, 'Use weeks instead of week'
    return self.weeks

@property
def weeks(self):
    self.unit = 'weeks'
    return self
```

注意 `second` 是返回self.seconds ，而 `seconds` 是返回的 self，也就是原Job对象。后面的都类似，关键词有:

-   second
-   minute
-   hour
-   day
-   week

比如说:

    schedule.every(10).minutes.do(job)

其将直接执行 Job.minutes，设置单位为 `minutes` ，然后在返回该Job对象。

而:

    schedule.every().hour.do(job)

其将执行 Job.hour ，其首先要确认interval是1，然后再返回Job.hours，然后设置单位为 `hours` ，然后再返回该Job对象。其他的都类似。

## Job对象的do方法<a id="orgheadline2"></a>

    def do(self, job_func, *args, **kwargs):
        """Specifies the job_func that should be called every time the
        job runs.
    
        Any additional arguments are passed on to job_func when
        the job runs.
        """
        self.job_func = functools.partial(job_func, *args, **kwargs)
        try:
            functools.update_wrapper(self.job_func, job_func)
        except AttributeError:
            # job_funcs already wrapped by functools.partial won't have
            # __name__, __module__ or __doc__ and the update_wrapper()
            # call will fail.
            pass
        self._schedule_next_run()
        return self

这里对该函数对象进行了额外的封装，加上了额外的参数。然后通过 `update_wrapper` 让这个函数获得原函数的 `__doc__` 之类属性从而更像一个正常的函数。然后执行 `_schedule_next_run` 方法。

    def _schedule_next_run(self):
        """Compute the instant when this job should run next."""
        # Allow *, ** magic temporarily:
        # pylint: disable=W0142
        assert self.unit in ('seconds', 'minutes', 'hours', 'days', 'weeks')
        self.period = datetime.timedelta(**{self.unit: self.interval})
        self.next_run = datetime.datetime.now() + self.period
        if self.start_day is not None:
            assert self.unit == 'weeks'
            weekdays = (
                'monday',
                'tuesday',
                'wednesday',
                'thursday',
                'friday',
                'saturday',
                'sunday'
            )
            assert self.start_day in weekdays
            weekday = weekdays.index(self.start_day)
            days_ahead = weekday - self.next_run.weekday()
            if days_ahead <= 0:  # Target day already happened this week
                days_ahead += 7
            self.next_run += datetime.timedelta(days_ahead) - self.period
        if self.at_time is not None:
            assert self.unit in ('days', 'hours') or self.start_day is not None
            kwargs = {
                'minute': self.at_time.minute,
                'second': self.at_time.second,
                'microsecond': 0
            }
            if self.unit == 'days' or self.start_day is not None:
                kwargs['hour'] = self.at_time.hour
            self.next_run = self.next_run.replace(**kwargs)
            # If we are running for the first time, make sure we run
            # at the specified time *today* (or *this hour*) as well
            if not self.last_run:
                now = datetime.datetime.now()
                if (self.unit == 'days' and self.at_time > now.time() and
                        self.interval == 1):
                    self.next_run = self.next_run - datetime.timedelta(days=1)
                elif self.unit == 'hours' and self.at_time.minute > now.minute:
                    self.next_run = self.next_run - datetime.timedelta(hours=1)
        if self.start_day is not None and self.at_time is not None:
            # Let's see if we will still make that time we specified today
            if (self.next_run - datetime.datetime.now()).days >= 7:
                self.next_run -= self.period

这个函数主要对该Job对象进行了一些时间上的业务逻辑处理，有空可以细看一下。

## Job对象的at方法<a id="orgheadline3"></a>

一个便捷的方法更好地设置时间。

    def at(self, time_str):
        """Schedule the job every day at a specific time.
    
        Calling this is only valid for jobs scheduled to run every
        N day(s).
        """
        assert self.unit in ('days', 'hours') or self.start_day
        hour, minute = time_str.split(':')
        minute = int(minute)
        if self.unit == 'days' or self.start_day:
            hour = int(hour)
            assert 0 <= hour <= 23
        elif self.unit == 'hours':
            hour = 0
        assert 0 <= minute <= 59
        self.at_time = datetime.time(hour, minute)
        return self

## Scheduler对象的run\_pending方法<a id="orgheadline4"></a>

用于判断的就是Job对象的 `should_run` 属性，其为真则将被执行，具体是执行Job对象的 `run` 方法。

    def run_pending(self):
        """Run all jobs that are scheduled to run.
    
        Please note that it is *intended behavior that tick() does not
        run missed jobs*. For example, if you've registered a job that
        should run every minute and you only call tick() in one hour
        increments then your job won't be run 60 times in between but
        only once.
        """
        runnable_jobs = (job for job in self.jobs if job.should_run)
        for job in sorted(runnable_jobs):
            self._run_job(job)

## should\_run属性<a id="orgheadline5"></a>

现在时间大于等于预定时间则执行任务。

    @property
    def should_run(self):
        """True if the job should be run now."""
        return datetime.datetime.now() >= self.next_run

Job对象的 `next_run` 是前面的 `_schedule_next_run` 方法计算得出的。

## Job对象的run方法<a id="orgheadline6"></a>

上一次执行时间设为现在。

    def run(self):
        """Run the job and immediately reschedule it."""
        logger.info('Running job %s', self)
        ret = self.job_func()
        self.last_run = datetime.datetime.now()
        self._schedule_next_run()
        return ret

## Job取消机制<a id="orgheadline7"></a>

    def _run_job(self, job):
        ret = job.run()
        if isinstance(ret, CancelJob) or ret is CancelJob:
            self.cancel_job(job)

        def cancel_job(self, job):
            """Delete a scheduled job."""
            try:
                self.jobs.remove(job)
            except ValueError:
                pass
    class CancelJob(object):
        pass

从这里我们看到函数若向执行一次之后则该Job取消，则需要返回 `return CancelJob()` 。

可能需要更好的取消Job机制，和执行多少次然后退出的机制。

很简单的一个模块，还可以写的功能更强大一些。