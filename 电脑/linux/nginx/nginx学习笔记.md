<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline2">1. 前言</a>
<ul>
<li><a href="#orgheadline1">1.1. 安装</a></li>
</ul>
</li>
<li><a href="#orgheadline6">2. nginx配置基础</a>
<ul>
<li><a href="#orgheadline3">2.1. 通用配置</a></li>
<li><a href="#orgheadline4">2.2. http部分配置</a></li>
<li><a href="#orgheadline5">2.3. server部分配置</a></li>
</ul>
</li>
<li><a href="#orgheadline10">3. 附录</a>
<ul>
<li><a href="#orgheadline7">3.1. nginx分配请求逻辑</a></li>
<li><a href="#orgheadline8">3.2. 403没有权限访问错误</a></li>
<li><a href="#orgheadline9">3.3. 参考资料</a></li>
</ul>
</li>
</ul>
</div>
</nav>


# 前言<a id="orgheadline2"></a>

nginx的官方文档在 [这里](http://nginx.org/en/docs/) ，有问题主要还是参看官方文档吧。

## 安装<a id="orgheadline1"></a>

debian系安装:

    sudo apt-get install nginx

rpm系统安装:

    sudo yum install nginx

# nginx配置基础<a id="orgheadline6"></a>

nginx的配置就是在 `/etc/nginx/sites-available` 那里新建一个配置文件，然后这样创建一个符号链接到 `sites-enabled` 那里。

    sudo ln -s /etc/nginx/sites-available/cdwanze.work /etc/nginx/sites-enabled/cdwanze.work

然后重启nginx即可。 

    sudo service nginx restart

nginx配置文件的基本格式是:

    <section> {
        <directive>  <parameters>;
    }

## 通用配置<a id="orgheadline3"></a>

这里的所谓通用的配置也就是所谓的 global section ，这些配置将影响整个server，我们常在 `nginx.conf` 中看到这些配置。

-   **user:** 当前工作进程下的user用户名。比如一般推荐 `nginx.conf` 中如下设置:

    # Run as a unique, less privileged user for security reasons.
    user www www;

也就是以用户名 `www` 来运行网站（大概是这个意思吧），为了不出错你需要确保服务器系统里有用户 www ，没有简单运行:

    useradd www

即可。

-   **worker\_processes:** 工作进程数设置，在 [这个项目](https://github.com/h5bp/server-configs-nginx) 中的推荐设置如下:

    # Sets the worker threads to the number of CPU cores available in the system for best performance.
    # Should be > the number of CPU cores.
    # Maximum number of connections = worker_processes * worker_connections
    worker_processes auto;

-   **error\_log:** 控制错误日志输出路径

    # Log errors and warnings to this file
    # This is only used when you don't override it on a server{} level
    error_log  logs/error.log warn;

第二个参数是控制输出级别，有: debug, info, notice, warn, error, crit, alert, and emerg 。

-   **pid:** 存储主进程的id信息的文件路径

    # The file storing the process ID of the main process
    pid        /var/run/nginx.pid;

## http部分配置<a id="orgheadline4"></a>

http部分也就是所谓的 `http` section部分配置，其是基于http module。http section部分后面有这么一句:

      include sites-enabled/*;
    }

然后我们后面会看到这么一句，那就是server section部分应该放入http section部分中。常常有些需求最后要到这里来配置。比如说 `client_max_body_size` ，如果你遇到nginx请求实体过大错误信息:

    Nginx 413 Request Entity Too Large

参考了 [这个网页](http://www.cyberciti.biz/faq/linux-unix-bsd-nginx-413-request-entity-too-large/) ，你需要在http section里面如下配置:

    # set client body size to 2M #
    client_max_body_size 2M;

-   **chunked\_transfer\_encoding:** 

这部分后面慢慢熟悉。

## server部分配置<a id="orgheadline5"></a>

server section部分在 `sites-available` 是配置的重点。

-   **linsten:** 设置虚拟server的监听端口:

    listen 80;

-   **server\_name:** 

    server {
        listen 80;
        return 444;
    }

这个虚拟服务器没有设置 `server_name` ，意思是如果进来的HTTP请求请求头没有 `HOST` 这一行，则将由该虚拟服务器处理。这里就是简单的返回444状态码。

我们在来看这个server配置:

    server {
      # don't forget to tell on which port this server listens
      listen [::]:80;
      listen 80;
    
      # listen on the www host
      server_name www.cdwanze.work;
    
      # and redirect to the non-www host (declared below)
      return 301 $scheme://cdwanze.work$request_uri;
    }

显示监听80端口，现在 `listen [::]:80;` 这个我还看不懂。然后server\_name的简单意思就是遇到 HOST 是 `www.cdwanze.work` 的请求都重定向为 `cdwanze.work/....` 的url请求。

server\_name 支持正则表达和通配符表达，正则表达暂时不讨论吧，通配符表达比如:

    *.example.com
    www.example.*
    .example.com # match *.example.com 和 example.com

-   **location:** location在server section里面，也是很关键的一个配置点。

    location / {
        proxy_pass http://127.0.0.1:5000;
    }

就是描述了在遇到 `/` 的时候如何处理。

-   proxy\_pass

代理传递，也就是比如说python的flask框架在后台端口5000运行， `/` 这样的请求将传递给flask的app来处理。这里值得提醒的是location的uri分发规则较为复杂，目前我们需要知道的是， `/` 是一个通用匹配，就是如果是精确匹配，当然就选这个规则，如果有其他规则匹配，则用其他规则，否则最后就考虑使用这个通用规则。更多信息请参看 [这个网页](http://seanlook.com/2015/05/17/nginx-location-rewrite/) 。

这种反向代理，一个很重要的知识点就是uri的改写规则。这里面东西也很多，比如下面的这个:

    location /socket.io {
        proxy_pass http://127.0.0.1:5000/socket.io;
    }

匹配到的部分会被改写为 `http://127.0.0.1:5000/socket.io` 但是也有些例外的情况，以后再详细讨论之。

-   proxy\_set\_header

比如websocket协议部分的转发，需要对header做如下一些修改:

    proxy_http_version 1.1;    
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";

具体就是送入upstream 服务器的header加上这两行:

    Upgrade: websocket
    Connection: Upgrade

这里所谓的upstream服务器，在nginx实际上就可以简单看作一个汇总性质的服务器，因为我们前面看到了nginx下面有很多虚拟的server，那么这个upstream可以看作最终面向客户端的那个服务器。初步的理解就是这么个意思。

# 附录<a id="orgheadline10"></a>

## nginx分配请求逻辑<a id="orgheadline7"></a>

这部分内容很关键，慢慢看下吧。

1.  根据请求的ip和端口号来核对 `listen` 信息。
2.  根据请求Host字段来核对 `server_name` 信息。
    -   核对由继续分为通配符前核对
    -   通配符后核对
    -   正则核对

3.  以上listen和server\_name的核对最后若没有匹配最后都会回滚到默认的配置中。

4.  以上核对若匹配则进一步根据相应的配置来进行请求处理。

## 403没有权限访问错误<a id="orgheadline8"></a>

我需要在本用户的主文件夹下的随便某个文件夹来写一些网页，然后nginx的server的 `root` 配置好后可能会出现 403错误，这很有可能是你 `nginx.conf` 文件的 `user` 配置，没有设置为本用户，所以才无权限操作。ubuntu下那个user好像默认的是var-www这个。将其改为你的用户名即可。参看了 [这个网页](http://zoroeye.iteye.com/blog/2166174) 。

## 参考资料<a id="orgheadline9"></a>

1.  mastering nginx