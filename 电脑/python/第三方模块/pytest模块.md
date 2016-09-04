<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 简介</a></li>
<li><a href="#orgheadline2">2. 第一个例子</a></li>
<li><a href="#orgheadline3">3. 捕捉异常</a></li>
</ul>
</div>
</nav>


# 简介<a id="orgheadline1"></a>

pytest是一个流行的python测试开发框架，很多python模块都将其作为标配。

安装就用pip install pytest 即可，然后看下安装情况：

    pytest --version

pytest可以很好的和setuptools模块集成起来，具体设置方法请参看我写的这个python小项目 [pyskeleton](https://github.com/a358003542/pyskeleton) 。

其重要利用了 pytest-runner 这个模块来实现了：

    python setup.py test

这个的输入。

当然你可以安装pytest之后直接下模块文件夹下运行：

    pytest

那么用上面的那种输入风格有什么好处呢，好处就是你直接修改模块和测试就行了，不仅不用安装该模块到系统里面，甚至连build操作都可以不用做:

    python setup.py build

这确实很方便，那么pytest的一些参数怎么传递进去了，如下所示是利用 `--addopts` 这个选项传递进去的:

    python setup.py test --addopts '-v tests/test_pytest.py'

# 第一个例子<a id="orgheadline2"></a>

在tests文件夹下新建一个文件test\_pytest.py，然后写入内容如下：

    def addone(x):
        return x + 1
    
    def test_answer():
        assert addone(3) == 4

然后你可以运行pytest来测试看看。

# 捕捉异常<a id="orgheadline3"></a>

如何捕捉期待的异常呢？如下所示：

```python
from pytest import raises

class MyException(Exception):
    pass

def test_my_exception():
    with raises(MyException):
        raise MyException
```