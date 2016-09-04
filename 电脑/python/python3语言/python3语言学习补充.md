<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. all和any关键词</a></li>
<li><a href="#orgheadline2">2. 快速更新类的本地变量</a></li>
<li><a href="#orgheadline3">3. 可迭代对象flatten</a></li>
<li><a href="#orgheadline4">4. __slots__ 方法</a></li>
<li><a href="#orgheadline5">5. 三元运算符</a></li>
<li><a href="#orgheadline6">6. __missing__ 方法</a></li>
<li><a href="#orgheadline9">7. 字符串比较大小</a>
<ul>
<li><a href="#orgheadline7">7.1. 中文比较大小？</a></li>
<li><a href="#orgheadline8">7.2. ord和chr函数</a></li>
</ul>
</li>
<li><a href="#orgheadline11">8. exec和eval</a>
<ul>
<li><a href="#orgheadline10">8.1. 如果执行import语句</a></li>
</ul>
</li>
<li><a href="#orgheadline12">9. assert语句</a></li>
<li><a href="#orgheadline13">10. 属性管理的函数</a></li>
<li><a href="#orgheadline14">11. __name__和__file__</a></li>
<li><a href="#orgheadline15">12. locals和globals</a></li>
<li><a href="#orgheadline16">13. product函数</a></li>
<li><a href="#orgheadline17">14. @property装饰器</a></li>
<li><a href="#orgheadline18">15. 缓存属性</a></li>
<li><a href="#orgheadline21">16. datetime object转变成为time_struct object</a>
<ul>
<li><a href="#orgheadline19">16.1. time_struct object to datetime object</a></li>
<li><a href="#orgheadline20">16.2. datetime object to time_struct object</a></li>
</ul>
</li>
<li><a href="#orgheadline22">17. __import__函数</a></li>
<li><a href="#orgheadline23">18. 上下文环境确认with语句</a></li>
<li><a href="#orgheadline26">19. 函数装饰器</a>
<ul>
<li><a href="#orgheadline24">19.1. 没有参数的函数装饰器</a></li>
<li><a href="#orgheadline25">19.2. 有参数的函数装饰器</a></li>
</ul>
</li>
<li><a href="#orgheadline29">20. 类装饰器</a>
<ul>
<li><a href="#orgheadline27">20.1. 无参数装饰器</a></li>
<li><a href="#orgheadline28">20.2. 有参数的装饰器</a></li>
</ul>
</li>
<li><a href="#orgheadline30">21. and or not的运算优先级</a></li>
<li><a href="#orgheadline33">22. 多进程</a>
<ul>
<li><a href="#orgheadline31">22.1. 进程fork</a></li>
<li><a href="#orgheadline32">22.2. 子进程和父进程分开</a></li>
</ul>
</li>
<li><a href="#orgheadline37">23. 多线程</a>
<ul>
<li><a href="#orgheadline34">23.1. 后台警报线程</a></li>
<li><a href="#orgheadline35">23.2. 多线程: 一个定时器</a></li>
<li><a href="#orgheadline36">23.3. 多线程下载大文件</a></li>
</ul>
</li>
</ul>
</div>
</nav>


# all和any关键词<a id="orgheadline1"></a>

这是python语言里面的关键词函数，源码很简单，下面列出来，看一下就清楚了:

```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
```

如果用语言表述的话是:

-   all，都是True，则返回True，否则返回False
-   any，只要有一个True则返回True，否则返回False。

# 快速更新类的本地变量<a id="orgheadline2"></a>

ref : <https://github.com/yasoob/intermediatePython/blob/master/one_liners.rst>

    class A(object):
        def __init__(self, a, b, c, d, e, f):
            self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})

# 可迭代对象flatten<a id="orgheadline3"></a>

    a_list = [[1, 2], [3, 4], [5, 6]]
    print(list(itertools.chain.from_iterable(a_list)))
    # Output: [1, 2, 3, 4, 5, 6]
    
    # or
    print(list(itertools.chain(*a_list)))
    # Output: [1, 2, 3, 4, 5, 6]

