<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 前言</a></li>
</ul>
</div>
</nav>


# 前言<a id="orgheadline1"></a>

scrapy模块用来进行网络抓取还是很便捷的，其python3的支持工作还是进行中，不过可以通过直接写爬虫脚本然后在python3中通过系统调用python2的方式获取抓取来的数据。所以刚开始我想采用的风格就是这种单脚本运行风格，以后python3支持了可能会考虑更紧密的继承到其他python3模块中去的风格。

如同官方文档说明的，最简单的使用就是定义一个 `spider.py` 爬虫文件，然后:

    scrapy runspider spider.py

然后可以通过 `-o` 选项来控制具体的输出文件，默认json格式。