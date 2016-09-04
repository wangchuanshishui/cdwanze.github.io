<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 简介</a></li>
<li><a href="#orgheadline6">2. task</a>
<ul>
<li><a href="#orgheadline2">2.1. run方法</a></li>
<li><a href="#orgheadline3">2.2. get_params方法</a></li>
<li><a href="#orgheadline4">2.3. output方法</a></li>
<li><a href="#orgheadline5">2.4. requires方法</a></li>
</ul>
</li>
<li><a href="#orgheadline8">3. parameter</a>
<ul>
<li><a href="#orgheadline7">3.1. 参数对象的值</a></li>
</ul>
</li>
<li><a href="#orgheadline9">4. target</a></li>
<li><a href="#orgheadline10">5. 配置文件</a></li>
</ul>
</div>
</nav>


# 简介<a id="orgheadline1"></a>

虽然luigi从源码上很简单，但我觉得最好将其称之为框架。模块和框架的区别在于当你引入一个框架时，整个软件的思路架构都会发生某种变动，而模块并没有那么大的影响，更像是一个额外的函数或者类，方便你的使用。总的来说我是不喜欢框架这种束缚人的东西的，但是顶层流程控制不同，它必然内在地对整个系统的架构发生某种深刻的影响，luigi正是这样一个项目，方便你进行你的软件或系统的顶层流程控制，所以最好称之为框架。

luigi框架的github项目地址在 [这里](https://github.com/spotify/luigi) ，其可以用pip简单安装之。官方文档也不能说没有或语焉不详，但对于顶层流程控制这个内在极丰富的领域来说，确实文档显得单薄了些。好在luigi框架源码结构清晰，也很简单。不过就算把luigi源码分析得差不多了，至于顶层流程控制这个领域来说，也只能说才刚刚开始。

# task<a id="orgheadline6"></a>

luigi源码 `__init__.py` 文件一开始就是

    from luigi import task

也确实该框架最核心的一个概念就是这个Task类。下面演示一个最基本的例子，通过这个基本的例子我们能够学到很多东西。

```python
import luigi

class Test(luigi.Task):
    count = luigi.IntParameter()
    x = luigi.Parameter(default="hello luigi")

    def run(self):
        print self.count
        print self.x
        print self.get_params()

if __name__ == '__main__':
    luigi.run()
```

首先我们看到luigi.IntParameter那里，这些变量在Task对象中都可以使用如self.count这样的语法引用，然而更重要的是这些变量都自动进入命令行封装了。

读者可以先简单看下这个命令行目前支持的选项，Test类一般为本脚本任务流的最终任务出口:

    python test1.py Test --help

其中count参量还需要输入值脚本才能正常运行:

    python test1.py Test --local-scheduler --count=10

然后脚本要正常运行你还需要加上 `--local-scheduler` ，这个所谓的scheduler可以简单的理解为luigi的任务调度器，这里设置为了本地的调度器。luigi还支持远程调度器，这样多台机器上可以使用同一的远程的任务调度器，这些机器会协同来完成任务工作流。

## run方法<a id="orgheadline2"></a>

run方法是Task对象很重要的一个方法，表明执行该任务其应该做些什么事情。

## get\_params方法<a id="orgheadline3"></a>

Task对象的 `get_params` 方法（其是一个类方法）会返回本任务对象收集的参数。这在有时需要传递全局型参数时很有用。

## output方法<a id="orgheadline4"></a>

下面看第二个例子:

```python
from __future__ import print_function

import luigi

class Test(luigi.Task):
    count = luigi.IntParameter()
    x = luigi.Parameter(default="hello luigi")


    def output(self):
        return luigi.LocalTarget("test2out.txt")

    def run(self):
        with self.output().open("w") as f:
            print(self.count,file=f)
            print(self.x,file=f)
            print(self.get_params(),file=f)

if __name__ == '__main__':
    luigi.run()
#python test2.py Test --local-scheduler --count=10
```

这个例子演示了output方法的作用，Test任务对象主体run方法作用和之前一样，这里打开了一个文件，而这个文件对象的获取是借助于output的返回的。这里output方法返回的一定是所谓的Target对象，其一定有一个exists方法，通常对应的是某个文件，如果存在则返回True，如果不存在则返回False（这个存在与否的信息方便luigi进行流程控制）。然后具体到LocalTarget对象，其就对应的是本地的某个文件对象。其有一个open方法，目前只有两种模式"r"或"w"。然后后面就和操作常规python文件对象一样了。

这个小程序简单将之前的那些信息写入到那个文件中去了。

## requires方法<a id="orgheadline5"></a>

到requires方法这里

# parameter<a id="orgheadline8"></a>

## 参数对象的值<a id="orgheadline7"></a>

参数对象进来之后还是什么luigi专门的Parameter对象，并不能在python中正常使用，需要类似 `p.value` 这样把值提出来之后才能变成常规的python值。

# target<a id="orgheadline9"></a>

# 配置文件<a id="orgheadline10"></a>

<http://blog.kissdata.com/2014/05/28/lugi.html#luigi>