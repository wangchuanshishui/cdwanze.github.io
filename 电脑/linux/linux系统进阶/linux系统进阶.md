<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline5">1. ssh命令</a>
<ul>
<li><a href="#orgheadline1">1.1. ssh远程登录</a></li>
<li><a href="#orgheadline2">1.2. ssh连接远程虚拟机(ubuntu系统)然后调用mongo时报错</a></li>
<li><a href="#orgheadline3">1.3. ssh连接进行某个长时间的任务</a></li>
<li><a href="#orgheadline4">1.4. 实现ssh跳转</a></li>
</ul>
</li>
<li><a href="#orgheadline6">2. sftp命令</a></li>
<li><a href="#orgheadline7">3. scp命令</a></li>
<li><a href="#orgheadline8">4. ln命令</a></li>
<li><a href="#orgheadline9">5. cron后台服务</a></li>
<li><a href="#orgheadline10">6. flock命令</a></li>
<li><a href="#orgheadline12">7. wc命令</a>
<ul>
<li><a href="#orgheadline11">7.1. 统计行数</a></li>
</ul>
</li>
<li><a href="#orgheadline13">8. lsof命令</a></li>
<li><a href="#orgheadline14">9. 终端开启代理</a></li>
<li><a href="#orgheadline16">10. netcat命令</a>
<ul>
<li><a href="#orgheadline15">10.1. 侦测开放端口</a></li>
</ul>
</li>
<li><a href="#orgheadline20">11. curl命令</a>
<ul>
<li><a href="#orgheadline17">11.1. 指定user-agent</a></li>
<li><a href="#orgheadline18">11.2. 设置cookie</a></li>
<li><a href="#orgheadline19">11.3. 查看本机的外网ip</a></li>
</ul>
</li>
<li><a href="#orgheadline27">12. linux系统用户管理</a>
<ul>
<li><a href="#orgheadline21">12.1. 新建用户</a></li>
<li><a href="#orgheadline22">12.2. 删除用户</a></li>
<li><a href="#orgheadline23">12.3. 修改用户密码</a></li>
<li><a href="#orgheadline24">12.4. 用户其他参数修改</a></li>
<li><a href="#orgheadline25">12.5. 以某用户身份登录</a></li>
<li><a href="#orgheadline26">12.6. 让某个用户是sudoer</a></li>
</ul>
</li>
<li><a href="#orgheadline30">13. nmap命令</a>
<ul>
<li><a href="#orgheadline28">13.1. 扫描整个子网</a></li>
<li><a href="#orgheadline29">13.2. 指定扫描端口</a></li>
</ul>
</li>
<li><a href="#orgheadline31">14. ifconfig命令</a></li>
<li><a href="#orgheadline32">15. date命令</a></li>
<li><a href="#orgheadline33">16. 参考资料</a></li>
</ul>
</div>
</nav>


# ssh命令<a id="orgheadline5"></a>

## ssh远程登录<a id="orgheadline1"></a>

