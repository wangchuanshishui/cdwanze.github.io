<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline9">1. 结合github进行项目管理</a>
<ul>
<li><a href="#orgheadline1">1.1. 安装git</a></li>
<li><a href="#orgheadline2">1.2. 远程仓库文件到本地</a></li>
<li><a href="#orgheadline3">1.3. 初始化本地仓库</a></li>
<li><a href="#orgheadline4">1.4. 本地仓库文件进入索引</a></li>
<li><a href="#orgheadline5">1.5. 将索引中改动的文件提交到本地仓库</a></li>
<li><a href="#orgheadline6">1.6. 本地仓库改动更新到远程仓库</a></li>
<li><a href="#orgheadline7">1.7. 远程仓库的改动更新到本地</a></li>
<li><a href="#orgheadline8">1.8. 日常改动提交流程总结</a></li>
</ul>
</li>
<li><a href="#orgheadline21">2. git补充知识</a>
<ul>
<li><a href="#orgheadline10">2.1. 第一次使用的配置</a></li>
<li><a href="#orgheadline11">2.2. 初始化仓库</a></li>
<li><a href="#orgheadline12">2.3. 远程仓库克隆到本地</a></li>
<li><a href="#orgheadline13">2.4. 本地文件进入索引</a></li>
<li><a href="#orgheadline14">2.5. 将索引跟踪的文件改动提交到本地仓库</a></li>
<li><a href="#orgheadline15">2.6. 本地仓库提交到远程仓库</a></li>
<li><a href="#orgheadline16">2.7. 远程仓库的改动更新到本地</a></li>
<li><a href="#orgheadline20">2.8. github其他小信息</a>
<ul>
<li><a href="#orgheadline17">2.8.1. .gitignore文件</a></li>
<li><a href="#orgheadline18">2.8.2. 如何删除本项目</a></li>
<li><a href="#orgheadline19">2.8.3. 本地仓库管理文件丢失</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#orgheadline22">3. 参考资料</a></li>
</ul>
</div>
</nav>


# 结合github进行项目管理<a id="orgheadline9"></a>

## 安装git<a id="orgheadline1"></a>

Ubuntu用apt-get命令安装git即可：

```sh
sudo apt-get install git
```

还有些文档说要安装git-core，Bergman说这是一个dummy package（仿制品），删掉就用git也没事的。<sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup> 

到github上注册，创建新的项目,这些我就不多说了。下面就git命令使用的基本流程说明如下：

## 远程仓库文件到本地<a id="orgheadline2"></a>

网上创建项目之后，你需要将网上的存档下载到本地，在你希望下载的地点，打开终端：

    git clone https://github.com/a358003542/xelatex-guide-book.git

后面的这个链接地址在你创建的项目的右下角哪里，写着HTTPS clone URL。

## 初始化本地仓库<a id="orgheadline3"></a>

**git init** 命令用于初始化本地仓库， **git clone** 下来的仓库文件已经初始化了，然后 **origin** 这个远程服务器名字也已经加上去了。<sup><a id="fnr.2" class="footref" href="#fn.2">2</a></sup>

## 本地仓库文件进入索引<a id="orgheadline4"></a>

让本地仓库文件进入git的索引（从而git对该文件进行变更的监控），让文件夹内的所有文件都进入索引是大家很常用的命令：

    git  add  .

如果你本地删除了文件，你希望仓库里面也删除这些文件，那么使用命令：

```sh
git  add  --all  .
```

## 将索引中改动的文件提交到本地仓库<a id="orgheadline5"></a>

```sh
git  commit   -m  '2013-08-25:19:00'
```

后面的文字串等下在github网站中会看到的，表示这个文件的标示符吧，你也可以取其他的名字，比如version0.1之类的。

## 本地仓库改动更新到远程仓库<a id="orgheadline6"></a>

第一次你需要给你的远程服务器取个简单点的名字：

    git remote add origin 
            https://github.com/a358003542/xelatex-guide-book.git

这里的 **origin** 的意思是远程服务器的简称，按理来说这个名字是可以随便取的，不过大家似乎都是取得origin，然后你从github上clone下来的仓库默认远程服务器名字大多也是 **origin** ， **master** 是远程仓库默认的一个分支，后面会讲到你可以创建其他的分支。

然后以后都可以用这个简单的命令来更新了：

```sh
git  push  origin  master
```

## 远程仓库的改动更新到本地<a id="orgheadline7"></a>

下面这个命令git对文件的操作是合并式的，也就是只是替换最新改动的文件。如果你希望远程仓库所有改动包括删除也更新到本地，使用可选项 `-- all` 。

```sh
git  pull origin master
```

## 日常改动提交流程总结<a id="orgheadline8"></a>

一般情况下就 add commit push 这三步。这是基本的日常维护提交流程。

如果你在网站上对远程仓库做了一些修改，记得先用pull命令将远程仓库的改动更新到本地。

# git补充知识<a id="orgheadline21"></a>

这段对上面提及的一些命令进行更加详细的讲解。当然读者可以再看一遍，就当是复习了。

## 第一次使用的配置<a id="orgheadline10"></a>

