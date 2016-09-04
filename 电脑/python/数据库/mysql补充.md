<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 备份和还原</a></li>
</ul>
</div>
</nav>


# 备份和还原<a id="orgheadline1"></a>

mysql的备份操作就是使用 `mysqldump` 命令，其将生成一个sql文件，然后还原实际上就是加载这个sql文件即可。还原过程如下所示:

    mysql -u root test < test.sql

下面主要说下 `mysqldump` 命令

    mysqldump -u user -h 127.0.0.1 -P 8888 -v -p test > test.sql

-   **`-u`:** 设置登录用户名
-   **`-h`:** 要连接的数据库服务器地址
-   **`-P`:** 要连接的数据库服务器端口
-   **`-v`:** 显示聒噪信息
-   **`-p`:** 和mysql命令类似，等下输入密码

其后必填参数是你想要dump的某个database名字。

本小节参考了 [这个网页](http://www.thegeekstuff.com/2008/09/backup-and-restore-mysql-database-using-mysqldump/) 。