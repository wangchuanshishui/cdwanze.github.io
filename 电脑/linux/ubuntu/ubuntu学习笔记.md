<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 找不到ffi.h</a></li>
<li><a href="#orgheadline2">2. 访问局域网其他电脑</a></li>
</ul>
</div>
</nav>


# 找不到ffi.h<a id="orgheadline1"></a>

参考了 [这个网页](http://stackoverflow.com/questions/12982486/glib-compile-error-ffi-h-but-libffi-is-installed) 。

    fatal error: ffi.h: No such file or directory

解决方案:

    sudo apt-get install libffi-dev

# 访问局域网其他电脑<a id="orgheadline2"></a>

需要安装samba服务

    sudo apt-get install samba

你也可以新建一个共享文件夹，推荐使用图形管理界面：

    sudo apt-get install system-config-samba