设置你的名字和email：

```sh
git config --global user.name "Your Name"
git config --global user.email "your_email@whatever.com"
```

这个是git的全局设置，和具体项目无关。你可以打开Ubuntu系统的主文件夹下的 `.gitconfig` 文件看一下。

## 初始化仓库<a id="orgheadline11"></a>

```sh
git init
```

**git init** 即在当前工作目录下初始化git的管理仓库，如果你打开查看隐藏文件，会看到一个 `.git` 文件夹，git用于管理当前项目的一些文件就存放在这里面，所谓的本地仓库应该也是放在这里面的。

如果你是在github上创建的项目，然后将这个项目克隆下来，那么就不需要再执行init命令，远程仓库已经执行了。

## 远程仓库克隆到本地<a id="orgheadline12"></a>

网上创建项目之后，你需要将网上的存档下载到本地，在你希望下载的地点，打开终端：

```sh
git clone theURL
```

上面代码的“theURL”就是你的项目的网页地址，在地址栏复制即可。此外还有什么SSH链接在github网页项目的右下角那里，一般使用就用https链接吧。

## 本地文件进入索引<a id="orgheadline13"></a>

本地文件进入git的索引，该文件夹内的所有文件都进入索引则在终端中输入如下命令：

```sh
git add theFilename
```

我们在github创建项目的时候已经创建了一个 `.gitignore` 配置文件，然后git是不索引这些后缀名的文件的。

如果你本地删除了文件，你希望远程仓库也删除这些文件，那么需要加上 `--all` 选项，这样我们一般日常更新本地文件夹的索引常使用如下命令：

```sh
git  add  --all   .
```

## 将索引跟踪的文件改动提交到本地仓库<a id="orgheadline14"></a>

这里的commit命令提交是指提交给本地git的管理仓库，就是 `.git` 文件夹里面的一些内容。

```sh
git  commit   -m  '0.01'
```

后面的文字串等下在github网站中会看到的，跟在文件名后面的，所以建议取简短一点。

## 本地仓库提交到远程仓库<a id="orgheadline15"></a>

第一次你需要给你的远程服务器取个简单点的名字：

```sh
git remote add origin theURL
```

上面代码的“theURL”就是你的项目的网页地址。

然后以后都可以用这个简单的命令来更新了：

```sh
git  push  origin  master
```

这里的origin的意思是远程服务器的简称，按理来说这个名字是可以随便取的，不过大家似乎都是取得origin，然后你从github上clone下来的内容大多也是origin <sup><a id="fnr.3" class="footref" href="#fn.3">3</a></sup> ，master是远程仓库默认的一个分支，后面会讲到你可以创建其他的分支。

## 远程仓库的改动更新到本地<a id="orgheadline16"></a>

下面这个命令git pull对文件的操作是合并式的，也就是只是替换最新改动的文件。如果你希望远程仓库所有改动包括删除也更新到本地，使用请可选项 `--all` 。

```sh
git  pull origin master
```

## github其他小信息<a id="orgheadline20"></a>

### .gitignore文件<a id="orgheadline17"></a>

你在github创建项目的时候如果选择好了项目语言，就会自动创建一个 `.gitignore` 文件，文件语法很简单，比如 `*.out` 则项目内所有后缀为out的文件都不会被加入索引。

### 如何删除本项目<a id="orgheadline18"></a>

在github项目网站右下角settings哪里进去有很多项目管理内容，其中最下面有删除项目的功能，请慎重使用。

### 本地仓库管理文件丢失<a id="orgheadline19"></a>

如果你把本地仓库隐藏的.git文件夹删除了，但是本地的更改你又想上传到远程仓库，你首先需要 `git init` ，然后添加远程服务器名字， `git remote add origin` 地址。然后建立本地索引， `git add -- all` 。然后commit和push。这里可能远程服务器会拒绝，push的时候加入 `-f` 选项会强制push， <span class="underline">但是要注意这样github网页里面所有之前commit的记录都没有了</span> 。

# 参考资料<a id="orgheadline22"></a>

1.  [git简明指南](http://rogerdudler.github.io/git-guide/index.zh.html)

2.  [git howto](http://githowto.com/)

3.  [图解git](http://marklodato.github.io/visual-git-guide/index-zh-cn.html)

4.  [git community book中文版](http://gitbook.liuhui998.com/)

<div id="footnotes">
<h2 class="footnotes">Footnotes: </h2>
<div id="text-footnotes">

<div class="footdef"><sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> <div class="footpara">[请参看这个网页](http://askubuntu.com/questions/5930/what-are-the-differences-between-the-git-and-git-core-packages)</div></div>

<div class="footdef"><sup><a id="fn.2" class="footnum" href="#fnr.2">2</a></sup> <div class="footpara">参考了[这个网站](http://www.cnblogs.com/findingsea/archive/2012/08/27/2654549.html)</div></div>

<div class="footdef"><sup><a id="fn.3" class="footnum" href="#fnr.3">3</a></sup> <div class="footpara">也就是你从远程仓库clone下面的内容不需要在add origin这个属性了，直接push就可以了。</div></div>


</div>
</div>