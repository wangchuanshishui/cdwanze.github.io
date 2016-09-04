<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 安装</a></li>
<li><a href="#orgheadline2">2. 配置</a></li>
<li><a href="#orgheadline3">3. 启动进程</a></li>
<li><a href="#orgheadline4">4. 停止进程</a></li>
</ul>
</div>
</nav>


# 安装<a id="orgheadline1"></a>

    apt-get install supervisor

# 配置<a id="orgheadline2"></a>

在 `/etc/supervisor/conf.d/` 下新建一些conf文件，内容如下:

    [program:app]
    command=/usr/bin/gunicorn -w 1 wsgiapp:application
    directory=/srv/www
    user=www-data

# 启动进程<a id="orgheadline3"></a>

    supervisorctl start app

# 停止进程<a id="orgheadline4"></a>

    supervisorctl stop app