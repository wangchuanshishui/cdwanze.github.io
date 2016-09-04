<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline3">1. 简介</a>
<ul>
<li><a href="#orgheadline1">1.1. 安装和配置</a></li>
<li><a href="#orgheadline2">1.2. 安装pymongo</a></li>
</ul>
</li>
<li><a href="#orgheadline15">2. mongodb入门</a>
<ul>
<li><a href="#orgheadline4">2.1. mongo命令简介</a></li>
<li><a href="#orgheadline5">2.2. 备份和还原</a></li>
<li><a href="#orgheadline6">2.3. mongodb的数据类型</a></li>
<li><a href="#orgheadline7">2.4. 连接数据库</a></li>
<li><a href="#orgheadline8">2.5. 插入数据</a></li>
<li><a href="#orgheadline10">2.6. 更新数据</a>
<ul>
<li><a href="#orgheadline9">2.6.1. 更新修饰符清单</a></li>
</ul>
</li>
<li><a href="#orgheadline11">2.7. 过滤器语法清单</a></li>
<li><a href="#orgheadline12">2.8. 删除文档</a></li>
<li><a href="#orgheadline13">2.9. find方法</a></li>
<li><a href="#orgheadline14">2.10. 光标对象</a></li>
</ul>
</li>
<li><a href="#orgheadline16">3. 集群服务器</a></li>
<li><a href="#orgheadline17">4. 备份</a></li>
<li><a href="#orgheadline18">5. json格式问题</a></li>
<li><a href="#orgheadline19">6. 参考资料</a></li>
</ul>
</div>
</nav>


# 简介<a id="orgheadline3"></a>

mongodb和sql的区别很大，虽然有类似的比较，如: mongodb的collection概念类似于sql的table概念；在sql表格中的column相当于mongodb文档中的key，在sql表格中的row相当于mongodb文档中的value；然后sql中的一行记录相当于mongodb的一个文档。但这只是就数据库概念来说的类比，具体到操作细节和数据库存储风格设计上还是有很大的差异的。

其中mongodb在存储上会比较灵活一点，mongodb中所谓的文档在使用上有点类似于python中的字典，所以mongodb一个collection里面各个文档之间并没有相同模式(same schema)的要求，然后就是一个文档里面有个key的值也可以是某个文档（或说字典更直观一点）。同时最值得强调一点的是mongodb和我们以前接触的SQL关系数据库最大的不同就是其内部没有关系连接这个概念，也就是没有类似的join语句的概念。然后从我初步的使用经验来判断，mongodb先在一个collection里面查询一个值，又在一个collection里面查询一个值，这种操作风格会特别的慢，所以正确使用mongodb的风格是关系最紧密一组实体都放在一起，而所有和这些实体相关的子属性部分，最好都放入文档内部，以字典中的字典的形式存储进去，这样mongodb的查询才有效率。

将mongodb的collection理解为集合更好于理解为SQL的table概念，同时我们看到对于mongodb来说，某些冗余重复信息可能是必要的甚至是很好的设计风格。总之我们应该避免跨集合的查询，关于mongodb如何正确的使用和设计，以后还需要专门讨论。

## 安装和配置<a id="orgheadline1"></a>

ubuntu下的安装是:

```sh
sudo apt-get install mongodb
```

这样安装之后提供的命令有mongod和mongo。其中mongod是其中mongodb的后台服务，默认是启动一个了的，所以如果你简单再输入mongod将会出错。你可以通过

    sudo service --status-all

来查看一下。mongodb service默认的端口号是 `27017` 。你可以通过给mongod指定另外的端口号和另外的数据库保存路径来另外建立一个mongodb的后台服务，具体如下所示:

    mongod --dbpath ~/mongodb --port 12321

具体这个文件夹你需要事先创建好。你可以在浏览器中输入 `localhost:12321` 来确认一下，然后按照浏览器的提示，如果输入 `localhost:13321` 还可以看到该数据库更多的信息。

默认mongodb的dbpath是 `/var/lib/mongodb` ，然后如果你需要用mongo命令来连接它的话，就如下输入:

    mongo localhost:12321

