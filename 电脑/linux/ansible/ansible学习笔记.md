<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline4">1. 前言</a>
<ul>
<li><a href="#orgheadline1">1.1. 安装</a></li>
<li><a href="#orgheadline2">1.2. 免密钥ssh登录</a></li>
<li><a href="#orgheadline3">1.3. 第一个例子</a></li>
</ul>
</li>
<li><a href="#orgheadline8">2. hosts文件配置</a>
<ul>
<li><a href="#orgheadline5">2.1. 写上多个主机组</a></li>
<li><a href="#orgheadline6">2.2. 主机变量设置</a></li>
<li><a href="#orgheadline7">2.3. 主机的其他参数控制</a></li>
</ul>
</li>
<li><a href="#orgheadline9">3. ansible的配置文件</a></li>
<li><a href="#orgheadline18">4. playbooks</a>
<ul>
<li><a href="#orgheadline17">4.1. ansible其内的模块</a>
<ul>
<li><a href="#orgheadline10">4.1.1. ping模块</a></li>
<li><a href="#orgheadline11">4.1.2. service模块</a></li>
<li><a href="#orgheadline12">4.1.3. command模块</a></li>
<li><a href="#orgheadline13">4.1.4. copy模块</a></li>
<li><a href="#orgheadline14">4.1.5. cron模块</a></li>
<li><a href="#orgheadline15">4.1.6. get_url模块</a></li>
<li><a href="#orgheadline16">4.1.7. git模块</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#orgheadline28">5. playbook最佳实践</a>
<ul>
<li><a href="#orgheadline19">5.1. hosts文件</a></li>
<li><a href="#orgheadline20">5.2. site.yml</a></li>
<li><a href="#orgheadline21">5.3. tags单独运行子任务用法</a></li>
<li><a href="#orgheadline22">5.4. role的全局参数</a></li>
<li><a href="#orgheadline23">5.5. role里的局部参数</a></li>
<li><a href="#orgheadline24">5.6. common role</a></li>
<li><a href="#orgheadline25">5.7. debug role</a></li>
<li><a href="#orgheadline26">5.8. begin role</a></li>
<li><a href="#orgheadline27">5.9. end</a></li>
</ul>
</li>
<li><a href="#orgheadline38">6. how to do it</a>
<ul>
<li><a href="#orgheadline29">6.1. 将压缩包解压包远程机器目标点</a></li>
<li><a href="#orgheadline30">6.2. rsync风格的将某个文件夹复制过去</a></li>
<li><a href="#orgheadline31">6.3. 如何获得远程机器的更多参数信息</a></li>
<li><a href="#orgheadline32">6.4. command和 shell的区别</a></li>
<li><a href="#orgheadline33">6.5. 如何在pip的虚拟环境下工作</a></li>
<li><a href="#orgheadline34">6.6. 如何安装本地的rpm包</a></li>
<li><a href="#orgheadline35">6.7. 用户用户组权限管理</a></li>
<li><a href="#orgheadline36">6.8. 删除文件或文件夹</a></li>
<li><a href="#orgheadline37">6.9. 如何微调配置文件</a></li>
</ul>
</li>
<li><a href="#orgheadline41">7. 附录</a>
<ul>
<li><a href="#orgheadline39">7.1. yaml语法</a></li>
<li><a href="#orgheadline40">7.2. 参考资料</a></li>
</ul>
</li>
</ul>
</div>
</nav>


# 前言<a id="orgheadline4"></a>

ansible是一个自动部署工具，当我们学习到后面之后，就会发现只写一个简单的web app是不够的，常常远程计算机那边的环境需要很多配置，比如后台脚本的执行啊，nginx配置来服务静态文件啊等等。而每个任务都手工用 `ssh` 端来操作的将是非常低效率的了，尤其到后面各个任务繁多，环境需要重复部署的时候。ansible就是解决这一问题的。

## 安装<a id="orgheadline1"></a>

其似乎可以通过pip来安装，但其就是一个应用工具罢了，并没有打算将其作为一个python模块来看待，所以就直接利用ubuntu的apt-get工具来安装了。

    ## 一般应该都已经装上了 sudo apt-get install software-properties-common
    sudo apt-add-repository ppa:ansible/ansible
    sudo apt-get update
    sudo apt-get install ansible

