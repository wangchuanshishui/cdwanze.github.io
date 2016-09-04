<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 前言</a></li>
<li><a href="#orgheadline2">2. <code>no-js</code> class</a></li>
<li><a href="#orgheadline3">3. 强制IE浏览器用更高的可用模式渲染网页</a></li>
<li><a href="#orgheadline4">4. 设置viewport设置</a></li>
<li><a href="#orgheadline5">5. modernizr</a></li>
<li><a href="#orgheadline6">6. jquery</a></li>
<li><a href="#orgheadline7">7. Google Universal Analytics</a></li>
<li><a href="#orgheadline8">8. Normalize.css</a></li>
<li><a href="#orgheadline9">9. initializr</a></li>
</ul>
</div>
</nav>


# 前言<a id="orgheadline1"></a>

本文是由对 [html5-boilerplate](https://github.com/h5bp/html5-boilerplate) 这个项目代码的分析而来。

# `no-js` class<a id="orgheadline2"></a>

    <html class="no-js" lang="zh">

他们说这个class可以用来设置某些情况下javascript被禁用之后的css。

# 强制IE浏览器用更高的可用模式渲染网页<a id="orgheadline3"></a>

这个后续可能不需要考虑了。

    <meta http-equiv="x-ua-compatible" content="ie=edge">

# 设置viewport设置<a id="orgheadline4"></a>

这个在自适应布局中已经有所接触。

    <meta name="viewport" content="width=device-width, initial-scale=1">

# modernizr<a id="orgheadline5"></a>

这个需要放在head标签部分预先加载，因为其和网页具体显示的html5兼容性有关。

# jquery<a id="orgheadline6"></a>

这里代码的意思应该是先网络加载jquery，如果没有则本地找找看。

    <script src="https://code.jquery.com/jquery-{{JQUERY_VERSION}}.min.js"></script>
    <script>window.jQuery || document.write('<script src="js/vendor/jquery-{{JQUERY_VERSION}}.min.js"><\/script>')</script>

# Google Universal Analytics<a id="orgheadline7"></a>

关于google analytics的site id，了解更多，请点击 [这里](https://analytics.google.com/) 。

# Normalize.css<a id="orgheadline8"></a>

似乎bootstrap也是基于Normalize.css的。

# initializr<a id="orgheadline9"></a>

[initializr这个项目](http://www.initializr.com/) 很有意思，可以方便我们更快速地生成html5小应用蓝图。其还有bootstrap支持。