## 安装pymongo<a id="orgheadline2"></a>

pymongo是mongodb的python接口，具体就用pip命令安装之即可:

    sudo pip2 install pymongo

一个简单的pymongo例子如下所示:

```python
import sys

from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    client = MongoClient(host='localhost',port=27017)
    print("Connection successfully")
except ConnectionFailure:
    sys.stderr.write("Could not connect the mongodb")
    sys.exit(1)

db = client['pytest']

user_janedoe = {
    "username" : "janedoe",
    "firstname" : "jane",
    "lastname" : "Doe",
    "dateofbirth" : datetime(1980,4,12),
    "score" : 0
    }
db.users.insert(user_janedoe)
```

读者可以先测一下，更详细的讨论后面再说吧。

# mongodb入门<a id="orgheadline15"></a>

## mongo命令简介<a id="orgheadline4"></a>

下面是一些常用命令一览:

-   `show dbs` 显示所有数据库名字
-   `db` 显示当前数据库名字
-   `use dbname` 切换到某个数据库或者创建某个数据库，要实际新建一个数据库还需要往里面塞点东西。比如:

    db.users.save({username:'zhangsan'})

这里的db就是db，并没有所谓的具体某个dbname意思。

-   `show collections` 显示当前数据库的所有colletions名字。
-   `exit` 退出mongo

## 备份和还原<a id="orgheadline5"></a>

使用 `mongodump` 命令进行mongodb的备份操作，使用 `mongorestore` 还原操作。

mongodump简单的操作就如下:

    mongodump

默认对接的是localhost:27017，然后备份文件放于当前工作目录的dump文件夹下。如果是其他端口或ip可用-h选项设置之，如下所示:

    mongodump -h localhost:37017

mongorestore简单的使用如下所示:

    mongorestore -h localhost:37017 dump

其中dump就是要还原的对应的备份文件夹名，然后可以通过-h选项来具体设置还原到那里去。

## mongodb的数据类型<a id="orgheadline6"></a>

-   null值
-   布尔值
-   数值，默认是64位浮点值，若想用整型则使用 NumberInt NumberLong ，其分别对应4字节和8字节有符号的整型值。
-   字符串值
-   date值
-   正则表达式值
-   array值
-   嵌套文档值，mongodb的文档可以嵌套文档的。
-   ObjectID

这些数据类型和python中的一些数据类型多能够对应上，值得一提的就是python的datetime模块的datetime对象是可以直接用来作为Date类型被pymongo接受的。

## 连接数据库<a id="orgheadline7"></a>

我写了 `get_mongodb_client` 这样一个函数，其将用于获取某个mongodb的连接client。

    from datetime import datetime
    from pymongo import MongoClient
    from pymongo.errors import ConnectionFailure
    
    import logging
    logging.basicConfig(level=logging.DEBUG)
    
    def get_mongodb_client(dburl,dbport=27017,repset=None):
        if not dbport:##不排除某些dbport是bool假值传进来
            dbport = 27017
        try:
            dbport = int(dbport)
            ## 不排除字符串赋值的情况，然后其他ValueError情况都捕捉并将dbport赋值为默认值27017
        except ValueError:
            dbport = 27017
    
        try:
            if repset is None:
                mongodb_client = MongoClient(host=dburl,port=dbport)
            else:
                mongodb_client = MongoClient(host=dburl,port=dbport,replicaset=repset)
            return mongodb_client
        except ConnectionFailure as ex:
            logging.warning(ex)

然后我们利用这个函数来获得一个mongodb client对象，

    client = get_mongodb_client("localhost",dbport="27017")

然后利用这个mongodb client对象来获得mongodb的某个具体数据库的db变量:

    db = client['pytest']

然后后面我们就可以这样用几乎接近于在mongo命令行终端的使用语法进行操作了:

    >>> db.users.find_one()
    {u'username': u'janedoe', u'firstname': u'jane', u'lastname': u'Doe', u'dateofbirth': datetime.datetime(1980, 4, 12, 0, 0), u'score': 0, u'_id': ObjectId('5593ae582d58e415e6dc88c9')}

