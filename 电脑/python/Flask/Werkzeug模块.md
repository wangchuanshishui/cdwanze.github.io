<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 安装</a></li>
<li><a href="#orgheadline4">2. 什么是WSGI</a>
<ul>
<li><a href="#orgheadline2">2.1. 通用网关接口</a></li>
<li><a href="#orgheadline3">2.2. web服务器网关接口</a></li>
</ul>
</li>
<li><a href="#orgheadline10">3. PEP333</a>
<ul>
<li><a href="#orgheadline5">3.1. 规范总览</a></li>
<li><a href="#orgheadline6">3.2. 应用程序这边</a></li>
<li><a href="#orgheadline7">3.3. 服务器这边</a></li>
<li><a href="#orgheadline8">3.4. 中间层</a></li>
<li><a href="#orgheadline9">3.5. 规范细节</a></li>
</ul>
</li>
<li><a href="#orgheadline15">4. werkzeug模块详解</a>
<ul>
<li><a href="#orgheadline11">4.1. create_environ函数</a></li>
<li><a href="#orgheadline12">4.2. Request对象</a></li>
<li><a href="#orgheadline13">4.3. Response对象</a></li>
<li><a href="#orgheadline14">4.4. run_simple函数</a></li>
</ul>
</li>
</ul>
</div>
</nav>


# 安装<a id="orgheadline1"></a>

推荐使用pip命令安装之。

```sh
pip install werkzeug
```

# 什么是WSGI<a id="orgheadline4"></a>

## 通用网关接口<a id="orgheadline2"></a>

通用网关接口(CGI, Common Gateway Interface)，【这里翻译自wiki】是一种老旧的技术了，几乎被所有的网络服务器支持。使用CGI的程序和网络服务器交流，服务器对于每次请求都要其中一次程序。而每一次请求都要启动一个新的python解释器——这需要花费一定的时间——这使得整个接口只能使用在低负荷的情况。

CGI的优点就是简单，写个使用CGI技术的python脚本只是三四行代码的事。但是这种简单是有代价的，CGI并没很好地帮助开发人员进行开发。

写一个CGI程序，现在也是可行的，只是不推荐这样做了。现在有 WSGI 了。

## web服务器网关接口<a id="orgheadline3"></a>

web服务器网关接口(WSGI, Web Server Gateway Interface)， 是网络服务器和网络应用程序（或者框架）之间一个简单通用的接口规范。其他有些语言后来也出现了类似的规范，但一般谈论WSGI主要是指python语言的。其最早由 Phillip J. Eby 写在 PEP 333 上（2003年11月）。后来被接受为python网络应用程序开发的一个标准。最新的标准版本号是v1.0.1，也就是PEP 3333（写于2010年9月）。

# PEP333<a id="orgheadline10"></a>

目前最新的是PEP 3333 ，其增加了很多新特性并支持python3，还是先从PEP333看起吧。

PEP333一开始谈到python里面服务器的框架很多，因此最好提出一个简单的网络服务器和网络应用程序或框架之间的通用接口，也就是所谓的 (the Python Web Server Gateway Interface **WSGI** )，这就是本PEP的目的。

## 规范总览<a id="orgheadline5"></a>

WSGI 接口分为两个部分: 一是服务器或网关；二是应用程序或框架。服务器那边引用一个可调用对象，是从应用程序那边传过来的。这个可调用对象具体该如何传过来取决于服务器那边。假定一些服务器或网关需要应用程序的部署者去写一个简短的脚本来创建一个服务器或网关的实例，然后给它提供一些应用程序对象。其他的服务器或网关则使用配置文件或者其他机制来指定应用程序应该从那里引入或者获取这些应用程序对象，

作为纯服务器/应用程序的补充，还可能创建一个中间层(middleware)，它实现了两边的规范。这样的组件对于服务器来说就好像一个应用程序一样行动；对于应用程序来说好像一个服务器。可作为扩展API，内容传输，导航或者其他有用的功能。

本文档中所谓的可调用(callable)是指函数，方法以及类或者实例有 `__call__` 方法。可调用对象就是指自身可调用，不需要向上回溯了。

## 应用程序这边<a id="orgheadline6"></a>

应用程序对象应该是可调用的，下面两个例子，一个是函数，一个是类。

