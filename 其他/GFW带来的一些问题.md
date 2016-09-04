<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. pypi下载用国内源</a></li>
<li><a href="#orgheadline2">2. js 用国内cdn源</a></li>
</ul>
</div>
</nav>


# pypi下载用国内源<a id="orgheadline1"></a>

    pip install --trusted-host pypi.douban.com -i http://pypi.douban.com/simple carbon

或者修改本机的pypi配置，在当前用户主文件夹下的 `.pip/pip.conf` 下加入内容:

    [global] 
    index-url = http://pypi.douban.com/simple

windows下是 `%HOMEPATH%\pip\pip.ini` 。

如果你遇到提示说要加入参数 `--trusted-host pypi.douban.com` ，你可以加上这个选项，或者在pypi配置里面加上：

    [install]
    trusted-host = pypi.douban.com

# js 用国内cdn源<a id="orgheadline2"></a>

推荐 [这个网站](http://www.bootcdn.cn/) 。