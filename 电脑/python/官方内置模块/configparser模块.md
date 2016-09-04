<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. ConfigParser模块</a></li>
<li><a href="#orgheadline2">2. 配置文件的格式</a></li>
<li><a href="#orgheadline7">3. SafeConfigParser类</a>
<ul>
<li><a href="#orgheadline3">3.1. 读取一个配置文件</a></li>
<li><a href="#orgheadline4">3.2. 获取某个值</a></li>
<li><a href="#orgheadline5">3.3. 插入或修改某个值</a></li>
<li><a href="#orgheadline6">3.4. 写入配置文件</a></li>
</ul>
</li>
<li><a href="#orgheadline13">4. 其他额外的一些方法</a>
<ul>
<li><a href="#orgheadline8">4.1. getint方法</a></li>
<li><a href="#orgheadline9">4.2. getfloat方法</a></li>
<li><a href="#orgheadline10">4.3. getboolean方法</a></li>
<li><a href="#orgheadline11">4.4. items方法</a></li>
<li><a href="#orgheadline12">4.5. has_section</a></li>
</ul>
</li>
<li><a href="#orgheadline18">5. python3的情况</a>
<ul>
<li><a href="#orgheadline14">5.1. 新建一个configparser对象</a></li>
<li><a href="#orgheadline15">5.2. 读取某个config文件</a></li>
<li><a href="#orgheadline16">5.3. 如同字典一般操作configparser对象</a></li>
<li><a href="#orgheadline17">5.4. 调用write方法写入</a></li>
</ul>
</li>
<li><a href="#orgheadline19">6. 不默认更改大小写</a></li>
</ul>
</div>
</nav>


# ConfigParser模块<a id="orgheadline1"></a>

简单的配置文件管理就用python的内置模块ConfigParse，在python3下是configparser。

具体使用新用户推荐就用 `SafeConfigParser` 类，其继承自 `Configparer` 类，其又继承自 `RawConfigParser` 类。我在初步学习了python2的ConfigParser模块的使用之后，一个感想就是config应该建立类似字典的api出来，这样对用户的使用更加友好，然后看到python3的configparser，果然python3对这个模块的修改让其更加简单易用了，现在python3里面的config更接近字典的api操作了。

下面是python3官方文档提供的例子:

    >>> import configparser
    >>> config = configparser.ConfigParser()
    >>> config['DEFAULT'] = {'ServerAliveInterval': '45',
    ...                      'Compression': 'yes',
    ...                      'CompressionLevel': '9'}
    >>> config['bitbucket.org'] = {}
    >>> config['bitbucket.org']['User'] = 'hg'
    >>> config['topsecret.server.com'] = {}
    >>> topsecret = config['topsecret.server.com']
    >>> topsecret['Port'] = '50022'     # mutates the parser
    >>> topsecret['ForwardX11'] = 'no'  # same here
    >>> config['DEFAULT']['ForwardX11'] = 'yes'
    >>> with open('example.ini', 'w') as configfile:
    ...   config.write(configfile)

更多详细细节请参看python3的官方文档，下面主要就python2的ConfigParser模块作一些说明。

# 配置文件的格式<a id="orgheadline2"></a>

配置文件还可以采用一种冒号分隔的格式，不过推荐就采用等号的格式，如下所示:

    [section1]
    key = value

其中value变成字符串之后两边的空格都会被移除。

# SafeConfigParser类<a id="orgheadline7"></a>

前面谈到新用户推荐就使用SafeConfigParser类来新建一个config对象，如下所示:

    import ConfigParser
    config = ConfigParser.SafeConfigParser()

## 读取一个配置文件<a id="orgheadline3"></a>

如果有现有的配置文件需要读取，则调用config对象的 **read** 方法:

    config.read('test.cfg')

read方法调用完就行了，config对象已经存储了那些值了。

## 获取某个值<a id="orgheadline4"></a>

调用config对象的 **get** 方法，具体格式如下:

    config.get(section, option[, raw[, vars]])

其有两个必填参数，第一个是section的名字，默认的"DEFAULT"也可以这样填上去，然后第二个参数是该section下的某个键或说option。

## 插入或修改某个值<a id="orgheadline5"></a>

调用config对象的 **set** 方法来进行修改某个值的操作，具体格式如下:

    config.set(section, option, value)

其有三个必填参数，第一个是section的名字，默认的"DEFAULT"也可以这样填上去，然后第二个是该section下某个键或说某个option，然后具体该option的值设置为第三个参数。

然后需要注意的是，如果set方法对于的某个section名字原config对象还没有的话，会报错的。你需要先调用 **add\_section** 方法来插入该section，然后才能正常用set设置某个键值。

    config.add_section('Section1')

## 写入配置文件<a id="orgheadline6"></a>

config对象修改好了之后，最后就是写入配置文件中去了。调用 **write** 方法，然后接一个文件对象，如下所示:

    config.write(open("test.cfg","w"))

# 其他额外的一些方法<a id="orgheadline13"></a>

## getint方法<a id="orgheadline8"></a>

    config.getint(section, option)

get方法的补充，从名字看得出来，其返回一个int值。

## getfloat方法<a id="orgheadline9"></a>

    config.getfloat(section, option)

get方法的补充，从名字看得出来，其返回一个float值。

## getboolean方法<a id="orgheadline10"></a>

    config.getboolean(section, option)

get方法的补充，从名字看得出来，其返回一个布尔值。

具体规则是，字符串 "1" ，"true" ， "on" 不分大小写视作 True ； 字符串 "0" ， "false" ， "off" 不分大小写视作 False；其他都视作 ValueError。

## items方法<a id="orgheadline11"></a>

    config.items(section)

把某个section部分看作字典，调用类似字典的items方法，返回键值对列表。

## has\_section<a id="orgheadline12"></a>

判断某个section是否存在，"DEFAULT"不在考虑范围内。

    config.has_section(section)

还有其他一些方法这里就不赘述了，具体请参看 [官方文档](https://docs.python.org/2/library/configparser.html) 。

---

# python3的情况<a id="orgheadline18"></a>

python3之后configparser的使用更加简单了，具体就分为如下几步:

## 新建一个configparser对象<a id="orgheadline14"></a>

    import configparser
    config = configparser.ConfigParser()

## 读取某个config文件<a id="orgheadline15"></a>

调用read方法具体读取某个config文件。

    config.read('test.cfg')

## 如同字典一般操作configparser对象<a id="orgheadline16"></a>

然后接下来就是如同字典一般操作这个configparser对象。其中 'DEFAULT' 是特殊的section，大致如下这样表达:

    config['DEFAULT'] = {'ServerAliveInterval': '45',
                         'Compression': 'yes',
                         'CompressionLevel': '9'}
    config['bitbucket.org'] = {}
    config['bitbucket.org']['User'] = 'hg'
    config['topsecret.server.com'] = {}

## 调用write方法写入<a id="orgheadline17"></a>

    with open('example.ini', 'w') as configfile:
        config.write(configfile)

# 不默认更改大小写<a id="orgheadline19"></a>

具体请参看 [这个网页](http://stackoverflow.com/questions/19359556/configparser-reads-capital-keys-and-make-them-lower-case) ，configparser模块默认吧option name也就是每个section的key name改成小写，我不太喜欢这种风格，因为将configparser刷成字典值时，我们通常认为字典的key大小写是区分的，可以如下改动，然后就不自动进行小写操作了:

```python
self.cfg = configparser.ConfigParser()
self.cfg.optionxform = str## not auto make it lowercase
```