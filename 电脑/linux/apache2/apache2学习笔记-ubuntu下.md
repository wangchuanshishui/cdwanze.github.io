<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 简介</a></li>
<li><a href="#orgheadline2">2. a2dissite命令</a></li>
<li><a href="#orgheadline3">3. a2ensite命令</a></li>
<li><a href="#orgheadline4">4. a2dismod命令</a></li>
<li><a href="#orgheadline5">5. a2enmod命令</a></li>
<li><a href="#orgheadline6">6. log文件在那里</a></li>
<li><a href="#orgheadline7">7. 查看当前apache2的一些环境变量</a></li>
<li><a href="#orgheadline8">8. 多站点的玩法</a></li>
<li><a href="#orgheadline9">9. 本地测试用域名支持</a></li>
<li><a href="#orgheadline11">10. 对应到用户的某个文件夹下</a>
<ul>
<li><a href="#orgheadline10">10.1. 文件夹权限</a></li>
</ul>
</li>
<li><a href="#orgheadline12">11. 404重定向</a></li>
<li><a href="#orgheadline17">12. 和flask框架一起</a>
<ul>
<li><a href="#orgheadline13">12.1. 简单的apache2配置</a></li>
<li><a href="#orgheadline14">12.2. Require做了什么</a></li>
<li><a href="#orgheadline15">12.3. what.wsgi文件</a></li>
<li><a href="#orgheadline16">12.4. 更复杂点的配置</a></li>
</ul>
</li>
<li><a href="#orgheadline18">13. apt-get安装软件包清单</a></li>
<li><a href="#orgheadline21">14. 附录</a>
<ul>
<li><a href="#orgheadline19">14.1. ab工具</a></li>
<li><a href="#orgheadline20">14.2. 参考资料</a></li>
</ul>
</li>
</ul>
</div>
</nav>


# 简介<a id="orgheadline1"></a>

