<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 如何把python中time模块的 <code>struct_time</code> 对象转化成为 <code>datetime</code> object</a></li>
</ul>
</div>
</nav>


# 如何把python中time模块的 `struct_time` 对象转化成为 `datetime` object<a id="orgheadline1"></a>

参看 [这个网页](http://stackoverflow.com/questions/1697815/how-do-you-convert-a-python-time-struct-time-object-into-a-datetime-object) 。

    from time import mktime

mktime函数接受time模块的 `struct_time` object，其可以来自time模块的 `gmtime` `localtime` `strptime` 这些函数，mktime函数将返回一个时间戳，然后用datetime模块的 `fromtimestamp` 函数可以接受这个时间戳。

总的过程即:

    from time import mktime
    from datetime import datetime
    
    dt = datetime.fromtimestamp(mktime(struct))