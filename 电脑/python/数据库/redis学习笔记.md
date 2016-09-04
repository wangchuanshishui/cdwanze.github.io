<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline5">1. 简介</a>
<ul>
<li><a href="#orgheadline1">1.1. 安装</a></li>
<li><a href="#orgheadline2">1.2. 数据库存储在那</a></li>
<li><a href="#orgheadline3">1.3. redis-cli</a></li>
<li><a href="#orgheadline4">1.4. python那边</a></li>
</ul>
</li>
<li><a href="#orgheadline6">2. python那边</a></li>
<li><a href="#orgheadline7">3. <span class="todo nilTODO">TODO</span> </a></li>
</ul>
</div>
</nav>


# 简介<a id="orgheadline5"></a>

redis是一个很有意思的数据库服务东西，其可以简单看作in-memory的常规那种one-key-one-value 类似字典的数据结构实时存储支持工具。最简单的应用我们可以用redis来做缓存来加速程序，当然还有其他高级用法等着你去发现。

## 安装<a id="orgheadline1"></a>

你需要安装redis服务，在ubuntu下是:

```sh
sudo apt-get install redis-server
```

然后需要安装python对接redis服务的接口:

```sh
sudo pip3 install redis
```

其github地址在 [这里](https://github.com/andymccurdy/redis-py) 。

## 数据库存储在那<a id="orgheadline2"></a>

数据首先放在内存里面的，然后redis有一个定时save机制，其细节暂时略过，总是redis-server会定时将数据save到dump.rdb里面去。我们可以在redis的配置文件:

    bash>>> sudo gedit /etc/redis/redis.conf

里面找到save具体的存储地址，大概在这里:

    bash>>> cd /var/lib/redis/
    bash>>> ls
    dump.rdb

然后我们当我们手动输入

    save

命令时redis-server会执行一次save操作。然后如果我们输入 `shutdown` 命令关闭redis-server，redis-server也会预先执行一次save操作。因为我们在ubuntu下使用的redis-server是作为系统服务后台自动运行的，其在开机的时候就会自动加载目标数据库。然后需要注意的是如果你把系统默认的redis-server关闭了，另外开辟的是一个独立的redis-server，其save就会save在终端当前工作目录，而且数据库和系统默认的那个redis-server是分开独立不相干的。

## redis-cli<a id="orgheadline3"></a>

输入 `redis-cli` 会视图连接默认的那个port 6379的redis-server，然后可以执行一些操作，简单读者简单看一下官方网页的 [互动教程](http://try.redis.io/) ，做的很好。

## python那边<a id="orgheadline4"></a>

python那边最基本的操作如下所示:

```python
&gt;&gt;&gt; import redis
&gt;&gt;&gt; r = redis.StrictRedis(host='localhost', port=6379, db=0)
&gt;&gt;&gt; r.set('foo', 'bar')
True
&gt;&gt;&gt; r.get('foo')
'bar'
```

最基本的如 `set` `get` 操作就不用多说了。

# python那边<a id="orgheadline6"></a>

python那边接口很简单，如上所示，你获得一个 `StrictRedis` 对象（新用户都推荐使用StrictRedis）之后，就是调用该对对象的一些方法罢了。官方文档在 [这里](https://redis-py.readthedocs.org/en/latest/) ，比较简单，大抵看源码估计也差不多的。比如说redis的 `del` 操作，在python这边对应的就是 `delete` 方法:

```python
def delete(self, *names):
    "Delete one or more keys specified by ``names``"
    return self.execute_command('DEL', *names)
```

还有很多方法后面在慢慢介绍，这里先介绍那个 `ConnectionPool` 概念，redis-py所有的连接都是如下模式:

    >>> pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    >>> r = redis.Redis(connection_pool=pool)

也就是都通过一个连接池对象来进行连接操作的。然后连接池对象还可以调配一个 `connection_class` ，其是一个 `Connection` 对象。这些都是底层的连接方法实现细节，可能某些时候需要考虑。

# TODO <a id="orgheadline7"></a>

更多细节补充