关于apache2 web server的简要介绍请参看 [wiki](https://zh.wikipedia.org/wiki/Apache_HTTP_Server) 。目前最广泛使用的apache版本是apache2.4，这是它的 [官方文档链接](http://httpd.apache.org/docs/2.4/) 。不过这个官方文档初看了一下似乎并不是怎么好看。

本文的环境是ubuntu14.04，其他debian系应该都差不多，rpm系可能除了配置文件在 `/etc/http` （还是httpd？） 那里其他应该都是很类似的。在ubuntu下配置文件是放在 `/etc/apache2` 那里的。

我们到了 `/etc/apache2` 那里，可以看到很多配置信息，其中一些配置信息我们一般不会改动，而是通过定制自己的网站配置。比如在 `sites-available` 这个文件夹里面放着一系列可用的网站apache2配置。其中有一个文件 `000-default.conf` ，其在本地对应的是localhost:80，而对外是0.0.0.0:80。这里的0.0.0.0具体是外网IP。假设这台服务器的外网IP是100.100.100.100，那么其他电脑输入100.100.100.100:80即访问了这个000-default网站。

这里需要额外提一下二级域名和三级域名的区别。严格意义上讲"www.someschool.edu"这样的域名是属于三级域名的，而只有"someschool.edu"这样的形式才是二级域名。并且严格意义上讲，二级域名就是对应的具体的某个外网IP，没有其他任何附加行为了。而三级域名则可能存在其他的跳转操作（包括DNS跳转和网络服务器的行为等）。比如"www.someschool.edu"是一个三级域名，而"blog.someschool.edu"也是一个三级域名，其在外网IP的基础上，DNS跳转行为不同的基础上，apache2还可以根据这些域名的不同来选择不同的行为。具体就是通过 **ServerName** 和 **ServerAlias** 来控制的，这样apache2网络服务器是可以支持一台主机管理多个域名站点的。

这里要说的是，在网站上不输入域名，而直接输入某个主机的外网ip地址，那么一般将访问的就是这个 `000-default` 。这个细节很微妙，总之经过我测试结果就是直接输入外网ip访问的就是这个 `000-default` 网站，而如果输入 `www.someschool.edu` ，那么通过DNS，该域名指向的就是那个外网ip，其通过apache2实际上会指向另外一个配置文件。而域名 `someschool.edu` 这样的域名输入就是等同于直接输入外网ip的行为。当然我们可以禁用这个 `000-default` 网站，如下所示:

# a2dissite命令<a id="orgheadline2"></a>

我们运行:

    sudo a2dissite

然后程序会提示你一些可用站点选项，这里输入000-default即将其禁用了。

这样的话输入 `www.someschool.edu` 和 `someschool.edu` 的行为通过 **ServerName** 和 **ServerAlias** 来管理，其行为就完全一样了（通过DNS也是可以做到类似的效果的）。

# a2ensite命令<a id="orgheadline3"></a>

类似的有 `a2ensite` 命令，其用于激活一个网站配置文件。

我们到 `/etc/apache2/sites-available` 那里，执行:

    sudo cp 000-default.conf test.conf

这里简单就使用原来的配置，然后稍做修改:

    DocumentRoot /var/www/test

然后我们还可以继续修改域名控制:

    ServerName www.someschool.edu
    ServerAlias someschool.edu

这个test文件夹也是放在/var/www里面的，文件夹名是随意的。

然后让这个配置文件可用，就是使用a2ensite命令来是这个站点可用的意思:

    sudo a2ensite

选择那个test即可

然后重启一下apache2服务，当然在/var/www下面需要随便放一个index.html文件，这个就不用多说了。

    sudo service apache2 restart

不出意外的话，你在浏览器输入localhost应该能够看到一个简单的页面了吧（这里假设你已经禁用了原000-default网站）。

然后我们可以通过浏览器来输入域名的方式来看一下。但这里要说的是，上面的配置

    ServerAlias someschool.edu

原意是如果遇到这个域名别名也视作同样是这个网站的意思。但对于二级域名来说并不确切。读者可以尝试一下再通过 **a2ensite** 命令将000-default网站启用，然后:

    curl someschool.edu

那么我们会看到这样抓取对应的正是这个000-default网站。

我们再看下面这个例子，很明显抓取baidu.com和抓取www.baidu.com响应是不同的。

    wanze@wanze-ubuntu64:~$ curl baidu.com
    <html>
    <meta http-equiv="refresh" content="0;url=http://www.baidu.com/">
    </html>
    wanze@wanze-ubuntu64:~$ curl www.baidu.com
    <!DOCTYPE html><html><body><script type="text/javascript">var
    ......

# a2dismod命令<a id="orgheadline4"></a>

我之前安装了suphp和suexec模块，还没设置成功，不想放在那里后来对我这里php文件的解析产生影响了，先用a2dismod命令将这两个模块解除了就显示正常了。 **a2dismod** 命令是禁用apache2的某个模块。

# a2enmod命令<a id="orgheadline5"></a>

激活apache2的某个模块。

# log文件在那里<a id="orgheadline6"></a>

在ubuntu下默认的log文件生成路径在 `/var/log/apache2` 那里。

# 查看当前apache2的一些环境变量<a id="orgheadline7"></a>

参考了 [这个网页](http://serverfault.com/questions/558283/apache2-config-variable-is-not-defined) 。

    source /etc/apache2/envvars
    apache2 -V

这些环境变量还看不懂。

# 多站点的玩法<a id="orgheadline8"></a>

apache2管理多站点前面已有所涉及，就是如下通过域名来管理的。

    ServerName www.cdwanze.org

# 本地测试用域名支持<a id="orgheadline9"></a>

我们如下可以修改系统的 `/etc/hosts` 文件来支持本地测试的域名支持:

    127.0.0.1    cdwanze.org
    127.0.0.1    www.cdwanze.org
    127.0.0.1    blog.cdwanze.org

# 对应到用户的某个文件夹下<a id="orgheadline11"></a>

现在我希望把网站对应的文件夹对应到（我在ubuntu下的）主文件夹下的某个文件夹，这样更方便调试。于是修改了前面的 `DocumentRoot` 参数，重启apache2服务之后，报错说“/没有权限访问”，

其报了这个错误:

    403 Forbidden You don't have permission to access / on this server

然后参考了 [这个网页](http://stackoverflow.com/questions/10873295/error-message-forbidden-you-dont-have-permission-to-access-on-this-server) ，进行如下设置即可:

    <Directory /home/wanze/workspace/cdwanze.org >
    Require all granted
    </Directory>

这里的:

    Require all granted

这种写法只适用于apache2.4或以上版本，不过我想（新用户）现在应该都是用的apache2.4或者以上版本了吧。看上去是给予全部权限的意思。

## 文件夹权限<a id="orgheadline10"></a>

实际上上面的说没有权限访问/的错误还可能是你本地文件夹或者文件的权限设置问题<sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup>。

一般网站不含可执行文件的推荐设置为644权限:

    sudo chmod -R 644 filefolder_name

644权限是 `-rw-r--r--` ，也就是只有文件所有者才可读可写，其他的都只有读权限，这是一种很安全的权限模式，基本上不用太担心出什么问题。

若该文件夹需要支持python脚本或者php等可执行脚本，那么常用的权限是755，也就是 `-rwxr-xr-x` ，即文件所有者可读可写可执行，群组所有或者其他人可读可执行。设置755权限可能会有点危险，需要进一步用apache2的其他模块，比如suPHP或者wsgi模块的群组用户权限管理来控制。

# 404重定向<a id="orgheadline12"></a>

推荐在网站文件夹本地建立一个 `.htaccess` 文件来管理，参考了 [这个网](http://www.jb51.net/article/25476.htm)页 。

首先你需要在该网站的apache2配置那里加上这么一行:

    <Directory /home/wanze/workspace/cdwanze.org >
    AllowOverride All
    </Directory>

这里是允许所有重定向的意思。

然后在 `.htaccess` 文件里面加上

    ErrorDocument 404 /404.html

也就是如果发生 **404** 错误，则返回 /404.html 这个网页文件。具体在你的网站文件夹目录下面新建一个404.html文件即可。

当然了如果你是用的flask框架编写网络服务器，那么其是可以做错误和其他重定向任务的，就不需要这样配置了。这里主要是针对那些php语言编写的网络服务器（apache2是本来就支持解析php文件的，但我不确定用flask框架之下是否还支持解析php文件，但也不关心，没谁这么用吧、、）。

# 和flask框架一起<a id="orgheadline17"></a>

apache2是支持flask框架编写网络服务器的，更确切的表达是，apache2有一个模块，安装上它apache2就支持wsgi接口了。对于python2，在ubuntu下要安装的是:

```bash
sudo apt-get install  libapache2-mod-wsgi
```

对于python3，要安装的是:

```bash
sudo apt-get install  libapache2-mod-wsgi-py3
```

默认那个 `wsgi` 模块安装之后就激活了，你可以通过 `a2dismod` 来看一下，就是那个 `wsgi` 模块。 这里参考了 [这个网页](http://stackoverflow.com/questions/28019310/running-django-python-3-4-on-mod-wsgi-with-apache2) 。

但是等一等，还有一些东西你需要配置，更多细节请参看flask框架官方文档的 [这里](http://flask.pocoo.org/docs/0.10/deploying/mod_wsgi/) ，下面简单介绍之。

## 简单的apache2配置<a id="orgheadline13"></a>

最简单的配置就是如下所示:

    WSGIScriptAlias / /home/wanze/workspace/cdwanze/cdwanze.wsgi
    
        <Directory /home/wanze/workspace/cdwanze >
        Require all granted
        </Directory>

## Require做了什么<a id="orgheadline14"></a>

其中 `Require all granted` 前面我们已谈到，是对访问权限的控制。参看apache2.2到apache2.4的 [升级文档](http://httpd.apache.org/docs/current/upgrading.html) ，
原2.2配置:

    Order deny,allow
    Deny from all

等同于2.4配置:

    Require all denied

原2.2配置:

    Order allow,deny
    Allow from all

等同于2.4配置:

    Require all granted

原2.2配置:

    Order Deny,Allow
    Deny from all
    Allow from example.org

等同于2.4配置:

    Require host example.org

关于这里Order什么的配置更详细的说明参看 [这个网页](http://www.fwolf.com/blog/post/191) 。其第一行就两种写法，逗号之间不能有空格。

1.  `Order Deny,Allow`

在这个写法后面，后面先写允许谁谁谁访问，然后写禁止谁谁谁访问。如下所示:

    Order Deny,Allow
    Deny from all
    Allow from example.org

这个写法的意思是禁止谁，允许谁，禁止所有只允许example.org访问。

1.  `Order Allow,Deny`

和上面描述类似，除了先写允许再写禁止。

新的apache2.4的 `require` 语法更多细节请参看apache2官方文档的 [这里](http://httpd.apache.org/docs/2.4/howto/access.html) 。接着前面的描述，还有如下表达:

允许某个具体的ip地址:

    Require ip ip.address

在前面有了，全部都允许、全部都禁止、全部都禁止只允许谁。还有如下，全部都允许只禁止谁:
不允许某个ip地址。

    Require all granted
    Require not ip 10.252.46.165

## what.wsgi文件<a id="orgheadline15"></a>

这一行具体设置那个what.wsgi文件在那里，一般就放在flask框架源码第一目录下吧。

    WSGIScriptAlias / /home/wanze/workspace/cdwanze/cdwanze.wsgi

然后这个what.wsig文件主要就是说明flask程序app对象在哪里。

这里首先把python的搜索路径加上，然后从你的flask主app对象所谓的文件中引入app，然后 `as application` 。

    import sys
    sys.path.insert(0, '/home/wanze/workspace/cdwanze')
    
    from cdwanze import app as application

## 更复杂点的配置<a id="orgheadline16"></a>

flask官方文档给出了更复杂点的配置如下所示:

    WSGIDaemonProcess cdwanze user=wanze group=wanze threads=5
    WSGIScriptAlias / /home/wanze/workspace/cdwanze/cdwanze.wsgi
    
        <Directory /home/wanze/workspace/cdwanze >
        WSGIProcessGroup cdwanze
        WSGIApplicationGroup %{GLOBAL}
    
        Require all granted
        </Directory>

具体其似乎和用户权限管理有关，这里的细节我还不太懂，不过大体就是用户和群组的控制吧，然后还有一个线程控制。这里暂时先就这样了。

# apt-get安装软件包清单<a id="orgheadline18"></a>

下面是一些在ubuntu下可以通过apt-get安装的软件包清单信息，你可能用得着的。

在ubuntu下安装所谓的LAMP套件是很简单了，实际上用apt-get直接安装也看不出来比用那个套件安装方法复杂多少。

    sudo apt-get install tasksel
    sudo tasksel install lamp-server

下面是我收集的相关软件安装包信息，主要参考了 [这个网页](http://bbs.aliyun.com/read/135940.html) 。当然通常所谓的LAMP套件不需要安装这么多东西，最简单的就是mysql-server，mysql-client，php5，apache2。然后后面这些软件包后面你可能会用到的。

-   **mysql-server:** Mysql服务器核心程序，服务器端主程序。
-   **mysql-client:** Mysql客户端，用以通过命令行方式登录管理Mysql服务器。
-   **mysql-common:** Mysql核心库文件，包含了运行Mysql必备的基本文件。
-   **php5:** 服务器端PHP解释器
-   **php5-cgi:** 服务器端PHP-CGI解释器
-   **php5-cli:** PHP5命令行工具
-   **php5-common:** PHP5一些基本文件
-   **php5-fpm:** 服务器端PHP-FPM程序 这个程序对Nginx处理PHP很重要
-   **php5-gd:** PHP5的GD模块 GD是一套开源图像处理库，一般dz生成缩略图或者加水印需要他
-   **php5-imagick:** PHP5的ImageMagick模块 DZ支持调用其用以提供比GD跟快以及更高效的图像处理
-   **php5-imap:** PHP5的IMAP模块 论坛的邮件发送功能可能需要
-   **php5-ldap:** PHP5的LDAP模块 LDAP是一个轻量级目录服务
-   **php5-mcrypt:** PHP5的MCrypt模块 主要用途是数据加密，比如phpmyadmin就会要求提供此模块来提供更高的安全性
-   **php5-mysql:** PHP5的MySQL模块 如果想让你的网站可以访问数据库，此模块必备
-   **php5-snmp:** PHP5的SNMP模块
-   **php5-sqlite:** PHP5的SQLite模块 SQLite是一个轻量级的数据库，某些软件可能需要
-   **php5-xmlrpc:** PHP5的XML-RPC
-   **apache2:** Apache元包（metapackage不会翻译的飘过）
-   **apache2-mpm-prefork:** AApache传统无线程模型
-   **apache2-utils:** Web服务器实用工具
-   **apache2.2-bin:** Apache公用二进制文件
-   **apache2.2-common:** Apache公用文件
-   **libapache2-mod-php5:** 服务器端，HTML嵌入式脚本语言（Apache模块）

下面继续列出一些相关软件包信息:

-   php5-curl
-   php5-json

# 附录<a id="orgheadline21"></a>

## ab工具<a id="orgheadline19"></a>

apache2的ab工具方便实际测试网页服务器在应对多个请求下的性能。

简单的使用就是:

    ab -n 1000 -c 4 http://localhost:8888/

假设你开了一个本地服务器端口8888，这里 `-n` 的意思是多少个请求， `-c` 的意思是多少个并发，也就是同时有多少个请求。更多细节请参看 [这里](https://httpd.apache.org/docs/2.4/programs/ab.html) 。

## 参考资料<a id="orgheadline20"></a>

1.  [PHP完全中文手册](http://php.freehostingguru.com/)
2.  [PHP手册](http://php.net/manual/zh/)
3.  哈佛大学的 [构建动态网页视频教程](http://open.163.com/special/opencourse/buildingdynamicwebsites.html)
4.  [关于a2ensite和a2dissite的讨论](http://blog.csdn.net/hfahe/article/details/5490223)

<div id="footnotes">
<h2 class="footnotes">Footnotes: </h2>
<div id="text-footnotes">

<div class="footdef"><sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> <div class="footpara">参考了 [这个网页](https://wiki.apache.org/httpd/13PermissionDenied) 。</div></div>


</div>
</div>