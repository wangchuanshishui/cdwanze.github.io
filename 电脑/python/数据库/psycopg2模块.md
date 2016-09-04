<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 简介</a></li>
<li><a href="#orgheadline2">2. 安装</a></li>
<li><a href="#orgheadline12">3. 基本的使用</a>
<ul>
<li><a href="#orgheadline3">3.1. 连接数据库</a></li>
<li><a href="#orgheadline4">3.2. 新建一个游标</a></li>
<li><a href="#orgheadline7">3.3. 执行某个SQL语句</a>
<ul>
<li><a href="#orgheadline5">3.3.1. 不要使用百分号字符串替换操作</a></li>
<li><a href="#orgheadline6">3.3.2. 不要使用字符串加法操作</a></li>
</ul>
</li>
<li><a href="#orgheadline8">3.4. fetchone方法</a></li>
<li><a href="#orgheadline9">3.5. 连接的commit方法</a></li>
<li><a href="#orgheadline10">3.6. 游标的close方法</a></li>
<li><a href="#orgheadline11">3.7. 连接的close方法</a></li>
</ul>
</li>
<li><a href="#orgheadline13">4. 其他</a></li>
</ul>
</div>
</nav>


# 简介<a id="orgheadline1"></a>

psycopg2模块是python操控postgresql数据库的模块。模块设计遵循了python的DB API 2.0 协议标准，如果你熟悉sqlite3模块，应该能很快上手。

# 安装<a id="orgheadline2"></a>

推荐用pip3命令安装之：

```sh
sudo pip3 install psycopg2
```

然后确保安装了libpq软件包。

    sudo apt-get install libpq-dev

# 基本的使用<a id="orgheadline12"></a>

## 连接数据库<a id="orgheadline3"></a>

    import psycopg2
    
    conn = psycopg2.connect("dbname=test user=wanze")

具体PostgreSQL那边数据库的设置问题如有问题，请参考 [sql数据库入门](sql数据库入门.html) 一文 。

## 新建一个游标<a id="orgheadline4"></a>

根据对于PostgreSQL的一个连接新建一个游标。

    cur = conn.cursor()

## 执行某个SQL语句<a id="orgheadline7"></a>

通过游标具体执行某个SQL语句

    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

值得一提的是execute方法可以接受一个字符串的替代列表（可迭代对象），作为替代位置占位符只能是 `%s` ，以前那些 `%d %f` 等都不能使用了。 然后在sqlite3那里占位符是 `?` 号。如下所示:

    cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
        (100, "abc'def"))

此外百分号替换符号类似format方法一样也支持变量名替换，但就作为单独字符串的这种替换风格是要被废弃的，单独的字符串操作还是推荐调用format方法。

    '%(a)s %(b)s' % {'a':'test', 'b':123}

游标对象的execute方法也支持类似的这种表达，不过不要和字符串的百分号替换操作混淆起来，如果要进行字符串操作，最好在execute函数之前就做好，而且正如前所述及的，execute的这种替换只是用 `%s` 来表示一个替换位置，而在sqlite3中则是使用的 `?` 。

    cur.execute("""INSERT INTO some_table (an_int, a_date, another_date, a_string)
        VALUES (%(int)s, %(date)s, %(date)s, %(str)s);""",
        {'int': 10, 'str': "O'Reilly", 'date': datetime.date(2005, 11, 18)})

最后文档说

    >>> cur.execute("INSERT INTO foo VALUES (%s)", ("bar"))  # WRONG
    >>> cur.execute("INSERT INTO foo VALUES (%s)", ("bar",)) # correct
    >>> cur.execute("INSERT INTO foo VALUES (%s)", ["bar"])  # correct

其中单元素元组后面还需要跟一个逗号，而列表形式则不需要。所以简单起见后面就写成列表形式以和百分号的字符串替换操作区分开来也是可以的。百分号字符串替换操作如果后面跟个列表，则输出可能不是你想要的:

    >>> '%s' % ['test']
    "['test']"
    >>> '%s' % ('test')
    'test'

### 不要使用百分号字符串替换操作<a id="orgheadline5"></a>

如下所示，这样的语法很容易被 <span class="underline">SQL injection</span> 攻击，

    >>> SQL = "INSERT INTO authors (name) VALUES ('%s');" # NEVER DO THIS
    >>> data = ("O'Reilly", )
    >>> cur.execute(SQL % data) # THIS WILL FAIL MISERABLY
    ProgrammingError: syntax error at or near "Reilly"
    LINE 1: INSERT INTO authors (name) VALUES ('O'Reilly')

### 不要使用字符串加法操作<a id="orgheadline6"></a>

同样不要在execute方法里使用字符串加法操作。

正确的用法就是execute方法第一个参数是SQL语句，第二个参数是替换字符的序列。

## fetchone方法<a id="orgheadline8"></a>

调用游标对象的fetchone方法获得一个游标的返回值。此外还有 **fetchmany** 和 **fetchall** 方法。fetchone如果有，返回一个元组，代表找到的第一条记录，fetchmany接受一个参数，返回一个列表，列表里装的元素类似于fetchone返回的一条记录的元组值，几个参数代表几条记录。然后fetchall就是返回所有的查询记录。

## 连接的commit方法<a id="orgheadline9"></a>

提交对于数据库的更改

## 游标的close方法<a id="orgheadline10"></a>

关闭游标

## 连接的close方法<a id="orgheadline11"></a>

关闭连接。

# 其他<a id="orgheadline13"></a>