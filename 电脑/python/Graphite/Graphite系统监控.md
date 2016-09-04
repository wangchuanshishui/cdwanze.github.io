<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 前言</a></li>
</ul>
</div>
</nav>


# 前言<a id="orgheadline1"></a>

显示 Diamond 收集信息，其通道将对接 Carbon， Carbon最基本的Cache层将和 Whisper 协作对时间序列下的数据分门别类放进各个wsp数据库文件中。这个过程还是很清晰的，唯一难点就是virtualenv和各个配置文件等等的协调问题。

比如说Diamond 经过一定配置，其日志输出和配置都可以放入一个文件夹里面去的。然后Carbon在安装的时候特别处理之后:

    pip install --trusted-host pypi.douban.com -i http://pypi.douban.com/simple carbon --install-option="--prefix=/home/wanze/workspace/mywebsite_backend/" --install-option="--install-lib=/home/wanze/workspace/mywebsite_backend/lib/python2.7/site-packages"

重要的配置和输出都可以统一管理，这无疑将会带来很大的便利。

Diamond发出的信息格式如下:

    servers.wanze-ubuntu.iostat.sda6.writes_merged 60.000 1469329380

Carbon层只是对于时间刻度有额外的处理，后面就是API开出来了，具体path，或说target 怎么写 `servers.wanze-ubuntu.iostat.sda6.writes_merged` 然后含义是什么，都要具体看Collector或者更进一步看命令行文档等等，查阅之后才能知晓的。

Graphite-web这个项目老实说不太好配，而且我们常常只需要一个API出口就可以了，其不好配和django太重也有点关系，推荐使用Graphite-API这个项目，flask轻量架构，更灵活，配置更简单，API接口出来了，根本不用操心后面项目动作该如何如何，没有任何限制。

Graphite-API这个项目初步安装之后得出的结论是，放入virtualenv中或者不放影响不大，而在虚拟环境下有个依赖模块 `cairocffi` 不能安装成功，只能sudo命令下安装。然后配置文件统一管理在你的主项目里面即可。

下面就API的使用，查询函数和以上相关的配置等等慢慢详细说明之。

---