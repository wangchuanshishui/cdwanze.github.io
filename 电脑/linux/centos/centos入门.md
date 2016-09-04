<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 前言</a></li>
<li><a href="#orgheadline4">2. yum命令</a>
<ul>
<li><a href="#orgheadline2">2.1. 下载对应的rpm包</a></li>
<li><a href="#orgheadline3">2.2. 本地源文件安装rpm包</a></li>
</ul>
</li>
</ul>
</div>
</nav>


# 前言<a id="orgheadline1"></a>

本文是个centos下各个小技巧，小经验的汇总，因为我之前都是接触的ubuntu debian系，所以姑且称这篇文章为入门性质吧。

# yum命令<a id="orgheadline4"></a>

在ubuntu下最先接触的就是apt-get命令（ubuntu16之后名字精简为apt了），那么centos下类似的命令就是yum命令。rpm系都可以用yum install来安装一些软件包。

## 下载对应的rpm包<a id="orgheadline2"></a>

推荐安装 `yum-utils` 这个软件包：

    yum install yum-utils

然后利用其提供的 yumdownloader 命令来下载对应的rpm包。

## 本地源文件安装rpm包<a id="orgheadline3"></a>

从本地源文件安装rpm包就是用 rpm命令来安装之：

    rpm -i what.rpm