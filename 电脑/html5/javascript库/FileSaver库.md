<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 简介</a></li>
</ul>
</div>
</nav>


# 简介<a id="orgheadline1"></a>

FileSaver库方便你把网页上的一些内容下载到本地，该项目的github地址在 [这里](https://github.com/eligrey/FileSaver.js) 。

具体使用就是一个 `saveAs` 函数。

    saveAs(Blob data, DOMString filename, optional Boolean disableAutoBOM)

如下所示:

    var blob = new Blob(["Hello, world!"], {type: "text/plain;charset=utf-8"});
    saveAs(blob, "hello world.txt");

然后javascript的Blob对象，如果你希望保存html富文本形式，type最好设置为: `{ "type" : "text/xml" }` 。