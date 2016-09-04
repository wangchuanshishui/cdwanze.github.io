<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline3">1. 什么是windows的dll文件</a>
<ul>
<li><a href="#orgheadline1">1.1. 静态链接</a></li>
<li><a href="#orgheadline2">1.2. 动态链接</a></li>
</ul>
</li>
<li><a href="#orgheadline4">2. python对接win32 api模块</a></li>
<li><a href="#orgheadline5">3. 在windows下安装python的模块</a></li>
<li><a href="#orgheadline6">4. cygwin环境下pygmentize的编码问题</a></li>
<li><a href="#orgheadline7">5. windows下cmd编码问题</a></li>
</ul>
</div>
</nav>


# 什么是windows的dll文件<a id="orgheadline3"></a>

## 静态链接<a id="orgheadline1"></a>

静态链接是将应用程序调用的库函数拷贝到可执行文件里面。当多个程序调用相同的函数，将会出现同一个函数的多个拷贝。 

## 动态链接<a id="orgheadline2"></a>

动态链接是程序运行时动态地加载所需的函数。比如windows下的dll文件或者linux下的so文件，从这些引入库中拷贝的是重定位信息，然后在需要的时候从这些文件中导入相应的函数。

# python对接win32 api模块<a id="orgheadline4"></a>

python对接win32 api模块推荐使用pywin32模块。

# 在windows下安装python的模块<a id="orgheadline5"></a>

如果有网络那么推荐就使用pip命令来安装，是很方便的，无需多言。如果没有网络的情况那么推荐下载exe或者whl包来安装，其中whl包就是对应的pip install命令，使用的pip wheel技术。

如果实在需要手工安装，通常纯python写的模块没什么问题，就是一些模块使用了cython技术等，其中cython那一块很是引起了我的兴趣。如果有c代码，那么需要安装visual studio2010开发环境，这很不方便。还有一个不是很完美的替代方案就是安装mingw程序，然后写一个distutils.cfg文件，内容如下：

    [build]
    compiler = mingw32

然后将其放入 `C:\Python34\Lib\distutils` 里面，cython可以安装成功，但是有的又不行，是一个不太完美的备选方案。

# cygwin环境下pygmentize的编码问题<a id="orgheadline6"></a>

在cygwin环境下，安装好emacs-win32之后，相关配置跟上，就可以很自如的使用emacs的org模式了，其中额外pygments宏包出现了编码问题，加上 `-O encoding=utf-8` 之后可以解决，代码如下所示：

    (format "pygmentize -O encoding=utf-8  -f html -l %s" lang)

# windows下cmd编码问题<a id="orgheadline7"></a>

在windows下通过geany调用python解释器，是进入的cmd终端模式，目前（win7）默认的是GBK编码，最好改成UTF-8编码。

65001 regid t  &#x2026;. 字体 &#x2026; 待核实。