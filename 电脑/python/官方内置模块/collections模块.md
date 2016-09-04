<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. Counter对象</a></li>
<li><a href="#orgheadline2">2. namedtuple对象</a></li>
<li><a href="#orgheadline3">3. OrderedDict对象</a></li>
</ul>
</div>
</nav>

collections模块里面有一些很有用的数据类型，更多信息请参看 [官方文档](https://docs.python.org/3.4/library/collections.html) 。

# Counter对象<a id="orgheadline1"></a>

# namedtuple对象<a id="orgheadline2"></a>

namedtuple数据类型你可能已经在某处接触到了，其非常有用。比如说argparse模块里面parse命令行输入之后返回的就是一个namedtuple对象。

其使用和概念都很简单，没啥好说的。下面是一个例子（来自官方文档）:

    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> p = Point(11, y=22)     # instantiate with positional or keyword arguments
    >>> p[0] + p[1]             # indexable like the plain tuple (11, 22)
    33
    >>> x, y = p                # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y               # fields also accessible by name
    33
    >>> p                       # readable __repr__ with a name=value style
    Point(x=11, y=22)

# OrderedDict对象<a id="orgheadline3"></a>

python中的字典对象默认各个key是没有顺序的，OrderdDict对象的概念就是在字典概念的基础上让各个key有顺序。

一个例子如下所示（来自官方文档）。简单的理解就是一个字典对象记住了各个key的插入顺序。

    >>> d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
    
    >>> # dictionary sorted by key
    >>> OrderedDict(sorted(d.items(), key=lambda t: t[0]))
    OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
    
    >>> # dictionary sorted by value
    >>> OrderedDict(sorted(d.items(), key=lambda t: t[1]))
    OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
    
    >>> # dictionary sorted by length of the key string
    >>> OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
    OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])