其他安装方式请参看 [官方文档](http://docs.ansible.com/ansible/intro_installation.html) 。

## 免密钥ssh登录<a id="orgheadline2"></a>

参看了 [这个网页](http://liluo.org/blog/2011/05/ssh-automatic-login/) 。

具体就是在该用户的主文件夹里面的 `.ssh` 文件夹里面有些文件吧，比如 `id_rsa.pub` 是本用户的公钥， `id_rsa` 是本用户的私钥。如果你在本机上运行:

    ssh-keygen -t rsa

就会生成这两个文件，免密钥ssh登录的设置就是把你的 公钥 放入到 `authorized_keys` 这个文件里面去，所以我们可以理解为 `.ssh` 文件夹的 `authorized_keys` 文件就是用来管理谁谁的公钥在里面就可以直接登录本机了。

具体要做的就是登录到远程主机，然后把你的公钥加进去即可。

## 第一个例子<a id="orgheadline3"></a>

假设你现在可以免密钥登录某一个远程服务器了，然后你在 `/etc/ansible/hosts` 这个文件里面把你的服务器名字加进去，然后执行:

    ansible all -m ping

如果一切正常的话其将返回 SUCESS 信息，证明现在你已经通过ansible正常连通你的远程服务器了。

# hosts文件配置<a id="orgheadline8"></a>

现在继续深入上面提及的那个hosts文件的配置。这里推荐阅读参考资料提及的官方文档的中文版，因为我对这一块很多术语不是很熟悉，阅读英文还是有点吃力的。比如说这里讨论的 `/etc/ansible/hosts` 这个文件是所谓的默认 `inventory` 文件，除了这个默认inventory配置文件之外，还可以写很多其他的配置文件的。而这些配置文件内容大体如下:

    [webservers]
    foo.example.com
    bar.example.com

`[webservers]` 这个字段定义的是所谓的主机组的概念，之前我们随便写上去的那个主机没属于任何主机组，然后一个主机组似乎还可以属于另外一个主机组等，这个有点复杂了。似乎主机组里面的主机可以怎么统一管理，这个后面再说。

## 写上多个主机组<a id="orgheadline5"></a>

额，这个简单了解下吧，就是写一句话对应多个主机吧，感觉好高端离我们这些平民好远了啊。

    [webservers]
    www[01:50].example.com
    
    [databases]
    db-[a:f].example.com

## 主机变量设置<a id="orgheadline6"></a>

组的变量情况请看文档下面，主机变量大体就是后面写上一些值就是了，因为这些变量在定义后playbooks也是可以使用的，而playbooks无疑是后面的重头戏，所以这还是值得提一下的。

    [atlanta]
    host1 http_port=80 maxRequestsPerChild=808
    host2 http_port=303 maxRequestsPerChild=909

## 主机的其他参数控制<a id="orgheadline7"></a>

应该大多和具体ssh连接的配置有关吧，比如:

    some_host         ansible_ssh_port=2222     ansible_ssh_user=manager

-   **`ansible_ssh_host`:** 这个一般没啥好设置的，不过可能你的主机名很长，则通过这个设置一下作为具体连接的主机名。而前面写的 `some_host` 只是作为主机别名。如果你的ansible版本号大于2了，那么推荐使用 `ansible_host` 。

-   **`ansible_ssh_port`:** 端口号，默认不需要配置。如果你的ansible版本号大于2了，那么推荐使用 `ansible_port` 。

-   **`ansible_ssh_user`:** ssh登录用户名，默认是你当前电脑的当前登录用户名，这个可能在某些情况下需要配置。如果你的ansible版本号大于2了，那么推荐使用 `ansible_user` 。

-   **`ansible_ssh_pass`:** 免密钥登录不需要配置。文档说不推荐使用。

后面一些感觉更不常用了，不过这个似乎有时会有用:

-   **`ansible_python_interpreter`:** 设置python编译器的路径，但实际操作用处也不大，一般推荐用virtualenv来管理python的模块吧。

# ansible的配置文件<a id="orgheadline9"></a>

这个应该是关于整个ansible环境的配置，有需要的看下吧。

# playbooks<a id="orgheadline18"></a>

感觉实际操作playbooks才是应该好好熟悉的一部分，所以什么 ad-hoc 命令，也就是通过ansible单刷某个命令的方式跳过去了，直接进入正题吧。playbooks内容很多，当然首先需要简单了解下yaml语法，但这连门都还没进去，慢慢来吧。

下面是最简单的一个例子，新建这么一个 `first.yaml` 文件:

```yaml
---
- hosts: work
  tasks:
  - name : ping and pong
    ping :
```

然后执行是:

    ansible-playbook first.yaml

这里只是简单的ping pong 了一下，这个配置简单的内容就是主机 `work` ，这个是在之前提到的 `/etc/ansible/hosts` 那个文件里定义的。然后对这个主机执行某个任务 `tasks` 。这是一个任务列表清单，name 描述了该任务，文字随意。然后执行了 `ping` 模块。

这个任务确保nginx重启了一次:

    - name: make sure nginx restarted
      service: name=nginx state=restarted

这个任务是确保nginx服务是运行着的:

    - name: make sure nginx is running
      service: name=nginx state=running

## ansible其内的模块<a id="orgheadline17"></a>

我们看到ansible-playbook就最基本的配置编写和使用还是很简单的，关键是具体任务那边要熟悉好一些特定的模块，ansible其内的模块可以用海量还形容，而且你还可以编写自己的模块。核心模块可以参看这个 [项目](https://github.com/ansible/ansible-modules-core) 。下面先简要介绍一些应该是很常用的模块。

### ping模块<a id="orgheadline10"></a>

试着连接主机，然后确认一个可用的python环境，然后返回pong。

### service模块<a id="orgheadline11"></a>

控制远程主机的后台服务。

-   **name:** 具体服务名。
-   **state:** 有四个选项: started, stoped, restarted, reloaded。具体是启动，停止，重启，重新加载。
-   **enabled:** 是否开机启动。
-   **args:** 额外的参数。

### command模块<a id="orgheadline12"></a>

在远程主机执行一个shell命令，重要级别不言而喻。

关机

    - command: /sbin/shutdown -t now

### copy模块<a id="orgheadline13"></a>

复制本机文件到远程主机。

-   **backup:** 在覆盖前备份原文件
-   **src:** 本地源文件
-   **dest:** 远程主机目标文件
-   **owner:** 文件的所有者
-   **mode:** 文件的模式
-   **group:** 文件的所有群
-   **force:** 强制文件替换，若为no则不替换

### cron模块<a id="orgheadline14"></a>

### get\_url模块<a id="orgheadline15"></a>

### git模块<a id="orgheadline16"></a>

# playbook最佳实践<a id="orgheadline28"></a>

## hosts文件<a id="orgheadline19"></a>

在项目的文件夹下新建一个hosts文件，其类似之前讨论的 `/etc/ansible/hosts` 文件，然后在本地通过如下语法引入：

    ansible-playbook -i hosts site.yml

## site.yml<a id="orgheadline20"></a>

刷脚本的主入口

## tags单独运行子任务用法<a id="orgheadline21"></a>

在roles文件夹里面新建一个common文件夹，然后common文件夹里面新建一个tasks文件夹，tasks文件夹里面定义一个main.yml，该文件内容大体如下:

    ---
    
    - name: task的名字
      command: ...

然后site.yml里面如下定义：

    ---
    
    - name: ansible 必要参数侦测
      hosts: all
      remote_user: root
      
      roles:
        - {role: common, tags: ['common']}

然后只运行某个子任务如下利用tags来完成。

    ansible-playbook -i hosts site.yml --tags=common

## role的全局参数<a id="orgheadline22"></a>

全局参数放在 group\_vars 文件夹的 all 文件里面，其也是一个简单的yaml问加。

## role里的局部参数<a id="orgheadline23"></a>

这些参数推荐在site.yml文件对应的role哪里定义，如下所示定义了一个 `folder_name` 变量 ：

    roles:
      - {role: update-sdsomweb, folder_name: "resource/install_venv", tags:  ['update-sdsomweb']}

## common role<a id="orgheadline24"></a>

common role的角色通常在完成某个单独子任务的时候也推荐将其加上，其一般完成某些任务必要的依赖安装和某些后续任务必要的远程机器环境参数的侦测工作。

## debug role<a id="orgheadline25"></a>

我们在debug role里面主要检测目标机器的一些参数看是不是符合我们的预期方便后续子任务的编写工作。如下所示:

    ---
    
    - name: debug for ansible_distribution
      debug: msg="{{ ansible_distribution }}"
      
    - name: debug for ansible_distribution_version
      debug: msg="{{ ansible_distribution_version }}"

## begin role<a id="orgheadline26"></a>

某些工作很特殊，最后放在最前面先做，那么推荐放在begin role里面。

## end<a id="orgheadline27"></a>

某些工作很特殊，最后安装配置的最后最后再做，那么这些内容就放在end role里面。

# how to do it<a id="orgheadline38"></a>

## 将压缩包解压包远程机器目标点<a id="orgheadline29"></a>

值得一提是unarchive模块最近才支持remote\_src模式，所以推荐还是采用本地压缩包源然后解压过去的方式。

    - name: 解压 apr 
      unarchive:
        src: "{{folder_name}}/apr-1.5.2.tar.gz"
        dest: /root

## rsync风格的将某个文件夹复制过去<a id="orgheadline30"></a>

为什么不利用copy模块，那就是scp如果文件夹里面结构稍微复杂点就会很慢，这时推荐使用 synchronize 模块：

    - name: 上传源
      synchronize: src=resource/winstore dest=/root mode=push

值得一提的是，rsync那边如果远程机器不是免密码ssh连接的话，这时又要输入密码，所以推荐common
 role里面一开始就将pub密钥传过去，然后这个功能需要远程机装了libselinux-python和 rsync 这两个软件包。

    - name: 上传ssh key
      authorized_key: user=root key="{{ lookup('file', '/home/what/.ssh/id_rsa.pub') }}"

这里的user是登录远程机器的用户名。

## 如何获得远程机器的更多参数信息<a id="orgheadline31"></a>

ansible的 setup 模块能够获得远程机器很多有用的信息，甚至能够知道远程机器运行的虚拟机软件是什么。不过你可能需要一些更多信息，比如远程机器默认的python版本是多少，这个时候我们可以用如下方式来获得：

    - name: get python version
      command: python -c 'import sys;print("{0}.{1}".format(sys.version_info.major,sys.version_info.minor))'
      register: python_version_check

这里的register注册的是执行上述命令command之后的返回结果，在ansible整个运行时里都是可以用，具体结果你可能还需要通过 `python_version_check.stdout` 这样的方式获得。

## command和 shell的区别<a id="orgheadline32"></a>

command和shell在很多情况下似乎都没有区别，shell严格意义上来讲就类似于你在shell中执行了某个命令，其可以使用bash的一些环境变量等，后面应该没事会优先考虑使用shell模块吧。

---

## 如何在pip的虚拟环境下工作<a id="orgheadline33"></a>

## 如何安装本地的rpm包<a id="orgheadline34"></a>

## 用户用户组权限管理<a id="orgheadline35"></a>

## 删除文件或文件夹<a id="orgheadline36"></a>

## 如何微调配置文件<a id="orgheadline37"></a>

# 附录<a id="orgheadline41"></a>

## yaml语法<a id="orgheadline39"></a>

一个简单例子如下:

```yaml
---
# 一位职工记录
name: Example Developer
job: Developer
skill: Elite
employed: True
foods:
    - Apple
    - Orange
    - Strawberry
    - Mango
languages:
    ruby: Elite
    python: Elite
    dotnet: Lame
```

yaml文件一开始都要加上这个:  `---` 。

注释是 `#`

然后相同缩进级别 `-` 开头的表示一个列表，然后其他键值对表示字典，大体就是这样。

## 参考资料<a id="orgheadline40"></a>

1.  官方 [英文文档](http://docs.ansible.com/ansible/index.html) ，这里有个翻译的 [中文文档](http://ansible-tran.readthedocs.io/en/latest/index.html) 。