<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. literal_eval函数</a></li>
</ul>
</div>
</nav>

更多信息请参看 [官方文档](https://docs.python.org/3.4/library/ast.html) 。

# literal\_eval函数<a id="orgheadline1"></a>

literal\_eval函数是一个非常有用的函数，其可用于将某个短小的python字符串转化成python object。如下所示:

```python
import ast
def str2pyobj(val):
    '''str to python obj or not changed'''
    try:
        val = ast.literal_eval(val)
    except Exception:###
        pass
    return val
```

支持的python object有: strings, bytes, numbers, tuples, lists, dicts, sets, booleans, and None.

所以一般的字符串如 "1" "3.14" "[1,2,3]" 将其分别转化成为integer float 和list是小菜一碟。当然最好建立异常捕捉，如果转化失败，则原样返回字符串即可。