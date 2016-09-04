<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. partial类</a></li>
<li><a href="#orgheadline2">2. update_wrapper函数</a></li>
<li><a href="#orgheadline3">3. wraps装饰器</a></li>
<li><a href="#orgheadline4">4. 参考资料</a></li>
</ul>
</div>
</nav>


# partial类<a id="orgheadline1"></a>

functools模块定义了一个partial类，其输入参数如下所示:

    functools.partial(func, *args, **keywords)

其将返回一个partial对象，其有 `__call__` 方法，也就是其可以类似函数进行调用。然后其有 **func** 属性，作为未来函数的调用； **args** 属性，作为未来函数的参数； **keywords** 属性，作为未来函数的可选参数。 简单来说就是partial对原函数对象func进行了封装（所以其特别适合做装饰器）， `newfun=partial(func,args,keywords)` ，使得调用这个newfun对象就好像调用原func一样，只是加上了额外的参数，其中args非可选参数是类似列表append形式，而keywords可选参数或说关键字参数是类似字典update形式。

下面是一个简单的演示例子:

```python
import functools

def fun1(a,b=2):
    print('called fun1 with',a,b)

def show_details(name,f,is_partial=False):
    print(name)
    print(f)
    if is_partial:
        print(f.func)
        print(f.args)
        print(f.keywords)
    else:
        print(f.__name__)

show_details('fun1',fun1)

fun1('fun1 a')

p1 = functools.partial(fun1,'p1 a',b=99)
show_details('p1',p1,True)

p1()
```

其输出如下:

    fun1
    <function fun1 at 0xb705880c>
    fun1
    called fun1 with fun1 a 2
    p1
    functools.partial(<function fun1 at 0xb705880c>, 'p1 a', b=99)
    <function fun1 at 0xb705880c>
    ('p1 a',)
    {'b': 99}
    called fun1 with p1 a 99

这里的逻辑是首先正常执行fun1，然后将fun用partial封装成p1，新增参数字符串'p1 a'和b=4，后面我们可以看到这个p1的参数都加进去了。然后执行这个p1我们看到了参数的变化。

# update\_wrapper函数<a id="orgheadline2"></a>

    functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)

这里参考了 [这个网页](http://www.wklken.me/posts/2013/08/18/python-extra-functools.html#functoolupdate_wrapper) 的描述。

具体参数暂且不论，就最简单的理解就是前面谈及的partial对象一些必要的参数还没有设置好，这里通过一个目标函数将其处理一下，给予其 `__name__` ， `__doc__` 等必要的属性。不过在实际使用的时候我们不需要记住这里是partial对象，wrapper或者wrapped都可以是两个普通的函数对象。

```python
import functools

def wrapped(a, b=2):
    """Docstring for myfunc()."""
    print('\tcalled myfunc with:', a, b)
    return

def wrapper(a):
    print('wrapper',a)

p = functools.update_wrapper(wrapper, wrapped)

print(p.__name__)
print(p.__doc__)
print(p(1))
```

    wrapped
    Docstring for myfunc().
    wrapper 1

我们看到函数还是原来的那个wrapper函数，但函数的一些内在属性如 `__name__` 等则被wrapped函数的覆盖了。

# wraps装饰器<a id="orgheadline3"></a>

参考 [这个网页](http://stackoverflow.com/questions/15357776/what-is-the-difference-between-functools-wraps-and-update-wrapper) 的描述:

这样的形式

    @wraps(f)
    def g():
        ...

就相当于:

    def g():
        ...
    g = update_wrapper(g, f)

也就是g就是wrapper，而f是wrapped。

在实际应用中，可以将这个函数g做成装饰器函数，如下所示:

```python
from functools import wraps

def mywrap(f):
    @wraps(f)
    def wrapper():
        print('wrapper')
    return wrapper

@mywrap
def wrapped(a, b=2):
    """Docstring for myfunc()."""
    print('\tcalled myfunc with:', a, b)
    return
```

这里的mywrap装饰器作用于wrapped函数之后，其除了 `__name__` 等属性还在之外，其他函数执行的方法都被mywrap里面定义的wrapper函数给覆盖了。

# 参考资料<a id="orgheadline4"></a>

1.  [functools模块官方文档](https://docs.python.org/3.4/library/functools.html)
2.  [pymotw网站](http://pymotw.com/2/functools/)