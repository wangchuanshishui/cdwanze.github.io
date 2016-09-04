<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 实时监控某个远程日志文件动态</a></li>
<li><a href="#orgheadline2">2. 制作服务脚本并让其自启动</a></li>
<li><a href="#orgheadline3">3. diff和patch命令</a></li>
</ul>
</div>
</nav>


# 实时监控某个远程日志文件动态<a id="orgheadline1"></a>

参考了 [这个网页](http://serverfault.com/questions/1669/shell-command-to-monitor-changes-in-a-file-whats-it-called-again/1670) 。

    tail -f logfile.log

# 制作服务脚本并让其自启动<a id="orgheadline2"></a>

下面这个服务脚本参考了 [这个网页](http://unix.stackexchange.com/questions/236084/how-do-i-create-a-service-for-a-shell-script-so-i-can-start-and-stop-it-like-a-d) 。

    #!/bin/bash
    
    case "$1" in 
    start)
       /path/to/hit.sh &
       echo $!>/var/run/hit.pid
       ;;
    stop)
       kill `cat /var/run/hit.pid`
       rm /var/run/hit.pid
       ;;
    restart)
       $0 stop
       $0 start
       ;;
    status)
       if [ -e /var/run/hit.pid ]; then
          echo hit.sh is running, pid=`cat /var/run/hit.pid`
       else
          echo hit.sh is NOT running
          exit 1
       fi
       ;;
    *)
       echo "Usage: $0 {start|stop|status|restart}"
    esac
    
    exit 0

一般具体执行的命令推荐放入 /usr/bin 或 /usr/local/bin 里面，当然放在其他地方也是可以的。

然后上面的服务脚本要放入 `/etc/init.d` 里面去。

这个时候就可以通过 `service what start` 来调用服务脚本了。 参考 [这个网页](http://xiaoxia.org/2011/11/15/create-a-simple-linux-daemon/) 。

要让服务脚本自启动，推荐用 `chkconfig` 命令来做。

-   `chkconfig --add what` 添加服务让chkconfig可以管理它。参考 [这个网页](http://imhuchao.com/501.html) 。
-   `chkconfig --del what` 删除服务
-   `chkconfig --level <级别> what on` 设置服务启动级别

启动级别有：

-   等级0表示：表示关机
-   等级1表示：单用户模式
-   等级2表示：无网络连接的多用户命令行模式
-   等级3表示：有网络连接的多用户命令行模式
-   等级4表示：不可用
-   等级5表示：带图形界面的多用户模式
-   等级6表示：重新启动

似乎较常用的级别设置是 `35`

    chkconfig --level 35 what on

# diff和patch命令<a id="orgheadline3"></a>

下面只讨论针对文件的对比。

    diff -u 源文件 目标文件 > test.patch

diff命令得出从源文件到目标文件的修改路径。一般加上 `-u` 来输出patch文件。

patch文件 `---` 表示源文件， `+++` 表示目标文件。

然后应用patch命令可以实现从源文件和patch文件来得到目标文件。

    patch -p0 test2.txt test.patch -o new_test2.txt

这里的 `new_test2.txt` 是test2.txt打上补丁文件之后的结果。

还可以取消补丁，或者说从目标文件得到源文件。

    patch -p0 -R test3.txt test.patch -o ori_test3.txt