```python
def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n']


class AppClass:
    """Produce the same output, but using a class

    (Note: 'AppClass' is the "application" here, so calling it
    returns an instance of 'AppClass', which is then the iterable
    return value of the "application callable" as required by
    the spec.

    If we wanted to use *instances* of 'AppClass' as application
    objects instead, we would have to implement a '__call__'
    method, which would be invoked to execute the application,
    and we would need to create an instance for use by the
    server or gateway.
    """

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Hello world!\n"
```

## 服务器这边<a id="orgheadline7"></a>

服务器接受HTTP client 发送过来的协议一次就运行一次前面讲到的应用程序可调用对象。

```python
import os, sys

def run_with_cgi(application):

    environ = dict(os.environ.items())
    environ['wsgi.input']        = sys.stdin
    environ['wsgi.errors']       = sys.stderr
    environ['wsgi.version']      = (1, 0)
    environ['wsgi.multithread']  = False
    environ['wsgi.multiprocess'] = True
    environ['wsgi.run_once']     = True

    if environ.get('HTTPS', 'off') in ('on', '1'):
        environ['wsgi.url_scheme'] = 'https'
    else:
        environ['wsgi.url_scheme'] = 'http'

    headers_set = []
    headers_sent = []

    def write(data):
        if not headers_set:
             raise AssertionError("write() before start_response()")

        elif not headers_sent:
             # Before the first output, send the stored headers
             status, response_headers = headers_sent[:] = headers_set
             sys.stdout.write('Status: %s\r\n' % status)
             for header in response_headers:
                 sys.stdout.write('%s: %s\r\n' % header)
             sys.stdout.write('\r\n')

        sys.stdout.write(data)
        sys.stdout.flush()

    def start_response(status, response_headers, exc_info=None):
        if exc_info:
            try:
                if headers_sent:
                    # Re-raise original exception if headers sent
                    raise exc_info[0], exc_info[1], exc_info[2]
            finally:
                exc_info = None     # avoid dangling circular ref
        elif headers_set:
            raise AssertionError("Headers already set!")

        headers_set[:] = [status, response_headers]
        return write

    result = application(environ, start_response)
    try:
        for data in result:
            if data:    # don't send headers until body appears
                write(data)
        if not headers_sent:
            write('')   # send headers now if body was empty
    finally:
        if hasattr(result, 'close'):
            result.close()
```

## 中间层<a id="orgheadline8"></a>

## 规范细节<a id="orgheadline9"></a>

应用程序对象将接受两个参数，一个是 `environ` ，一个是 `start_response` 。服务器那边会如此调用的，比如: `application(environ, start_response)` 。

environ 是一个字典值，包含着CGI风格的环境变量。这个environ一定要是python内置的字典类型，而不是用于自己定义的衍生字典类型。这个字典值应该允许被应用程序随意修改，其也应该包含WSGI要求的一些变量等等。

start\_response 是一个可调用对象，接受两个参数和一个可选参数。一个是status，一个是response\_headers，一个是exec\_info。应用程序必须运行这个可调用对象，如下所示: start\_response(status, response\_headers) 

status是用来描述状态信息的字符串，response\_headers是一个列表，列表里装着(header\_name, header\_value)这样的值用来描述HTTP响应头信息。可选参数exec\_info定义了start\_response遇到错误该如何做。

start\_response 应该返回write(body\_data) ，这个write函数接受一个字符串可选参数body\_data，即将要写入HTTP响应体的内容。

# werkzeug模块详解<a id="orgheadline15"></a>

## create\_environ函数<a id="orgheadline11"></a>

    from werkzeug.test import create_environ
    
    environ = create_environ('/test','http://localhost:8080')

创建一个environ字典值。里面有很多其他信息已经补充进去了。

## Request对象<a id="orgheadline12"></a>

    from werkzeug.test import create_environ
    
    environ = create_environ('/test','http://localhost:8080')
    
    from werkzeug.wrappers import Request
    
    request = Request(environ)

## Response对象<a id="orgheadline13"></a>

    from werkzeug.wrappers import Response
    
    def application(environ, start_response):
        response = Response('hello world!')
        return response(environ,start_response)

## run\_simple函数<a id="orgheadline14"></a>

建立一个简单的服务器

    from werkzeug.serving import run_simple
    run_simple('localhost',8080,application, use_reloader=True)

这里在本地运行一个简单的服务器，监听端口8080，注意是数字。然后是运行的应用程序是前面简单写的application函数，就是所谓的可调用应用程序对象，然后 `use_reloader=True` 的意思是如果模块发生变动，则重新启动服务器。