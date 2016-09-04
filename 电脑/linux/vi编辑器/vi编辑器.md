<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 前言</a></li>
<li><a href="#orgheadline2">2. 常用快捷键</a></li>
<li><a href="#orgheadline3">3. 块选择</a></li>
<li><a href="#orgheadline10">4. 查找和替换</a>
<ul>
<li><a href="#orgheadline4">4.1. 匹配某个单词</a></li>
<li><a href="#orgheadline5">4.2. 查找历史</a></li>
<li><a href="#orgheadline6">4.3. 反向查找</a></li>
<li><a href="#orgheadline7">4.4. 锚定行的开始</a></li>
<li><a href="#orgheadline8">4.5. 锚定行的结尾</a></li>
<li><a href="#orgheadline9">4.6. 匹配空行</a></li>
</ul>
</li>
<li><a href="#orgheadline15">5. vimrc配置</a>
<ul>
<li><a href="#orgheadline11">5.1. 解决Backspace键乱码和方向键乱码</a></li>
<li><a href="#orgheadline12">5.2. 自动缩进</a></li>
<li><a href="#orgheadline13">5.3. 设置行号</a></li>
<li><a href="#orgheadline14">5.4. 开启语法高亮</a></li>
</ul>
</li>
</ul>
</div>
</nav>


# 前言<a id="orgheadline1"></a>

推荐ubuntu下安装完整版的vim

    apt install vim

这样一些按键乱码问题会自动解决。

然后注意中文输入法状态下可能会造成你切换vi模式的困扰。

# 常用快捷键<a id="orgheadline2"></a>

-   Ctrl + f  屏幕向下移动一页

-   G 移动到最后一行

-   gg 移动到第一行 推荐就直接用 `1G` 行跳转操作， `100G` 意思是跳转到第100行。

-   dd 删除当前行

-   yy 复制当前行

-   p 粘贴

-   u 撤销

-   r redo

# 块选择<a id="orgheadline3"></a>

按键 `v` 进入块选择，然后移动光标进行块选择。

-   y 复制块

-   d 删除块

# 查找和替换<a id="orgheadline10"></a>

## 匹配某个单词<a id="orgheadline4"></a>

`/Lao Zi`

这样我们就开始搜索精确匹配含有“Lao Zi”这个字符串了，如果你按 

`n`

那么就是继续查找“Lao Zi”，也就是查找下一个

## 查找历史<a id="orgheadline5"></a>

如果输入 / 然后按方向键，就如同我们在终端上直接按方向键可以调用上一个命令一样，现在我们可以调用上一次的查找命令。这个有时很有用的。

## 反向查找<a id="orgheadline6"></a>

使用问号 `?` 什么就是反向查找。同样 `n` ，下一个也是反向的，你可以理解n是将上一次的查找命令重做一次。

## 锚定行的开始<a id="orgheadline7"></a>

`^` 符号表示一行的开始。现在我们执行如下查找命令：

`/^Th`
这算是一个小型的正则表达式匹配模式了，用自然语言来描述就是：匹配以T为行首，后面还跟一个字母h的文本。我们看到一些The和This开头的行都匹配进去了，请读者试试 /^This 来精确匹配以T为行首，后面跟着字母his的文本。

## 锚定行的结尾<a id="orgheadline8"></a>

`$` 符号表示一行的结尾。现在让我们匹配以“之。”结尾的文本：

`/之。$`

我们看到这个例子只匹配行尾和行尾前面有“之。”这两个字符的文本。

## 匹配空行<a id="orgheadline9"></a>

空行的表示就是 `/^$` 。这样将会匹配每一条没有任何字符的空行。

# vimrc配置<a id="orgheadline15"></a>

在当前用户主文件夹下的 `.vimrc` 文件里面可以进行一些vi编辑器的定制配置。

## 解决Backspace键乱码和方向键乱码<a id="orgheadline11"></a>

    set nocompatible 
    set backspace=2

## 自动缩进<a id="orgheadline12"></a>

    set autoindent

## 设置行号<a id="orgheadline13"></a>

    set nu

## 开启语法高亮<a id="orgheadline14"></a>

    syntax on