# \_\_slots\_\_ 方法<a id="orgheadline4"></a>

请参看 [这个网页](https://github.com/yasoob/intermediatePython/blob/master/__slots__magic.rst) 。

我多少对这个不太感兴趣，因为我观察python程序大部分情况下，RAM用的并不多，有的时候我们甚至要考虑强制使用RAM来提高程序的运算速度。但了解一下吧。

# 三元运算符<a id="orgheadline5"></a>

也就是类似这样的结构:

    loop = loop if loop is not None else get_event_loop()

通常我们在处理函数的入口参数实现默认值的情况的时候会用到，比如上面一般函数参数那里写着 `loop=None` ，用上面这种一行形式更简洁一些。而我们不直接在函数定义的那里采用默认值可能有两种情况，一是该默认值并不方便作为默认值，而最好默认为None
；还有一种情况是默认值是需要通过某个函数等运算得到的。

# \_\_missing\_\_ 方法<a id="orgheadline6"></a>

对于字典或者字典的子类，你可以通过定义 `__missing__` 方法来回避找不到键值而抛出的 `KeyError` ，参考了 [这个网页](http://stackoverflow.com/questions/635483/what-is-the-best-way-to-implement-nested-dictionaries-in-python) 。如下所示:

```python
class NestedDict(collections.UserDict):
    '''
Implement this data structure:
{"section":{},
}

learning from http://stackoverflow.com/questions/635483/what-is-the-best-way-to-implement-nested-dictionaries-in-python

'''
    def __init__(data=None):
        super().__init__(data)

    def __missing__(self, key):
        value = self[key] = dict()
        return value

    def update_in_section(self, section, d):
        self[section].update(d)

    def get_in_section(self, section,key):
        return self[section].get(key)

    def delete_in_section(self,section,key):
        del self[section][key]

    def set_in_section(self,section,key,value):
        self[section][key] = value
```

如果找不到该key，则该类会自动赋值一个新的 dict()并作为该key的值。你可能希望使用 `type(self)()` ，但这种风格对json的兼容性不太好，推荐还是都用dict类。

# 字符串比较大小<a id="orgheadline9"></a>

读者可以实验一下python中字符串之间是可以比较大小的：

    >>> 'abc' > 'ab'
    True
    >>> 'fabc' > 'abc'
    True
    >>> '3.04' > '3'
    True

这个特性有的时候很有用的，具体是如何比较大小的呢？按照python官方文档的描述，采用的是词典编纂顺序。具体描述信息如下：

> 序列之间比较大小是，首先两个序列各自的第一个元素开始比较，如果它们相同，则进行下一个比较，直到任何一个序列被穷尽。如果两个序列各自比较的类型都是相同的，那么整个过程将一直进行下去。如果两个序列是相等的则认为它们是相等的，如果某一个序列是另外一个序列的子序列，则那个短的序列认为比长的序列要小。具体到每一个元素的大小比较，是按照ASCII顺序对其进行比较的。

## 中文比较大小？<a id="orgheadline7"></a>

读者这时会想到，既然python中字符串都默认是unicode编码（utf-8），那么中文应该也是能够比较大小的吧，事实确实如此：

    >>> '章' > '张'
    True
    >>> '章' < '张'
    False
    >>> ord('章')
    31456
    >>> ord('张')
    24352

感兴趣的读者可以打开字符映射表看一下，'张'对应的unicode编号是U+5F20，你输入0x5f20，返回的正是24352。如果你输入hex(24352)，返回的就是'0x5f20'。

## ord和chr函数<a id="orgheadline8"></a>

ord函数接受 *一个* 字符，然后返回其unicode编码，十进制的。chr函数是ord函数的反向，比如你输入24352这个十进制uniocde，就返回了对应的字符。

    >>> chr(24352)
    '张'

所以我们可以总结到，python3的字符串比较大小，是基于utf-8编码的。

# exec和eval<a id="orgheadline11"></a>

exec和eval都可以用来执行python代码的字符串形式，exec没有返回值，eval有返回值。不过这两个函数使用都要慎重，按照diveintopython3  [第8章第九节](http://www.diveintopython3.net/advanced-iterators.html) 的讲解，这些代码如果混入网络服务器中确实会很危险，如果一定要用，必须对输入字符串进行严格正则限定。

不过话虽然这样说，但这两个函数的使用有时能够给程序的架构带来意想不到的好处。

```python
def get_info(self):
    if self.netloc in netloc_id:
        target = netloc_id.get(self.netloc)
        print('在调用模块', target)
        exec('from youget.{0} import youget'.format(target), globals())
        self.info = youget(self.url)
    else:
        print('还不支持站点',self.netloc)

    return self.info
```

在比如说我写过一个根据小型python代码生成svg文件的小模块，具体绘图的python代码类似下面的样子：

```python
from pysvg.basicshapes import *
from pysvg.core import *

svg = Svg(width=XMAX * 2,height=YMAX * 2)
p0 = Point(0,0)
circle = Circle(p=p0, r=Quantity(2))
circle.set('fill',"red")
svg.add(circle)

p1 = Point(0,0)
p2 = Point(2,2)
line = Line(p1,p2)
svg.add(line)

rect = Rect(Point(-2,2),Point(2,-2))
svg.add(rect)

g1 = Group('g1',circle,rect)
g1.set('transform','translate(100)')
svg.add(g1)

print(svg)
```

这里不讨论那些类的具体细节，实际上很简单，就是编好 `__str__` 字符串输出控制函数。这里我们看到最后的那个print函数。然后字符串的输出流是用下面这个核心代码控制的参考了 [这个网页](http://stackoverflow.com/questions/701802/how-do-i-execute-a-string-containing-python-code-in-python)

## 如果执行import语句<a id="orgheadline10"></a>

参考了 [这个网页](http://stackoverflow.com/questions/12505047/in-python-why-doesnt-an-import-in-an-exec-in-a-function-work) ，如果在exec语句里面使用import语句，具体引入的变量名希望被外围程序使用，则需要如下所示。这里globals()返回当前全局变量值字典。

    exec('from youget.{0} import youget'.format(target), globals())

# assert语句<a id="orgheadline12"></a>

assert语句简单的理解就是 `assert True` ，正常刷过去，而 `assert False` 将抛出 `AssertionError` 。

# 属性管理的函数<a id="orgheadline13"></a>

hasattr，setattr，getattr，delattr，这些函数都属于关于python中各个对象的属性管理函数，其都是内置函数。

其中hasattr(object, name)检测某个对象有没有某个属性。

setattr(object, name, value)用于设置某个对象的某个属性为某个值， `setattr(x,a,3)` 对应 `x.a = 3` 这样的语法。

getattr(object, name[, default])用于取某个对象的某个属性的值，对应 `object.name` 这样的语法。

delattr(object,name)用于删除某个对象的某个属性，对应 `del object.name` 这样的语法。

# \_\_name\_\_和\_\_file\_\_<a id="orgheadline14"></a>

这里所谓脚本被引入是指用import或者from语句被另外一个脚本引入进去，而这里所谓的脚本被执行是指直接如 `python test.py` 这样的形式执行该py脚本。

这两种形式很有一些区别，下面慢慢谈论:

1.  `__name__` 的区别。这个大家应该很熟悉了。如果脚本是被引入的， `__name__` 的值是该引入的脚本文件名，比如引入的是 `test.py` ，那么该脚本被引入，对于这个test.py文件来说，其内的 `__name__` 的值就是 `test` ，也就是 **模块名** 。；而如果是作为脚本被执行，则该 `__name__` 是 `__main__` 。

2.  `__file__` 的区别。如果脚本是被执行的，假设该脚本文件是 `hello.py` ，那么在这个被执行脚本中， `__file__` 的值是 `hello.py` ，也就是 **文件名** 。如果是被引用的，那么对于那个被引入的脚本来说， `__file__` 的值是该被引入脚本相对系统来说的 **完整文件名** ，比如是 `/home/wanze/桌面/hello.py` 。

3.  如果我们要得知本脚本在系统中的绝对位置，可以使用os.path模块的abspath函数。

```python
import os
path = os.path.abspath('')
```

其将返回该脚本在系统所在的目录。

# locals和globals<a id="orgheadline15"></a>

python的 `locals()` 返回本函数内的局部变量字典值，而 `globals()` 则返回本模块文件的全局变量。 `locals` 是只读的，而 `globals()` 不是，我们可以利用 `globals()` 对脚本文件玩出一些新花样。

# product函数<a id="orgheadline16"></a>

product函数在 `itertools` 模块里面，按照官方文档的说明是product(A, B)返回值等价于((x,y) for x in A for y in B)，也就是各种可能的组合情况（类似于笛卡尔积的概念）:

    >>> list(product(['a','b'],['c']))
    [('a', 'c'), ('b', 'c')]

此外单一迭代加上 **repeat** 参数也会生成一些很有意思的结果:

    >>> list(product(['True','False'],repeat=len('abc')))
    [('True', 'True', 'True'), ('True', 'True', 'False'), ('True', 'False', 'True'), ('True', 'False', 'False'), ('False', 'True', 'True'), ('False', 'True', 'False'), ('False', 'False', 'True'), ('False', 'False', 'False')]

这可以看作:

    >>> list(product(['True','False'],['True','False'],['True','False']))
    [('True', 'True', 'True'), ('True', 'True', 'False'), ('True', 'False', 'True'), ('True', 'False', 'False'), ('False', 'True', 'True'), ('False', 'True', 'False'), ('False', 'False', 'True'), ('False', 'False', 'False')]

也就是这样2\*2\*2的笛卡尔积的组合形式。

# @property装饰器<a id="orgheadline17"></a>

简单的理解就是如下所示:

```python
class Apple():
    def __init__(self):
        self._color = 'red'

    @property
    def color(self):
        return self._color

apple = Apple()
```

这样将给这个类定义个属性，具体调用这个属性就用这样的点号引用即可，然后实际执行的就是 `@property` 装饰的那个函数。 现在这个color属性只可读，不可更改。

    >>> apple.color
    'red'
    >>> apple.color = 'yellow'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: can't set attribute

请参看 [这个网页](http://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work) ，这里讲到了 `@color.setter` 装饰器，来装饰某个函数之后，通过这个函数来修改color属性。然后还有 `@color.deleter` 装饰某个函数之后，来通过这个函数来删除某个属性。这里deleter的使用可能较少，一般 `@property` 就能满足大部分需求了，有的觉得需要修改某个属性则定义setter。

# 缓存属性<a id="orgheadline18"></a>

如果读者研究额上面的 property 装饰器，那么我们可以继承这个property class来写出一个具有缓存特性的属性:

```python
import logging

class memorized_property(property):
    def __init__(self,*args,**kwargs):
        super(memorized_property,self).__init__(*args,**kwargs)
        self.name = '_{}'.format(self.fget.__name__)

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")


        if self.name in obj.__dict__:
            logging.debug('from memory------------------------------')
            return obj.__dict__[self.name]
        else:
            logging.debug('from computing##########################')
            value = obj.__dict__[self.name] = self.fget(obj)
            return value

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        obj.__dict__[self.name] = value

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        del obj.__dict__[self.name]

import time

class Test(object):
    def __init__(self):
        pass

    @memorized_property
    def x(self):
        return time.time()

    @x.setter
    def x(self,value):
        pass
    @x.deleter
    def x(self):
        pass

if __name__ == '__main__':
    logging.basicConfig(level = logging.DEBUG)
    t =  Test()
```

# datetime object转变成为time\_struct object<a id="orgheadline21"></a>

## time\_struct object to datetime object<a id="orgheadline19"></a>

[参考这个网页](http://stackoverflow.com/questions/1697815/how-do-you-convert-a-python-time-struct-time-object-into-a-datetime-object) 

    from time import mktime
    from datetime import datetime
    
    dt = datetime.fromtimestamp(mktime(struct))

## datetime object to time\_struct object<a id="orgheadline20"></a>

<http://stackoverflow.com/questions/8022161/python-converting-from-datetime-datetime-to-time-time>

    >>> t = datetime.datetime.now()
    >>> t
    datetime.datetime(2011, 11, 5, 11, 26, 15, 37496)
    
    >>> time.mktime(t.timetuple()) + t.microsecond / 1E6
    1320517575.037496

# \_\_import\_\_函数<a id="orgheadline22"></a>

<http://stackoverflow.com/questions/2349991/python-how-to-import-other-python-files>

# 上下文环境确认with语句<a id="orgheadline23"></a>

参看了 [这个网页](https://github.com/yasoob/intermediatePython/blob/master/context_managers.rst) 。

\_\_enter\_\_   <span class="underline"><span class="underline">exit</span></span> 类方法

# 函数装饰器<a id="orgheadline26"></a>

## 没有参数的函数装饰器<a id="orgheadline24"></a>

    def mydecorator(function):
        def _mydecorator(*args,**kargs):
            # do some stuff
            res = function(*args,**kargs)##实际执行被装饰的函数
            # do some other stuff
            return res
        return _mydecorator

## 有参数的函数装饰器<a id="orgheadline25"></a>

有参数的函数装饰器用到的情况更少了，稍微了解下即可，需要使用二级封装。arg1进入装饰器函数是以类似lisp中自由变量的形式存在的。

    def mydecorator(arg1, arg2):
        def _mydecorator(function):
            def __mydecorator(*args,**kargs):
                res = function(*args,**kargs)
                return res
            return __mydecorator
        return _mydecorator

# 类装饰器<a id="orgheadline29"></a>

装饰器在python中扮演着非常重要的地位，下面简要介绍之。

## 无参数装饰器<a id="orgheadline27"></a>

如果你的装饰器不需要参数，那么就简单用一个函数装饰器即可。

```python
def mydecorator(function):
    def _mydecorator(*args,**kargs):
        # do some stuff
        res = function(*args,**kargs)##实际执行被装饰的函数
        # do some other stuff
        return res
    return _mydecorator
```

## 有参数的装饰器<a id="orgheadline28"></a>

或者 有状态的装饰器 一律采用 内置类对象的风格，这样更加清晰。

最核心的部分如下所示

```python
def plan(every, unit, at=None, loop=None,**kwargs):
    def _plan(func):
        return Plan(func,every,unit,at=at,loop=loop, **kwargs)
    return _plan
```

具体函数的参数传递给了你的对象的 `__call__` 方法

```python
    def _call_(self,*fn_args):
        """Used as a decorator"""
        if self.auto_start:
            self.loop.call_soon_threadsafe(self.func,*fn_args)

@plan(every=0,unit="minute")
def job(name):
    print("I'm working...{}".format(name))
```

当你执行
job(name)

实际上执行的是
job(name) = plan(job)(name)

plan() 返回的 Plan(&#x2026;.) 对象
你的装饰器参数全部都传递了这个Plan对象，存储状态，额外的操作都是可以的。

或者说

job(name) = Plan(job,. .. .. ..)(name)

也就是job这个原来是个函数的东西经过装饰器装饰之后， 实际上是一个 Plan对象了。﻿

# and or not的运算优先级<a id="orgheadline30"></a>

一般是推荐用括号清晰表达，然后not我们知道优先级是最高的。我们再看下面这个例子:

    >>> True or True and False
    True

这个例子很好地说明了and和or的优先级顺序，具体就是 <span class="underline">and的优先级比or的要高</span> 。

# 多进程<a id="orgheadline33"></a>

进程的定义是: 一个正在执行的程序实例。每个进程都有一个唯一的进程ID，也就是所谓的 **PID** 。使用 `ps` 命令的第一个列就是每个进程的PID属性。在python中你可以使用 `os.getpid()` 来查看当前进程的PID。

以前只有一个CPU的机器上，多任务操作系统实际上一次也只能运行一个进程，操作系统是通过不断切换各个进程给你一种多任务似乎同时在运行多个程序的感觉的。多CPU机器上是真的可以同时运行多个进程。

## 进程fork<a id="orgheadline31"></a>

进程fork简单来说就类似于git某个项目的fork，进行了一些基本代码信息和其他配置以及其他相关信息的复制或注册。这就相当于在当前代码环境下，你有两个分别单独运行的程序实例了。

下面是一个非常简单的小例子，你可以把os.fork()语句移到print('before fork')之前来看看变化。

```python
import os, time

print('before fork ')
os.fork()

print('say hello from', os.getpid())

time.sleep(1)

print('after fork')
```

对于这个程序简单的理解就是，本py文件编译成字节码进入内存经过某些成为一个程序实例了（其中还包含其他一些信息），然后程序具体运行的时候会通过os.fork来调用系统的fork函数，然后复制本程序实例（以本程序实例目前已经所处的状态），因为print('before fork')已经执行了，所以子进程就不会执行这一行代码了，而是继续os.fork()下面的代码继续执行。此时就相当于有两个程序在运行了，至于后面的打印顺序那说不准的。

关于操作系统具体如何fork的我们可以暂时不考虑，这两个程序实例里面的变量和运行环境基本上是一模一样的，除了运行的状态有所不同之外。fork可以做出一种程序多任务处理方案吧，不过os模块的fork方法目前只支持unix环境。

## 子进程和父进程分开<a id="orgheadline32"></a>

请看下面的代码: 

```python
import os, time

print('before fork ')
pid = os.fork()
if pid:
    print(pid)
    print('say hello from parent', os.getpid())
else:
    print(pid)
    print('say hello from child', os.getpid())

time.sleep(1)

print('after fork')
```

其运行结果大致如下:

    before fork 
    13762
    say hello from parent 13761
    0
    say hello from child 13762
    after fork
    after fork

我们看到在父进程那一边，pid是本父进程的子进程PID，而在子进程那一边，os.fork()返回的是0。可以利用这点将父进程的操作和子进程的操作分开。具体上面的代码if pid 那一块是父进程的，else那一块是子进程的。

# 多线程<a id="orgheadline37"></a>

线程的内部实施细节其实比进程要更加复杂，一般通俗的说法就是线程是轻量级进程，这里不深入讨论具体线程的细节。

python操作线程的主要模块是 **threading**
模块，简单的使用就是新建一个线程对象(Thread)，然后调用 `start` 方法来启动它，具体线程要做些什么由本线程对象的 `run` 确定，你可以重定义它，如果是默认的就是调用本线程Thread类新建是输入的 `target` 参数，这个target参数具体指向某个函数。下面是一个简单的例子: 

```python
import random, threading

result = []

def randchar_number(i):
    number_list = list(range(48,58))
    coden = random.choice(number_list)
    result.append(chr(coden))
    print('thread:', i)

for i in range(8):
    t = threading.Thread(target = randchar_number, args=(i,))
    t.start()

print(''.join(result))
```

    \begin{Verbatim}
    thread: 0
    thread: 1
    thread: 2
    thread: 3
    thread: 4
    thread: 5
    thread: 6
    thread: 7
    22972371

**注意:**  控制参数如果只有一个后面那个逗号必须加上。

## 后台警报线程<a id="orgheadline34"></a>

下面的函数实现了一个后台警报线程，不会阻塞主程序。

```python
def beep(a,b):
    '''make a sound , ref: http://stackoverflow.com/questions/16573051/python-sound-alarm-when-code-finishes
    you need install  ``apt-get install sox``

    :param a: frenquency
    :param b: duration

    create a background thread,so this function does not block the main program
    '''
    def _beep(a,b):
        import os
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (b,a))
    from threading import Thread
    thread = Thread(target=_beep,args=(a,b))
    thread.daemon = True
    thread.start()
```

如上所示，原beep函数调用系统的play命令制造一个声音，其中b是声音持续的时间，所以其是阻塞的。我们将其作为一个线程调用之后，然后其就没有阻塞主程序了。这里的 `daemon` 的意思是让这个线程成为一个后台线程，请参看 [这个网页](http://stackoverflow.com/questions/190010/daemon-threads-explanation) ，其说道后台线程可以不用管了，后面会随着主程序自动关闭。

线程还可以用如下类的风格编写。下面代码参考了  [这个网页](http://www.ibm.com/developerworks/aix/library/au-threadingpython/index.html) 。

```python
import random, threading

threads = []

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.result = ''
    def run(self):
        number_list = list(range(48,58))
        coden = random.choice(number_list)
        self.result = chr(coden)
    def getvalue(self):
        return self.result


for i in range(8):
    t = MyThread()
    t.start()
    t.join()
    threads.append(t)

result = ''
for t in threads:
    result += t.getvalue()
print(result)
```

    05649040
    >>>

上面调用线程对象的 `join` 方法是确保该线程执行完了，其也可能返回异常。上面的做法不太标准，更标准的做法是单独写一行t.join代码: 

    for t in threads:
        t.join()

来确保各个线程都执行完了，如之前的形式并不能达到多任务并行处理的效果。

上面的例子对线程的执行顺序没有特殊要求，如果有的话推荐使用python的queue模块，这里就略过了。

## 多线程: 一个定时器<a id="orgheadline35"></a>

这个例子主要参考了 [这个网页](https://mail.python.org/pipermail/tutor/2004-November/033333.html) 。

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading

class Timer(threading.Thread):
    def __init__(self,interval, action=lambda:print('\a')):
        threading.Thread.__init__(self)
        self.interval = interval
        self.action = action

    def run(self):
        time.sleep(self.interval)
        self.action()

    def set_interval(self,interval):
        self.interval = interval

#timer = Timer(5)
#timer.start()

class CountDownTimer(Timer):
    def run(self):
        counter = self.interval
        for sec in range(self.interval):
            print(counter)
            time.sleep(1.0)
            counter -= 1
        ####
        self.action()

#timer = CountDownTimer(5)
#timer.start()

def hello():
    print('hello\a')

timer = CountDownTimer(5, action = hello)
timer.start()
```

具体还是很简单的，这里之所以使用线程就是为了timer.sleep函数不冻结主程序。

## 多线程下载大文件<a id="orgheadline36"></a>

本小节参考了 [这个网页](http://stackoverflow.com/questions/13973188/requests-with-multiple-connections) 和 [这个网页](http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py) 。

下面的 `get_content_tofile` 函数在目标内容大小大于1M的时候将启动多线程下载方法。其中 `guess_url_filename` 函数是根据url来猜测可能的目标下载文件名字，还只是一个尝试版本。

注意下面使用requests.get函数的时候加上了 `stream=True` 参数，这样连接目标url的时候只是获得头文件信息而不会进一步下载content内容。这方便我们早期根据headers里面的信息做出一些判断。

接下来根据HTTP头文件的 `content-length` 来判断要下载内容的大小，如果没有这个属性，那么目标url是没有content内容的，本函数将不会对这一情况做出反应，这通常是单网页url，使用requests的get方法获取网页文本内容即可。

然后如果目标长度小于1M，那么就直接打开文件，使用requests模块里response对象的\verb+iter\_content+方法来不断迭代完content内容。

如果目标长度大于1M，则采用一种多线程下载方法。首先是\verb+get\_content\_partly+这个函数，接受url和index，这个index是一个简单的索引，具体多少bytes后面还需要计算。关于多线程操作和具体多少bytes的计算细节这里略过讨论了。唯一值得一提的就是HTTP协议的Range属性，begin-end，对应具体的范围0-1024，还包括1024位，所以实际上有1025个bytes，为了获得和我们python中一致的体验，我们让其end为begin+1024-1。这样就有1024个bytes位，然后定位是(0, 1024)，即和python中的一样，不包括1024位。

然后还有一个小信息是，HTTP协议返回的头文件中的\textbf{content-range}属性，如果你请求Range越界了，那么将不会有这个属性。那么begin没有越界，end越界的请求如何呢？HTTP协议处理得很好，这种跨界情况都只返回最后那点content内容。

最后写文件那里降低内存消耗，使用了下面的语句来强制文件流写入文件中，好释放内存，否则你的下载程序内存使用率是剧增的。

    f.flush()
    os.fsync(f.fileno())

```python
import re
def guess_url_filename(url):
    '''根据url来猜测可能的目标文件名，'''
    response = requests.get(url, stream=True)###还有一个content-type信息可以利用
    s = urlsplit(url)
    guess_element = s.path.split('/')[-1]
    guess_pattern = re.compile(r'''
    (.png|.flv)
    $           # end of string
    ''', re.VERBOSE | re.IGNORECASE)

    if re.search(guess_pattern,guess_element):
        filename = guess_element
    else:
        filename = guess_element + '.html'
    return filename

import threading
import os
class DownloadThread(threading.Thread):
    def __init__(self, url,begin,chunk_size = 1024*300):
        threading.Thread.__init__(self)
        self.url = url
        self.begin = begin
        self.chunk_size = chunk_size
        self.result = b''
    def run(self):
        headers = {'Range':'bytes={begin}-{end}'.format(begin = str(self.begin),
            end = str(self.begin + self.chunk_size-1))}

        response = requests.get(url, stream=True, headers = headers)

        if response.headers.get('content-range') is None:
            self.result = 0###表示已经越界了
        else:
            self.result = response.content
            print('start download...', self.begin/1024, 'KB')

    def getvalue(self):
        return self.result

def get_content_partly(url, index):
    threads = []
    content = b''
    chunk_size = 1024*300# 这个不能设置太大也不能设置太小
    block_size = 10*chunk_size# 具体线程数

    for i in range(10):
        t = DownloadThread(url, index * block_size + i*chunk_size )
        t.start()
        threads.append(t)

    for i,t in enumerate(threads):
        t.join()

    for t in threads:
        if  t.getvalue():
            content += t.getvalue()

    return content

import os
def get_content_tofile(url,filename = ''):
    '''简单的根据url获取content，并将其存入内容存入某个文件中。
    如果某个内容size 小于1M 1000000 byte ，则采用多线程下载法'''

    if not filename:
        filename = guess_url_filename(url)

    # NOTE the stream=True parameter
    response = requests.get(url, stream=True)
    if not response.headers.get('content-length'):
        print('this url does not have a content .')
        return 0
    elif response.headers.get('content-length') &lt; '1000000':
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:
        with open(filename, 'wb') as f:
            for i in range(1000000):###very huge
                content = get_content_partly(url, i)
                if content:
                    f.write(content)
                    f.flush()
                    os.fsync(f.fileno())
                else:
                    print('end...')
                    break
```