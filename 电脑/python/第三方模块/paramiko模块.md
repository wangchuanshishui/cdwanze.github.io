<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 简介和安装</a></li>
<li><a href="#orgheadline4">2. SSHClient类</a>
<ul>
<li><a href="#orgheadline2">2.1. exec_comand方法</a></li>
<li><a href="#orgheadline3">2.2. open_sftp方法</a></li>
</ul>
</li>
</ul>
</div>
</nav>


# 简介和安装<a id="orgheadline1"></a>

paramiko是一个python模块提供了ssh(Secure Shell)协议支持。

安装就用pip安装之。

    pip install paramiko

# SSHClient类<a id="orgheadline4"></a>

基本的使用就是通过SSHClient新建一个ssh client对象，然后通过这个对象进行连接，连接之后再进行其他的一些操作。下面演示一个简单的 `get_ssh_client` ，其将返回一个连接好了的ssh client对象。

```python
import paramiko
from paramiko.client import SSHClient
import getpass

def get_ssh_client(hostname, username=None,port=22, password=None, pkey=None, key_filename=None):
    client = SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for i in range(10):
        try:
            client.connect(hostname=hostname, port=port,username=username,password=password,pkey=pkey,key_filename=key_filename)
            return client
        except paramiko.ssh_exception.AuthenticationException:
            if password is None:
                password = getpass.getpass("please input the password: ")
            else:
                password = getpass.getpass("you may input the wrong password, please try again: ")
        except Exception as ex:
            import time
            print("some unknow problem, i will wait and try it again")
            time.sleep(10)
```

上面这段代码就是通过SSHClient新建了一个ssh client对象，然后调用connect方法来进行连接。具体connect连接方法会进行很多尝试:

1.  首先是试着根据传递过来的pkey参数或者key\_filename参数来。
2.  通过其他SSH agent来。
3.  最常用的，通过系统~/.ssh文件来。
4.  通过具体的username和password来。

然后上面代码的这一句:

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

的意思是试着查看你系统里的那个known\_hosts文件，如果没有则采用自动添加策略。这个一般都要加上。

然后整个程序采用了多次try试探机制，并设置了多次重连，和可能的密码输入错误排除。因为我不喜欢代码里面将密码明文写出来这种风格，所以最好还是采取实时输入的方法。

## exec\_comand方法<a id="orgheadline2"></a>

现在我们通过这个 `get_ssh_client` 函数返回的ssh client对象，其已经连接上目标远程主机了，接下来等着我们的就是具体来执行某个命令了，其主要通过调用 `exec_command` 方法来完成。这小节内容参考了 [这个网页](http://sebastiandahlgren.se/2012/10/11/using-paramiko-to-send-ssh-commands/) 。

    stdin,stdout,stderr = sshclient.exec_command('ls')
    
    print(stdout.read())

具体返回的是stdin，stdout，stderr这三个类似python中文件对象的东西，其内有channel属性，其实paramiko模块里定义的Channel对象，这些Channel对象有很多方法。比如exit\_status\_ready()来判断这个channel是否已经远程终止了，recv\_ready()用来判断这个channel可以读了，等等。

这样的返回确实不太好用，可以考虑进一步封装SSHClient对象:

```python
class MySSHClient(SSHClient):
    def __init__(self):
        super(MySSHClient,self).__init__()


    def exec_command(self,cmd):
        stdin,stdout,stderr = super(MySSHClient,self).exec_command(cmd)

        while not stdout.channel.exit_status_ready():
            while stdout.channel.recv_ready():
                print stdout.channel.recv(1024)
            while stdout.channel.recv_stderr_ready():
                print stdout.channel.recv_stderr(1024)

    def exec_sudo_command(self,cmd,password=None):
        sudo_cmd = "sudo -S " + cmd
        if password is None:
            password = getpass.getpass("please input the remote password: ")

        stdin,stdout,stderr = super(MySSHClient,self).exec_command(cmd)

        if not stdout.channel.closed:
            stdin.write('%s' % password)
            stdin.flush()

        while not stdout.channel.exit_status_ready():
            while stdout.channel.recv_ready():
                print stdout.channel.recv(1024)
            while stdout.channel.recv_stderr_ready():
                print stdout.channel.recv_stderr(1024)
```

这里主要是给 `exec_command` 命令提供了额外的打印支持，包括正常输出和可能的错误输出。然后加入 `exec_sudo_command` 可用于执行管理员命令。

## open\_sftp方法<a id="orgheadline3"></a>

调用sshclient对象的open\_sftp方法将会返回一个SFTPClient对象。通过paramiko.sftp\_client.SFTPClient这个SFTPClient对象，我们可以进行很多和sftp相关的操作，比如get方法进行下载文件和put方法进行上传文件操作。

    get(remotepath, localpath, callback=None)
    
    put(localpath, remotepath, callback=None, confirm=True)