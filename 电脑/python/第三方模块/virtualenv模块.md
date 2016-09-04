<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 简介</a></li>
<li><a href="#orgheadline3">2. 安装</a>
<ul>
<li><a href="#orgheadline2">2.1. 可能出现的问题</a></li>
</ul>
</li>
<li><a href="#orgheadline4">3. 新建一个项目</a></li>
<li><a href="#orgheadline6">4. 激活本地虚拟环境</a>
<ul>
<li><a href="#orgheadline5">4.1. 通过pip安装某个模块</a></li>
</ul>
</li>
<li><a href="#orgheadline7">5. 退出本地虚拟环境</a></li>
<li><a href="#orgheadline8">6. 使用心得</a></li>
<li><a href="#orgheadline9">7. 参考资料</a></li>
</ul>
</div>
</nav>


# 简介<a id="orgheadline1"></a>

你经常看到很多python高手演讲视频里面他们通常会用到virtualenv命令，这个命令就是python的virutalenv模块提供的。其主要作用就是建立一个封闭独立的python开发环境，因为一个python项目的开发通常会涉及到多个模块，而你激活virtualenv环境之后，通过pip3命令安装的模块是安装在本项目文件夹内的，这样就建立了单独的固定某个模块版本的开发环境。这方面好处应该越到后面就也显露出来了【我开发经验还不是很多，老实说也没有切身体会】，不管怎么说，每一个新的开发环境都用virtualenv模块来控制管理，是个不错的习惯。

# 安装<a id="orgheadline3"></a>

现在都推荐完全使用python3了，所以这里只说pip3了。安装就是用pip3来安装常规安装即可。

```sh
sudo pip3 install virtualenv
```

## 可能出现的问题<a id="orgheadline2"></a>

我用ubuntu的apt-get命令安装的python3-pip，在执行上面命令的时候出了问题，可能是我的pip版本命令过低了。推荐按照 [官方文档](https://pip.pypa.io/en/latest/installing.html) 来安装最新版本的pip3命令。

# 新建一个项目<a id="orgheadline4"></a>

新建一个项目就是使用virutalenv命令，然后后面跟一个文件夹名字，等下要新建的文件夹名字。

```sh
virutalenv helloworld
```

目前这个项目默认使用的就是python3，这很好，就不用改了，毕竟现在推荐完全使用python3来编写代码。然后已经安装好setuptools和pip命令了。

# 激活本地虚拟环境<a id="orgheadline6"></a>

运行下面的命令即进入本地虚拟环境：

```sh
cd helloworld
source bin/activate
```

## 通过pip安装某个模块<a id="orgheadline5"></a>

这里用pip应该也就是pip3，我还不大确定，如果一定是pip3那么就可以简单输入pip即可：

```sh
pip3 install pint
```

然后你看到不需要sudu权限就安装成功了，这说明这个pint模块是安装在本地的，你可以到外面打开一个终端进入python环境或者本地虚拟环境来看下。在本地虚拟环境下输入python即可，默认肯定是python3了。

其他pip命令操作都是和外面一样的，这里就不多说了。

# 退出本地虚拟环境<a id="orgheadline7"></a>

运行deactivate命令即可

```sh
deactivate
```

# 使用心得<a id="orgheadline8"></a>

这里过段时间再来补充具体的使用心得。

# 参考资料<a id="orgheadline9"></a>

1.  [主要参考了这个网站](http://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/)。