<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 简介</a></li>
</ul>
</div>
</nav>


# 简介<a id="orgheadline1"></a>

eventlet是python的一个网络并发解决方案模块。其官方文档在 [这里](http://eventlet.net/) 。

    pip install eventlet

最简单的一个例子:

```python
import eventlet
from eventlet.green import urllib2

urls = ["http://www.google.com/intl/en_ALL/images/logo.gif",
       "https://www.python.org/static/img/python-logo.png",
       "http://us.i1.yimg.com/us.yimg.com/i/ww/beta/y3.gif"]

def fetch(url):
    return urllib2.urlopen(url).read()

pool = eventlet.GreenPool()
for body in pool.imap(fetch, urls):
    print("got body", len(body))
```