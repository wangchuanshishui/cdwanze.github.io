<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline2">1. 前言</a>
<ul>
<li><a href="#orgheadline1">1.1. 安装</a></li>
</ul>
</li>
<li><a href="#orgheadline3">2. 管理员新建一个仓库</a></li>
<li><a href="#orgheadline4">3. 客户端检出仓库</a></li>
<li><a href="#orgheadline6">4. 客户端将某个文件或文件夹加入索引</a>
<ul>
<li><a href="#orgheadline5">4.1. <code>--force</code></a></li>
</ul>
</li>
<li><a href="#orgheadline7">5. 客户端提交本地修改</a></li>
<li><a href="#orgheadline8">6. 更新服务器仓库的修改到本地</a></li>
<li><a href="#orgheadline9">7. 文件夹约定</a></li>
<li><a href="#orgheadline10">8. 一般客户端的工作流程</a></li>
<li><a href="#orgheadline11">9. 参考资料</a></li>
</ul>
</div>
</nav>


# 前言<a id="orgheadline2"></a>

svn版本控制是一种基于client/server模型很自然的发展，其中server在svn中是一个很重要的概念。而git相比svn更加的去中心化了，这种去中心化是有代价的，那就是git相比svn更加复杂了。

本文只讨论linux下的使用情况。然后作者写这篇文章的时候已经有一定的git使用经验了，可能本文并不适合对版本控制没有任何概念的读者。

## 安装<a id="orgheadline1"></a>

在windwos下推荐使用 [tortoisesvn](http://tortoisesvn.net/) ，就是那只萌哒哒的乌龟。

在ubuntu下则是:

    sudo apt-get install subversion

centos下是:

    sudo yum install subversion

一般用户就使用svn命令，读者可以使用 `svn --help` 来简单看一下用法。和管理员操作相关的还有两个命令 `svnadmin` 和 `svnserve` ，同样可用 `--help` 来看一下用法。

# 管理员新建一个仓库<a id="orgheadline3"></a>

    svnadmin create testsvn

# 客户端检出仓库<a id="orgheadline4"></a>

客户端第一次和服务器交互，需要使用checkout命令来检出仓库。

    svn checkout theurl

# 客户端将某个文件或文件夹加入索引<a id="orgheadline6"></a>

客户端将某个文件或文件夹加入索引:

    svn add doc

这里将文件夹doc里面的所有内容加入索引。

## `--force`<a id="orgheadline5"></a>

如果某个文件夹内某些文件已经add了某些文件还没有add，然后你希望这个文件夹里面所有的文件都add进去，那么可以通过加上选项 `--force` 来达到这个目的。

    svn add --force doc

# 客户端提交本地修改<a id="orgheadline7"></a>

客户端提交本地修改使用commit命令。

    svn commit -m 'say something'

# 更新服务器仓库的修改到本地<a id="orgheadline8"></a>

更新服务器仓库的修改到本地，相当于git 的pull命令，svn对应的是update命令。

    svn update

# 文件夹约定<a id="orgheadline9"></a>

一般约定trunck是开发主线（相当于git的master），然后branches文件夹是开发支线，然后tags文件夹是标签副本。

# 一般客户端的工作流程<a id="orgheadline10"></a>

1.  svn update ，将服务器端的最新内容更新到本地
2.  本地修改项目文件，此外还有 `svn add；svn delete；svn copy；svn move` 。
3.  检视你的修改，svn status ； svn diff。
4.  撤消你的修改，svn revert
5.  发布你的更改，svn commit。

# 参考资料<a id="orgheadline11"></a>

1.  svn 官方文档 1.7版。
2.  基本的入门信息 [这篇网页](http://www.flyne.org/article/851) 介绍得挺好的。