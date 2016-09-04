<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 安装</a></li>
<li><a href="#orgheadline2">2. setuptools基础</a></li>
<li><a href="#orgheadline3">3. pkg_resources模块来管理读取资源文件</a></li>
<li><a href="#orgheadline4">4. 在pypi上注册你的软件</a></li>
<li><a href="#orgheadline5">5. 在pypi上上传你的软件</a></li>
<li><a href="#orgheadline6">6. 下载安装源文件</a></li>
</ul>
</div>
</nav>

虽然官方内置distutils模块也能实现类似的功能，不过现在人们更常用的是第三方模块setuptools，相当于distutils模块的加强版，初学者推荐就使用setuptools模块。更多内容请参看 [官方文档](https://pythonhosted.org/setuptools/index.html) 。

# 安装<a id="orgheadline1"></a>

安装就是先安装pip3：

    sudo apt-get install python3-pip

然后通过pip3来安装setuptools：

    sudo pip3 install setuptools

# setuptools基础<a id="orgheadline2"></a>

安装官方文档最简单的“setup.py”文件如下所示：

```python
from setuptools import setup, find_packages
setup(
    name = "HelloWorld",
    version = "0.1",
    packages = find_packages(),
)
```

第一行是从setuptools模块中引入setup函数和find\_packages函数。

setup函数接受一系列的字典值，下面就setup函数的一些字典值的含义慢慢道来：

-   **name:** 本软件的名字
-   **version:** 本软件的版本号
-   **author:** 本软件的作者
-   **author\_email:** 本软件作者的邮箱
-   **maintainer:** 本软件的维护者
-   **maintainer\_email:** 本软件维护者的邮箱
-   **contact:** 本软件的联系人。可以不写，则是维护者的名字，如果没有则是作者的名字。
-   **contact\_email:** 本软件的联系人的邮箱，可以不写，则是维护者的邮箱，如果没有则是作者的邮箱。
-   **license:** 本软件的license
-   **url:** 本软件项目主页地址
-   **description:** 本软件的简要描述
-   **long\_description:** 本软件的完整描述，一般如下定义一行函数，然后读取本地目录下面README.md文件。

```python
import os.path
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
```

然后long\_description如下设置：

```python
long_description=read('README.md'),
```

-   **platforms:** 本软件经过测试可运行的平台
-   **classifiers:** 本软件的分类，请参考[这个网页](https://pypi.python.org/pypi?%3Aaction=list_classifiers) 给出一些值。是字符串的列表。
-   **keywords:** 本软件在pypi上搜索的关键词，字符串的列表。
-   **packages:** 你的软件依赖的模块。一般如下使用：

```python
packages = find_packages(),
```

则你文件夹下有 `__init__.py` 文件的都将视作python模块并加入进去。

除此之外你也可以直接手工输入你的模块名字，具体就是字符串的列表。

-   **entry\_point:** entry\_point属性视图解决在Linux <sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup> 下的脚本调用问题。如下所示：

```python
entry_points = {
'console_scripts' :[ 'zwc=zwc.zwc:main',],
}
```

其中zwc是你的shell调用的名字，然后zwc是你的模块，另外一个zwc是你的主模块的子模块，然后main是其中的main函数。这就是你的shell调用程序的接口了。类似的还有gui\_script可以控制你调用GUI图形的命令入口。

-   **install\_requires:** 接受字符串的列表值，将你依赖的可以通过pip安装的模块名放入进去，然后你的软件安装会自动检测并安装这些依赖模块。

-   **setup\_requires:** 和 `install_requires` 类似，所不同的是这个更加侧重于本 `setup.py` 所需要的依赖。然后注意 `setup_requires` 只是把依赖模块下载下来，还没有具体安装，因为 `setup.py` 具体还在执行。如果你希望某个依赖模块至于 `setup.py` 就可用，则需要将该依赖模块加入到 `install_requires` 和 `setup_requires` 中。

-   **package\_data:** 你的软件的模块额外附加的（除了py文件的）其他文件，具体设置类似这样 `{"skeleton":['*.txt'],}` 其中skeleton这里就是具体的你的软件的模块（对应的文件夹名），然后后面跟着的就是一系列的文件名列表，可以接受glob语法。注意这里只能包含你的模块文件夹也就是前面通过packages控制的文件夹下面的内容。
-   **include\_package\_data:** 这个一般设置为True，似乎可以省略？

其他不常用的属性值列在下面：

-   **scripts:** 不推荐使用，推荐通过entry\_point来生成脚本。
-   **py\_modules:** 不推荐使用，推荐使用packages来管理模块。
-   **data\_files:** 前面的package\_data是只能在你的模块文件夹里面的其他数据文件等，然后可能还有一些数据文件你需要包含的，用data\_files来控制，具体后面跟着的参数格式如下面例子所示：

```python
data_files = [('icos',['icos/wise.ico'])],
#这是添加的icos文件夹下面的wise.ico文件
data_files = [('',['skeleton.tar.gz'])],
#这是添加的主目录下的skeleton.tar.gz文件
```

值得一提的是data\_files不能接受glob语法。

data\_files已经不推荐使用了，推荐用package\_data来管理，可以方便用pkg\_resources里面的方法来引用其中的资源文件。具体说明请看后面。

# pkg\_resources模块来管理读取资源文件<a id="orgheadline3"></a>

如下所示

    from pkg_resources import resource_filename
    resource_stream('wise','icos/Folder-Documents.ico')

第一个参数是模块名字，第二个参数是模块中的文件的相对路径表达。

上面的例子是resource\_filename，返回的是引用的文件名。此外还有命令：resource\_string，参数和resource\_filename一样，除了它返回的是字节流。这个字节流可以赋值给某个变量从而直接使用，或者存储在某个文件里面。

# 在pypi上注册你的软件<a id="orgheadline4"></a>

具体很简单，就是

```sh
python3 setup.py register
```

你需要在pypi官网上注册一个帐号，然后你的软件不一定能够注册成功，因为很多好名字都被别人取了。。

# 在pypi上上传你的软件<a id="orgheadline5"></a>

```sh
python3 setup.py sdist upload
```

# 下载安装源文件<a id="orgheadline6"></a>

参考了 [这个网页](http://stackoverflow.com/questions/7300321/how-to-use-pythons-pip-to-download-and-keep-the-zipped-files-for-a-package) 。

    pip install --download="/pth/to/downloaded/files" package_name

<div id="footnotes">
<h2 class="footnotes">Footnotes: </h2>
<div id="text-footnotes">

<div class="footdef"><sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> <div class="footpara">windows下的情况不清楚。</div></div>


</div>
</div>