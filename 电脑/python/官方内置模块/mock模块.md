<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 简介</a></li>
<li><a href="#orgheadline2">2. 参考资料</a></li>
</ul>
</div>
</nav>


# 简介<a id="orgheadline1"></a>

从python3.3开始mock模块已经成为python标准模块的一部分了，在unittest.mock那里。python2则要考虑单独按照mock模块。

刚开始接触mock模块可能会比较困惑，恩，这东西很神奇，但有什么用。其就是方便做单元测试的，所以要理解mock模块就必须从单元测试的各个需求入手。结果官方文档里面介绍很多的Mock还有MagicMock对象并不怎么常用，我们更常用的是mock的patch功能。而我们在单元测试的时候，使用mock模块很大一部分需求就是我们的单元测试代码对数据库操作或者网络请求部分等，有很大的不可重现性和干扰性，所以我们会patch原有的数据库连接行为，或者网络请求行为，然后修改某些属性，从而达到更便利的单元测试的目的。

刚开始了解mock，这个例子是要弄懂的:

```python
from mymodule import rm

try:
    import mock
except Exception as e:
    from unittest import mock
import unittest

class RmTestCase(unittest.TestCase):

    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os,mock_path):
        mock_path.isfile.return_value = False

        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        mock_path.isfile.return_value = True
        rm("path")
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("path")


if __name__ == '__main__':
    unittest.main()
```

这里本测试脚本要使用 mymodule 模块里面的 os.path ，那么如上patch一下，然后装饰在函数上面，则将会自动传递一个Mock对象进去，mock文档里面有很大篇幅讨论的Mock对象的使用方法这就用的上了。

一般patch的引用原则是:

> Mock an item where it is used, not where it came from.

然后这一般是patch的模块下面的某个属性，如果是patch某个类下的某个属性，则使用 `patch.object` ，其可以专门定制某个类下的某个属性，不过 `__init__` 方法不可以这样做，然后我发现可以通过这样的写法，来重载原类的 `__init__` 定义:

    @mock.patch('api_server.SQLAlchemyProxy', TestSQLAlchemyProxy)
    def test_post(self):

这里的 TestSQLAlchemyProxy 类可以继承自原类，然后重载 `__init__` 方法。这种写法指定new参数之后，后面函数就不会接受参数。

# 参考资料<a id="orgheadline2"></a>

1.  [an introduction to mocking in python](https://www.toptal.com/python/an-introduction-to-mocking-in-python)
2.  [python mock tutorial](http://python-mock-tutorial.readthedocs.io/en/latest/mock.html)