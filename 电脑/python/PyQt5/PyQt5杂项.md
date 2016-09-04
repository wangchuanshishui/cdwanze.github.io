<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. Qt程序的中文输入法</a></li>
<li><a href="#orgheadline2">2. QScintilla</a></li>
</ul>
</div>
</nav>

sudo apt-get remove appmenu-qt5

# Qt程序的中文输入法<a id="orgheadline1"></a>

我是在Ubuntu系统下，使用的是fcitx输入法，如果使用的是Qt5软件，那么是需要额外安装fcitx-frontend-qt5的。然后fcitx-frontend-qt4可能和fcitx-frontend-qt5冲突（？），不太确定，我之前两个都装了，并不能正常输入中文。后来删除qt4然后注销然后才可以。

# QScintilla<a id="orgheadline2"></a>

QScintilla是著名的开源编辑器组件的Qt实现，要快速开发出一个现代的编辑器，可不需要如上慢慢的自己手工编写各个功能了。

Scintilla特别适合编辑和debug代码，其具有如下功能：

\begin{itemize}
\item 语法高亮，支持70多种语言。
\item 错误指示。
\item 代码自动提示完成。
\item 调用函数的提示信息。
\item 代码折叠
\item 边界提示
\item 可记录宏
\item 多种视图
\item 打印支持
\end{itemize}

现在用QScintilla子模块来重构之前的项目。

1.setPlainText  改成 setText
2.isModified 前面不需要Document()了，也就是直接被QsciScintilla调用。
3.toPlainText 要改成text()
4.setModified 前面不需要Document()了。

sudo apt-get install python3-pyqt5.qsci