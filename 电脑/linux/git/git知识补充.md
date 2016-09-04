<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 输入 <code>git status</code> 中文路径名是乱码</a></li>
<li><a href="#orgheadline2">2. github走ssh通道</a></li>
</ul>
</div>
</nav>

cdwanze #+LATEX\_CLASS: article

# 输入 `git status` 中文路径名是乱码<a id="orgheadline1"></a>

请读者参看 [这个网页](https://gist.github.com/nightire/5069597) 。

具体在ubuntu下终端的显示，我试了一下只需要如下设置即可:

    git config --global core.quotepath false

简单来说就是git的路径默认转义行为关闭了。官方完整文档解释如下:

> core.quotePath
> The commands that output paths (e.g. ls-files, diff), when not given the -z option, will quote "unusual" characters in the pathname by enclosing the pathname in a double-quote pair and with backslashes the same way strings in C source code are quoted. If this variable is set to false, the bytes higher than 0x80 are not quoted but output as verbatim. Note that double quote, backslash and control characters are always quoted without -z regardless of the setting of this variable.

# github走ssh通道<a id="orgheadline2"></a>

github走ssh通道。之前我都不在意，都是勤快的手工输入密码的。。github那边把你的ssh密钥加进去，然后你的项目 `.git/config` 那个文件的 url 设置为git连接即可，

首先测试一下连通性吧:

    bash>>> ssh git@github.com﻿