SSH协议用于计算机之间的加密远程登录。本小节主要参考了阮一峰的 [这篇日志](http://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html) 。

ubuntu下似乎都自带 `ssh` 命令了，windows下一般使用 `PuTTY` 这个软件。

ssh登录命令格式如下:

    ssh username@host

其中ssh默认的端口号是22，你可以通过 `-p` 来指定其他端口号。这里的username是远程计算机的用户名，这里的host是ip地址包括局域网的192.168&#x2026;之类的。

具体第一次用ssh命令登录会提示你输入密码，这个密码不是远程计算机的登录密码，而是连接密码。可以不设置。如果设置了对于终端登录似乎影响不大，后面设置公钥登录之后仍会不需要输入密码就会登录了，但如果通过python的paramiko模块进行ssh登录，那么还需要一些额外的配置，这块这里先略过，在python的paramiko模块那里做进一步的讨论。

默认情况下ssh登录远程终端是需要输入远程计算机的密码的，你也可以通过一种将自己的公钥上传到远程计算机的方法来实现不用输入密码来登录之。首先你需要生成自己的公钥:

    ssh-keygen

具体生成的公钥文件文件在 `$HOME/.ssh` 那里，其为 `id_rsa.pub` ，还有一个 `id_rsa` 是什么私钥文件。然后将公钥文件上传上去即可:

    ssh-copy-id username@host

## ssh连接远程虚拟机(ubuntu系统)然后调用mongo时报错<a id="orgheadline2"></a>

ssh连接远程虚拟机(ubuntu系统)然后调用mongo时报错，具体错误信息如下所示:

    Failed global initialization: BadValue Invalid or no user locale set. Please ensure LANG and/or LC_* environment variables are set correctly

这个问题很简单，就是语言没设置好，解决方案参见 [这个网页](http://askubuntu.com/questions/536875/error-in-installing-mongo-in-virtual-machine) 。具体就是在当前终端输入:

    export LC_ALL=en_US.UTF-8

即可。最好把这行命令放在主文件夹的 `.bashrc` 文件那里。

## ssh连接进行某个长时间的任务<a id="orgheadline3"></a>

ssh连接远程主机，然后要执行某个长时间的命令任务，如果你有一段时间没去管那个终端窗口了，ssh连接就可能会自动中断，终端之后远程的相关进程也会被kill掉。这是会返回什么 `Broken pipe` 错误。

一个简单的解决方案是在远程主机上执行某个命令，然后这个命令前面加上 `nohup` 这个命令，类似下面这种格式:

    nohup thecommand

更好地解决方案是在远程安装（ubuntu下用apt-get安装之） `screen` 这个小工具，然后在远程通过screen命令来开启一个执行某个shell命令的全屏窗口（这样其就不会被自动关闭了），哪怕你本地的那个终端窗口关闭了，远程主机相关进程还是会在那里运行的。screen命令常见的用法有:

-   **screen -S name:** 创建一个screen进程，并给他取个名字，后面的screen进程可以直接使用这个名字。
-   **screen -ls:** 看看当前电脑里面都有那些screen进程。
-   **screen -r thename\_or\_thepid:** 重连某个screen进程，默认只能连Detached（失连）的进程。
-   **screen -wipe:** 清除某些Dead的screen进程。
-   **screen -D -r:** 有的时候某个screen进程可能已经断开连接了，但其还是显示的Attached，可以用这样的选项组合来强制某个screen进程失连，然后再重连。

更多细节请参看 [这个网页](http://www.ibm.com/developerworks/cn/linux/l-cn-screen/) 。

## 实现ssh跳转<a id="orgheadline4"></a>

语法如下:

    ssh -t root@100.100.100.100 ssh root@192.168.0.100

这将先对外网ip100.100.100.100（随便捏造的）进行ssh登录，然后再通过那台远程主机跳转到他们局域网的192.168.0.100那台机器上。这里的两个ssh命令都可以跟上其他一些参数，比如-p来控制端口等。

# sftp命令<a id="orgheadline6"></a>

ftp协议(File Transfer Protocol, 文件传输协议)是用于在网络上进行文件传输的一套标准协议。sftp命令是基于ssh命令来进行上传和下载文件的。本小节参考了 [这个网页](http://codingstandards.iteye.com/blog/985744) 。

sftp命令的使用有点类似于ssh命令:

    sftp root@100.100.100.100

这样就将试图连接那个远程主机，sftp的可选参数和ssh命令的可选参数有一些类似，但又有所不同。比如端口设置选项是大写字母P `-P` 。进入sftp>提示符之后，有一些命令可以用，其中最重要的两个命令是: `put` ， `get` 。

put是上传文件，get是下载文件。如果在顶层python程序中，指定好文件名，是不需要了解其他的命令的。不过下面这些命令读者可以稍微了解一下，比如pwd，查看远程服务器当前目录，cd，更远远程服务器目录，ls，mkdir等。然后类似的还有lpwd，查看本地系统当前目录，lcd更换本地当前目录和lls，lmkdir等。

# scp命令<a id="orgheadline7"></a>

一般还是优先使用sftp命令来在远程主机上进行拷贝或上传文件操作，但如果远程主机没开ftp服务，那么就不能使用sftp命令了。这是你可以使用scp命令来实现这些功能。本小节参考了 [这个网页](http://coolnull.com/1264.html) 。

从名字看得出来scp命令可以理解为基于ssh命令的cp命令。在使用方法上也类似，除了文件或文件夹路径前加上了ssh标识，如下所示:

    scp test.txt root@100.100.100.100:~

如上所示，如果是本地路径，则可以不加":"冒号前面那串。然后最常用的选项有:

-   **-r:** 递归复制整个目录
-   **-P:** 控制端口号
-   **-p:** 保留原文件的修改时间，访问时间和访问权限

# ln命令<a id="orgheadline8"></a>

本小节参考了 [这个网页](http://kingplesk.org/2011/06/linux-ln-%E7%AC%A6%E5%8F%B7%E8%BF%9E%E6%8E%A5%E7%9A%84%E5%B1%82%E6%95%B0%E8%BF%87%E5%A4%9A/) 。

具体例子如下所示:

    sudo ln -s ~/工作空间/liteide/bin/liteide /usr/local/bin/liteide

默认是硬连接，如果加上-s则是符号连接。一般使用符号连接吧。然后注意符号连接都要使用绝对路径表示，否则会返回符号连接层数过多错误。

# cron后台服务<a id="orgheadline9"></a>

有的ubuntu下可能还没有安装cron后台服务，通过

    sudo apt-get install cron

安装之。

cron的后台服务程序，可以用来让系统执行一些计划内的周期性任务。具体这个服务的操作如下:

    sudo service cron status  #查看状态
    sudo service cron start   #启动服务
    sudo service cron stop    #停止服务
    sudo service cron restart #重启动服务

然后具体这个服务的配置文件似乎有几个，但一般都通过crontab这个命令查看或修改之，这样配置是会立即生效的。具体crontab的命令用法如下:

    crontab -l  #列出配置文件内容
    crontab -e  #进入配置文件编辑

一般的写法就是:

    分 时 日 月 星期几 命令

其中小时是24时制，星期几0表示星期日，1表示星期一，后面类推。后面的命令就是一行简单的shell命令，如果是多行命令的话建议写成bash脚本，然后给这个脚本可执行权限，然后写上该脚本的绝对路径名即可。

具体文档给出了这样一个例子:

    # 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/

这里的数字0就表示0分钟，5就表示5小时，然后\*表示随意不做要求，1表示星期一。这样这行命令总的意思是每周一上午五点整执行一次这个命令。

再来看个例子:

    */5 * * * * echo  $(date +"%F_%T") "i am working" >> /tmp/test.log

上面这种"\*/5"这种分隔符表达意思是每隔五分钟，然后将这些信息追加到这个log日志文件中去。

然后这个是每天早上七点做什么。

    0 7 * * * command

更多信息请参看光头红薯的 [这篇帖子](http://www.oschina.net/question/12_2535) 。

# flock命令<a id="orgheadline10"></a>

flock命令可用于linux系统中管理某个bash脚本中的某段代码在一个时间段内只有一个进程存在，也就是通过一个文件来设置锁的技术，称之为文件锁。最常用的文件锁，也是flock命令默认的模式就是排他锁模式，这种情况下该锁文件别人既不可读也不可写；此外还有一种什么共享锁模式，此时别人是可以读的同样不可写。共享锁和排他锁的区别 [这个网页](http://stackoverflow.com/questions/11837428/whats-the-difference-between-an-exclusive-lock-and-a-shared-lock) 介绍得很好。

下面是一个简单的flock程序演示例子:

```sh
#!/bin/bash

(
  flock  200 

  echo "test"

  sleep 10

) 200&gt;/var/lock/test.lock

echo "test out"
```

读者可以简单地打开几个终端来测试一下，这里我们将会看到这段代码在后面进程中相当于被阻塞了，但还是在那里等待着。

如果我们将代码改为:

```sh
#!/bin/bash

(
  flock -w 1 200 || exit 1

  echo "test"

  sleep 10

) 200&gt;/var/lock/test.lock

echo "test out"
```

这是另外一种很常用的形式，这里的-w选项设置了一个等待时间，比如你开了第一个进程之后，第二个进程会等待1s，获不得文件锁就将exit 1 ，注意这里exit 1之后只是flock这行命令退出了，后面的echo命令还将继续执行，这通常不是我们期望的行为。所以后面一般再加上或逻辑然后再执行exit 1，这就退出整个flock这个执行代码了。

这样测试的结果是，第一个进程占有文件锁之后，后面的进程都试探一次之后就会退出，然后flock代码块后面的代码是都会执行的。

这里的句柄号fd 200并没什么特殊含义，请参看 [这个网页](http://stackoverflow.com/questions/13551840/bash-flock-why-200) 。

# wc命令<a id="orgheadline12"></a>

## 统计行数<a id="orgheadline11"></a>

这通常在linux管道模式下使用，进行log文件grep之后的行数统计来获得一些额外的信息。

    wc -l

# lsof命令<a id="orgheadline13"></a>

我最先接触lsof命令是如下需求: 查看端口号1080是被谁占用了，如果你希望释放该端口号，则kill掉该进程即可。

    lsof -i :1080

这里的 **lsof** 命令倒不是专门为了查看端口号而设置的，其完整名字为list open files，也就是列出系统当前打开的文件的意思。由于在linux系统中， <span class="underline">一切皆文件</span> ，所以通过查看打开的文件信息能够获得很多有用的当前系统运行情况的信息。下面内容主要参考了 [这个网页](http://www.ha97.com/1029.html) 和 [这个网页](http://www.oschina.net/question/12_145479) 。

在我们输入如下命令之后:

```bash
sudo lsof | head
```

会看到一些信息，这个lsof命令一般输出内容都会很长，所以将其通过管道送入head命令中去了。然后刚开始很多信息的读取都需要管理员权限（倒不是会出错，而是信息读取不倒），所以这里也加上管理员权限了。

    COMMAND    PID  TID    USER   FD     TYPE   DEVICE   SIZE/OFF       NODE NAME
    init         1         root  cwd      DIR      8,7       4096          2 /
    init         1         root  rtd      DIR      8,7       4096          2 /
    init         1         root  txt      REG      8,7     265848    1704003 /sbin/init
    ......

输出的格式大抵就是如下这几列:

-   **COMMAND:** 进程名
-   **PID:** 进程号
-   **USER:** 进程所有者
-   **FD:** 文件描述符，应用程序通过文件描述符来识别文件。
    -   **cwd:** Current working directory
    -   **txt:** Text file
    -   **mem:** Memory Mapped file
    -   **mmap:** Memory Mapped device
    -   **Number:** It represent the actual file descriptor. For example, 0u, 1w and 3r

-   **TYPE:** 文件类型
    -   **REG:** Regular file
    -   **DIR:** Directory
    -   **CHR:** Character special file
    -   **FIFO:** First in first out
-   **DEVICE:** 指定磁盘名称
-   **SIZE:** 文件大小
-   **NODE :** 索引节点，文件在磁盘上的标识
-   **NAME:** 具体打开文件的名字

对于上面的这些列有如下的筛选选项:

    lsof -c string 按照COMMAND列过滤，目标进程名包含string这个字符串。
    lsof -u username 按照USER列过滤，指定具体的user是谁。
    lsof -p PID 按照PID列过滤，指定具体的PID是多少。
    lsof -d FD 按照FD这一列进行过滤，具体根据指定的文件描述符来。

然后 `-i` 用法上面谈过一点了，可以用来查看具体端口号被那个进程占用了。你还可以查看多个进程，如下所示:

    lsof -i :1-100

这是查看端口号1到100的占用情况。

实际 `-i` 选项是针对网络连接的情况的，如果只是纯用 `-i` 选项，将列出所有和网络连接相关的进程。然后 `-i` 后面可以跟的描述形式挺复杂的:

    lsof -i [46] [protocol][@hostname|hostaddr][:service|port]

后面都是过滤选项吧，4指IPv4，6指IPv6。protocol是指TCP或UDP:

    lsof -i 4TCP

这是指列出网络连接IPv4，协议为TCP的进程。

    lsof -i 4TCP@localhost

这是指列出网络连接IPv4，协议为TCP，host是localhost的进程。

    lsof -i 4TCP@localhost:1000-3000

这是指列出网络连接IPv4，协议为TCP，host是localhost，端口号是1000到3000的进程。

lsof命令还有 `+D` 选项，其作用是列出某文件夹下已经被打开的文件。

    sudo lsof +D /var/log

# 终端开启代理<a id="orgheadline14"></a>

没啥好的代理，自由门那个有时还可以用，有时还是需要在终端开启全局代理，然后再运行python脚本，这样省去了很多麻烦。

    export HTTP_PROXY="http://127.0.0.1:8580"
    export HTTPS_PROXY="http://127.0.0.1:8580"

# netcat命令<a id="orgheadline16"></a>

参考了 [这个网页](http://www.oschina.net/translate/linux-netcat-command) 。

最简单的使用如下，可用于很简单的和服务器的交互。

    netcat ip地址 端口号

## 侦测开放端口<a id="orgheadline15"></a>

    nc -z -v -n 172.31.100.7 21-25

-   **-z:** 连接成功之后立即关闭
-   **-v:** 这个不用多说，冗余输出
-   **-n:** 不要使用DNS反向查询域名

# curl命令<a id="orgheadline20"></a>

最基本的用法就是

```bash
curl the_url
```

the\_url就是类似在浏览器上的输入，然后将会返回爬取的结果。

然后一些选项如下所示（参考了 [这个网页](http://www.ruanyifeng.com/blog/2011/09/curl.html) ）:

-   **-o:** 结果输出到文件
-   **-L:** 开启网页自动跳转
-   **-i:** 显示网页响应头
-   **-I:** 只显示响应头
-   **-v:** 不用多说，冗余信息打印
-   **-d:** post方法的送数据，具体格式是:

    curl --data "data=xxx" example.com/form.cgi

-   **-X:** 指定具体HTTP协议动作，如POST DELETE等

## 指定user-agent<a id="orgheadline17"></a>

    curl --user-agent "[User Agent]" [URL]

## 设置cookie<a id="orgheadline18"></a>

    curl --cookie "name=xxx" www.example.com

## 查看本机的外网ip<a id="orgheadline19"></a>

运行命令行:

    curl ifconfig.sh

你可以看到本机的外网ip，但是要注意，由于一般家庭用户都没有自己固定的外网ip，这似乎并没有什么实际用途。

# linux系统用户管理<a id="orgheadline27"></a>

## 新建用户<a id="orgheadline21"></a>

```bash
useradd new_user_name
```

新建用户有很多选项设置，这里值得一提的就是 `-d` 用于设置新建用的主文件夹。

## 删除用户<a id="orgheadline22"></a>

```bash
userdel -r user_name
```

选项 `-r` 用于删除该用户的主文件夹。

## 修改用户密码<a id="orgheadline23"></a>

修改用户的密码。默认是当前登录用户。

    passwd

如果你以root登录之后，可以具体来修改某个用户的密码:

    passwd the_name

## 用户其他参数修改<a id="orgheadline24"></a>

读者可以查看一下 `/etc/passwd` 文件里面的内容，其中 **usermod** 命令选项的修改都是和该文件的某项相关。这里就不列出来了，读者请通过 `--help` 细查之。比如:

    usermod the_name -md new_home

这是把某个用户的原主文件夹移到新的主文件夹那里。

## 以某用户身份登录<a id="orgheadline25"></a>

用 **login** 具体以某个用户登录，然后用 **exit** 退出该用户的登录。

## 让某个用户是sudoer<a id="orgheadline26"></a>

参考了 [这个网页](http://unix.stackexchange.com/questions/179954/username-is-not-in-the-sudoers-file-this-incident-will-be-reported) 。

```bash
sudo usermod -aG sudo,adm user_name
```

就是给某个用户加上sudo权限使其成为sudoer。

# nmap命令<a id="orgheadline30"></a>

扫描目标主机的端口号，参考了 [这个网页](http://blog.jobbole.com/54595/) 。

最简单的扫描就是:

    nmap 主机名 -v
    nmap ip地址 -v

## 扫描整个子网<a id="orgheadline28"></a>

```bash
namp 192.168.0.*
```

## 指定扫描端口<a id="orgheadline29"></a>

    nmap -p 80,443 192.168.0.101 #多个端口
    nmap -p 80-160 192.168.0.101 #端口范围

# ifconfig命令<a id="orgheadline31"></a>

# date命令<a id="orgheadline32"></a>

date命令前面已谈到一点，更多信息请参看 [这个网页](http://www.cyberciti.biz/faq/linux-unix-formatting-dates-for-display/) 。主要是一些输出格式的控制，这里就不赘述了。

<http://unix.stackexchange.com/questions/24626/quickly-calculate-date-differences>

# 参考资料<a id="orgheadline33"></a>

1.  鸟哥的私房菜