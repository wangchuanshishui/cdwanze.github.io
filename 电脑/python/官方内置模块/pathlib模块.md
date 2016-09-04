<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline2">1. 简介</a>
<ul>
<li><a href="#orgheadline1">1.1. 第一个例子</a></li>
</ul>
</li>
<li><a href="#orgheadline39">2. Path对象详解</a>
<ul>
<li><a href="#orgheadline6">2.1. 基于Path的遍历</a>
<ul>
<li><a href="#orgheadline3">2.1.1. iterdir方法</a></li>
<li><a href="#orgheadline4">2.1.2. glob方法</a></li>
<li><a href="#orgheadline5">2.1.3. rglob方法</a></li>
</ul>
</li>
<li><a href="#orgheadline11">2.2. 基于Path的判断</a>
<ul>
<li><a href="#orgheadline7">2.2.1. exists()</a></li>
<li><a href="#orgheadline8">2.2.2. is_file()</a></li>
<li><a href="#orgheadline9">2.2.3. is_dir()</a></li>
<li><a href="#orgheadline10">2.2.4. is_symlink()</a></li>
</ul>
</li>
<li><a href="#orgheadline19">2.3. 基于Path的路径组合操作</a>
<ul>
<li><a href="#orgheadline12">2.3.1. parts</a></li>
<li><a href="#orgheadline13">2.3.2. drive</a></li>
<li><a href="#orgheadline14">2.3.3. root</a></li>
<li><a href="#orgheadline15">2.3.4. anchor</a></li>
<li><a href="#orgheadline16">2.3.5. parents</a></li>
<li><a href="#orgheadline17">2.3.6. parent</a></li>
<li><a href="#orgheadline18">2.3.7. joinpath</a></li>
</ul>
</li>
<li><a href="#orgheadline29">2.4. 基于Path的常规命令操作</a>
<ul>
<li><a href="#orgheadline20">2.4.1. cwd()</a></li>
<li><a href="#orgheadline21">2.4.2. stat()</a></li>
<li><a href="#orgheadline22">2.4.3. chmod(mode)</a></li>
<li><a href="#orgheadline23">2.4.4. rename(target)</a></li>
<li><a href="#orgheadline24">2.4.5. rmdir()</a></li>
<li><a href="#orgheadline25">2.4.6. lchmod(mode)</a></li>
<li><a href="#orgheadline26">2.4.7. lstat()</a></li>
<li><a href="#orgheadline27">2.4.8. mkdir(mode=0o777, parents=False)</a></li>
<li><a href="#orgheadline28">2.4.9. touch</a></li>
</ul>
</li>
<li><a href="#orgheadline38">2.5. 基于Path的文件操作</a>
<ul>
<li><a href="#orgheadline30">2.5.1. suffix</a></li>
<li><a href="#orgheadline31">2.5.2. suffixes</a></li>
<li><a href="#orgheadline32">2.5.3. name</a></li>
<li><a href="#orgheadline33">2.5.4. stem</a></li>
<li><a href="#orgheadline34">2.5.5. open(mode='r', buffering=-1, encoding=None, errors=None, newline=None)</a></li>
<li><a href="#orgheadline35">2.5.6. as_uri</a></li>
<li><a href="#orgheadline36">2.5.7. as_posix</a></li>
<li><a href="#orgheadline37">2.5.8. is_absolute</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</nav>


# 简介<a id="orgheadline2"></a>

自python3.4以后起，python3就内置了pathlib模块了，不过之前的python版本，通过pip安装pathlib之后，后面的使用也差不了太多了。下面的讨论主要参考了python3.4 pathlib模块的官方文档，以其为准。

这个模块主要让我们对系统的路径更加灵活的操作，python取代bash进行系统运维的时候，有大量的对文件名，路径等的操作，pathlib将大大简化我们在这一块的工作量。

下面的例子是在python2.7，通过pip安装pathlib环境下运行的。就一般的使用使用 `Path` 类即可。

## 第一个例子<a id="orgheadline1"></a>

```python
from pathlib import Path
import os

p1 = Path(os.path.expanduser('~'))
p2 = Path('.')

print([x for x in p1.glob("*.pdf") if x.is_file()])
print([x for x in p2.iterdir() if x.is_dir()])
```

其运行结果如下:

    [PosixPath('/home/wanze/Pentaho Analytics for MongoDB.pdf'), PosixPath('/home/wanze/Python_for_Data_Analysis.pdf'), PosixPath('/home/wanze/pearsons.pdf'), PosixPath('/home/wanze/ecs_sdk.pdf'), PosixPath('/home/wanze/Pentaho Kettle Solutions.pdf')]
    [PosixPath('Rambutan'), PosixPath('wanze_private'), PosixPath('forebrain'), PosixPath('python-future')]

这里Path是可以接受相对路径语法的，所以"."和".."都是可用的。然后Path对象有方法glob和iterdir方法，其中glob就是类似linux的glob命令，这个后面细讲；然后iterdir将遍历当前目录。遍历之后返回了一个可迭代对象（读者可以看一下，是一个生成器对象），展开之后仍然是一个个Path对象。然后Path对象有 `is_file` 方法和 `is_dir` 方法来判断该Path对象是不是文件夹或者文件路径。

# Path对象详解<a id="orgheadline39"></a>

## 基于Path的遍历<a id="orgheadline6"></a>

### iterdir方法<a id="orgheadline3"></a>

### glob方法<a id="orgheadline4"></a>

### rglob方法<a id="orgheadline5"></a>

然后和一些基于Path的判断函数结合，我们可以设计出一些更简便的函数:

## 基于Path的判断<a id="orgheadline11"></a>

### exists()<a id="orgheadline7"></a>

### is\_file()<a id="orgheadline8"></a>

### is\_dir()<a id="orgheadline9"></a>

### is\_symlink()<a id="orgheadline10"></a>

    def ls_file(path="."):
        return [p for p in Path(path).iterdir() if p.is_file()]
    
    def ls_dir(path="."):
        return [p for p in Path(path).iterdir() if p.is_dir()]

## 基于Path的路径组合操作<a id="orgheadline19"></a>

### parts<a id="orgheadline12"></a>

### drive<a id="orgheadline13"></a>

### root<a id="orgheadline14"></a>

### anchor<a id="orgheadline15"></a>

### parents<a id="orgheadline16"></a>

### parent<a id="orgheadline17"></a>

### joinpath<a id="orgheadline18"></a>

## 基于Path的常规命令操作<a id="orgheadline29"></a>

### cwd()<a id="orgheadline20"></a>

### stat()<a id="orgheadline21"></a>

### chmod(mode)<a id="orgheadline22"></a>

### rename(target)<a id="orgheadline23"></a>

### rmdir()<a id="orgheadline24"></a>

### lchmod(mode)<a id="orgheadline25"></a>

### lstat()<a id="orgheadline26"></a>

### mkdir(mode=0o777, parents=False)<a id="orgheadline27"></a>

### touch<a id="orgheadline28"></a>

## 基于Path的文件操作<a id="orgheadline38"></a>

### suffix<a id="orgheadline30"></a>

### suffixes<a id="orgheadline31"></a>

### name<a id="orgheadline32"></a>

### stem<a id="orgheadline33"></a>

### open(mode='r', buffering=-1, encoding=None, errors=None, newline=None)<a id="orgheadline34"></a>

### as\_uri<a id="orgheadline35"></a>

### as\_posix<a id="orgheadline36"></a>

### is\_absolute<a id="orgheadline37"></a>

group()

is\_socket()

is\_fifo()

is\_block\_device()

is\_char\_device()

owner()

replace(target

resolve

symlink\_to

unlink