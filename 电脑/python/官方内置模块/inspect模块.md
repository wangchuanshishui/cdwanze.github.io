<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. getfile函数</a></li>
<li><a href="#orgheadline2">2. getcallargs函数</a></li>
</ul>
</div>
</nav>

更多信息请参看 [官方文档](https://docs.python.org/3.4/library/inspect.html) 。

# getfile函数<a id="orgheadline1"></a>

传入python object，返回定义该object具体是在那个文件中的。可以如下获取该文件的系统绝对路径地址:

    os.path.abspath(inspect.getfile(func))

值得一提的是，如果该模块被安装进入系统了，那么实际该文件的地址应该是类似这样的形式:

    /usr/local/lib/python3.4/dist-packages/infome-15.10.30-py3.4.egg/infome/web/youdao.py

注意该egg的名字后面的版本号。

# getcallargs函数<a id="orgheadline2"></a>

如下所示:

    params = inspect.getcallargs(func,*args,**kargs)

相当于模拟执行了func函数，然后返回如果执行func函数时其接受的参数字典值（包括必填参数和可选参数）。