这里的 `db.users.find_one` 其中db是某个数据库，然后users是该数据库下的某个collection名，更加偏python风格的写法是:

    >>> db['users'].find_one()
    {u'username': u'janedoe', u'firstname': u'jane', u'lastname': u'Doe', u'dateofbirth': datetime.datetime(1980, 4, 12, 0, 0), u'score': 0, u'_id': ObjectId('5593ae582d58e415e6dc88c9')}

但这有点怪，因为这会误导人们意味还可以 `db.get("users")`  这样用，而这样是会报错的。

## 插入数据<a id="orgheadline8"></a>

可以调用Collection对象的insert方法来插入一个新的记录，不过官方文档说这个insert方法将被废弃了，新的用户推荐用 `insert_one` 和 `insert_many` 方法。其中insert\_one是插入一个文档，然后insert\_many第一个参数是一个列表，也就是插入多个文档组成的列表。

    db.users.insert_one{'name':"张三"}

这两个方法是立即在数据库中生效的。然后如果我们如果希望是某原文档存在则修改否则就插入这样的逻辑是，则需要使用update方法，具体见下面。

## 更新数据<a id="orgheadline10"></a>

在最新的pymongo文档中，update方法也被废弃了，取而代之的是 `replace_one` ， `update_one` ， `update_many` 这三个方法。

    replace_one(filter, replacement, upsert=False)
    update_one(filter, update, upsert=False)
    update_many(filter, update, upsert=False)

这三个方法首先通过filter过滤器获得一些目标文档，如果upsert设置为True，并且过滤器过滤之后没有找到目标文档，则将执行插入操作。然后replace\_one和update\_one都只对找到的第一个文档进行操作，然后replace\_one是替换操作，而update\_one是更新操作。

其中replace\_one就是用一个新的文档替换旧的文档这很好理解，而update\_one则需要说一下。mongodb的原生update方法有两种模式，一种是替换模式；另一种更新修饰符模式。这里pymongo将这两种模式分开来了。update\_one就对应那个更新修饰符模式，而不能使用新文档替换旧文档那种模式了。

### 更新修饰符清单<a id="orgheadline9"></a>

-   `$inc`  元素加法，某个元素加上多少，一般是数值加法吧。

    "$inc":{"score":1} ——文档的score属性将加上1

-   `$set`  元素设置值，某个元素具体设置为多少值。

    "$set":{"username":"niall"}——文档的username属性具体设置为niall。

-   `$unset` 删除某个属性。

    "$unset":{"username":1}——文档的username属性被删除了。

-   `$push` 列表元素append操作。

    "$push":{"emails":"foo@example.com"}——文档的emails将会添加"foo@example.com"，如果原来没有email这个键，那么其值为:["foo@example.com"]

-   `$pop` 列表元素的pop操作。

    "$pop":{"emails":1}——文档的emails列表右边最后一个元素将被删除。这可能不太好用，pull会更加精确的删除

-   `$pull` 列表元素精确移除某个子元素。

    "$pull":{"emails":"foo@example.com"}——文档的emails列表中的"foo@example.com"将被移除

-   `$pullAll` 类似上面的pull，但是一次移除多个列表子元素操作。

    $pullAll":{"emails":["foo@example.com", "foo2@example.com"]}——文档emails列表的"foo@example.com", "foo2@example.com"都将被移除

-   `$rename` 某个属性键名字更改

    "$rename":{"emails":"old_emails"}

-   `$addToSet` 给某个列表元素添加某个子元素，是确保其存在的逻辑，也就是有则不加，没有则加上。

    "$addToSet":{"emails":"foo@example.com"}

这里顺便把过滤器语法也介绍一下:

## 过滤器语法清单<a id="orgheadline11"></a>

    q = {
    "firstname" : "jane",
    "surname" : "doe"
    }

过滤器各个字句默认AND逻辑连接，若要或逻辑则要使用 `$or` 连接。

要score大于0如下所示:

    q = {
    "score" : { "$gt" : 0 }
    }

类似的操作符还有:

-   `$gt`    >
-   `$lt`    <
-   `$gte`   >=
-   `$lte`   <=
-   `$all`  比如 "skills":{"$all":["mongodb","python"]} ，那么skills这个列表必须包含mongodb和python这两个子元。
-   `$exists` 属性必须存在
-   `$mod`
-   `$ne` 不等于 !=
-   `$in` 某元素于某个列表中
-   `$nin` 某个元素不在某个列表中
-   `$nor`  "$nor":[{"language":"english"},{"country":"usa"}] 控制某个元素不是某个值
-   `$or`  或语句的表达， "$or":[{"language”:"english"},{"country":"usa"}]
-   `$size` 列表的size或者说所含元素个数必须是多少

## 删除文档<a id="orgheadline12"></a>

同样原pymongo的remove方法被废弃了，取而代之的是 `delete_one` 和 `delete_many` 方法。其都只接受一个过滤器参数，然后内在操作逻辑就是根据过滤器找到的文档，删除一个或者全部删除。

    delete_one(filter)
    delete_many(filter)

## find方法<a id="orgheadline13"></a>

find方法，过滤查询某个记录，如果不带过滤器参数，则返回所有目标记录。在mongo终端命令下输入

    db.users.find()

即返回users这个collection所有的记录，而在pymongo中是返回的一个光标对象，如下所示:

    <pymongo.cursor.Cursor object at 0x7fb5e7ca4210>

其返回的是一个光标对象，可以直接用for语句于之上进行迭代操作，很是方便。

然后类似mongodb的findOne，pymongo的Collection对象也有一个find\_one方法，具体使用上和find方法没什么差异，除了最后返回的是找到的第一个文档，以字典值的形式返回。

## 光标对象<a id="orgheadline14"></a>

这个光标对象还有count方法返回所含记录数，还有sort方法应该是对接的mongodb其内的sort方法。cout方法并不受光标对象是否迭代的影响，但是sort方法注意不能在光标对象发生迭代之后操作，最好是先sort之后再进行迭代。

sort方法的语法和mongodb原生的sort方法语法有点差异:

    for doc in collection.find().sort([
            ('field1', pymongo.ASCENDING),
            ('field2', pymongo.DESCENDING)]):
        print(doc)

如果只是对一个排序，也可以写成这样的形式:

    for doc in collection.find().sort('field', pymongo.ASCENDING):
        print(doc)

# 集群服务器<a id="orgheadline16"></a>

连接集群服务器格式如下所示（参考了 [这个网页](http://stackoverflow.com/questions/13912765/how-do-you-connect-to-a-replicaset-from-a-mongodb-shell) ）:

    mongo --host=inors0504/redstone:27019,ltprod01:27108,innoali02:27018

# 备份<a id="orgheadline17"></a>

具体是利用mongodump命令来进行备份， `--host` 用来控制连接url， `--db` 用来控制具体备份那个数据库，还可以具体到某个collection。然后 `-o` 用来控制输出的备份文件夹名。

    mongodump --host=atlas-04  --db=mls06085  -o mongodump_2015-07-29

# json格式问题<a id="orgheadline18"></a>

请参看 [这个网页](http://stackoverflow.com/questions/16586180/typeerror-objectid-is-not-json-serializable) ，比如说你把mongodb里面的数据读出来了，然后可能有存入到json文件中去的需求，常规操作会出现这样的错误:

    TypeError: ObjectId('') is not JSON serializable

上面的网页提到的自己添加json Encode的方法并不是很好，然后下面的一个答案不错，具体如下所示:

    >>> from bson import Binary, Code
    >>> from bson.json_util import dumps
    >>> dumps([{'foo': [1, 2]},
    ...        {'bar': {'hello': 'world'}},
    ...        {'code': Code("function x() { return 1; }")},
    ...        {'bin': Binary("")}])

更多细节请参看 [这里](http://api.mongodb.org/python/current/api/bson/json_util.html) ，这个bson也是pymongo模块里面的。

# 参考资料<a id="orgheadline19"></a>

1.  mongodb and python, Author:Niall O’Higgins, year:2011
2.  mongodb - the definitive guide, Author:Kristina Chodorow, May 2013:Second Edition
3.  MongoDB Basics , Author:David Hows, Peter Membrey etc. year: 2014