<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 简介</a></li>
<li><a href="#orgheadline8">2. 背景图片设置</a>
<ul>
<li><a href="#orgheadline2">2.1. 设置背景图片</a></li>
<li><a href="#orgheadline3">2.2. 设置背景图片位置</a></li>
<li><a href="#orgheadline4">2.3. 设置背景图片是否重复</a></li>
<li><a href="#orgheadline5">2.4. 设置背景图片不随页面滚动</a></li>
<li><a href="#orgheadline6">2.5. 设置背景图片尺寸</a></li>
<li><a href="#orgheadline7">2.6. 设置背景颜色</a></li>
</ul>
</li>
<li><a href="#orgheadline9">3. 控制文本大小写</a></li>
<li><a href="#orgheadline10">4. 控制文本对齐方式</a></li>
<li><a href="#orgheadline11">5. 边框画一个圆</a></li>
<li><a href="#orgheadline12">6. z-index属性</a></li>
<li><a href="#orgheadline20">7. 表单</a>
<ul>
<li><a href="#orgheadline13">7.1. 单行文本输入</a></li>
<li><a href="#orgheadline14">7.2. 多行文本输入</a></li>
<li><a href="#orgheadline15">7.3. 按钮</a></li>
<li><a href="#orgheadline16">7.4. required属性</a></li>
<li><a href="#orgheadline17">7.5. 单选按钮</a></li>
<li><a href="#orgheadline18">7.6. 复选按钮</a></li>
<li><a href="#orgheadline19">7.7. 其他type类型</a></li>
</ul>
</li>
<li><a href="#orgheadline26">8. bootstrap简介</a>
<ul>
<li><a href="#orgheadline21">8.1. 安装js脚本</a></li>
<li><a href="#orgheadline22">8.2. viewport元数据声明</a></li>
<li><a href="#orgheadline23">8.3. container类</a></li>
<li><a href="#orgheadline24">8.4. 栅格系统</a></li>
<li><a href="#orgheadline25">8.5. 其他常规css设置</a></li>
</ul>
</li>
<li><a href="#orgheadline27">9. lead盒子</a></li>
<li><a href="#orgheadline28">10. jumbotron盒子</a></li>
<li><a href="#orgheadline29">11. thumbnail盒子</a></li>
<li><a href="#orgheadline30">12. bootstrap的表单</a></li>
<li><a href="#orgheadline31">13. pull-left和pull-right</a></li>
<li><a href="#orgheadline33">14. tabs的制作</a>
<ul>
<li><a href="#orgheadline32">14.1. pill形状tabs制作</a></li>
</ul>
</li>
<li><a href="#orgheadline34">15. 如何制作一个 <code>Bootstrap</code> 风格的带链接的按钮</a></li>
<li><a href="#orgheadline35">16. 参考资料</a></li>
</ul>
</div>
</nav>


# 简介<a id="orgheadline1"></a>

本文将在 [html5入门](html5入门.html) 一文的基础上，进一步深入学习html5前端知识。

# 背景图片设置<a id="orgheadline8"></a>

## 设置背景图片<a id="orgheadline2"></a>

    background-image:url("https://theurl/tothe/image.jpg");

## 设置背景图片位置<a id="orgheadline3"></a>

设置背景图片位置，可能的值有top，center，right，left，top，bottom等，如下所示:

    top left
    top center
    top right
    center left
    center center
    center right
    bottom left
    bottom center
    bottom right

如果只给出一个值，则第二个值是默认值center。

    background-position: center center;

## 设置背景图片是否重复<a id="orgheadline4"></a>

默认是repeat，如下设置为 `no-repeat` ，则背景图片不会重复以铺满整个背景了。

    background-repeat: no-repeat;

## 设置背景图片不随页面滚动<a id="orgheadline5"></a>

    background-attachment:fixed;

## 设置背景图片尺寸<a id="orgheadline6"></a>

如下设置为 `cover` ，则背景图片会拉伸到足够大，以覆盖整个区域，图片某些部位可能不会显示在背景中。

    background-size: cover;

如果设置为 `contain` ，则背景图片会拉伸至最大长度或最大宽度不超过背景为止。

此外还可以如下指定宽高比，下面是宽100px，高150px: 

    background-size:100px 150px;

## 设置背景颜色<a id="orgheadline7"></a>

这里是html各个标签盒子的背景颜色，而color设置的是里面字体的颜色。

    background-color:red;

# 控制文本大小写<a id="orgheadline9"></a>

如下所示，依次为: 大写，首字母大写，小写。

    h1 {text-transform:uppercase}
    h2 {text-transform:capitalize}
    p {text-transform:lowercase}

bootstrap提供了 `text-lowercase` , `text-uppercase` , `text-capitalize` class:

    <p class="text-lowercase">HELLO world</p>
    <p class="text-uppercase">hello world</p>
    <p class="text-capitalize">hello world</p>

<p class="text-lowercase">HELLO world</p>
<p class="text-uppercase">hello world</p>
<p class="text-capitalize">hello world</p>

# 控制文本对齐方式<a id="orgheadline10"></a>

主要作用于p段落盒子的属性支持: <strong>text-left</strong> ,  <strong>text-center</strong> ,  <strong>text-right</strong> ,  <strong>text-justify</strong> , <strong>text-nowrap</strong> 。

具体这些css都很简单:
<pre class="pre-scrollable">
    .text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
</pre>

# 边框画一个圆<a id="orgheadline11"></a>

这样边框就成为一个圆了。

    border-radius:50%;

    <div style="border:1pt solid blue;border-radius:50%;width:100px;height:100px;margin:auto;"></div>

<div style="border:1pt solid blue;border-radius:50%;width:100px;height:100px;margin:auto;"></div>

# z-index属性<a id="orgheadline12"></a>

css中某个标签盒子设置z-index属性，将影响这些标签盒子的堆叠顺序。比如说如下将header标签的 `z-index` 属性设置为1，而其他的都不设置，则保证header网页头部分总是第一个先堆放。:

    header{
        z-index:1;
    }

# 表单<a id="orgheadline20"></a>

之前并没有对html中的表单各个情况进行说明，这里详细说明之。这里所谓的表单是指 `form` 标签加上其内包含的 `input` 等元素。这些input元素构成了我们熟知的文本输入框，下拉列表，单选框，复选框等等。

    <form>
        <input>    </input>
    </form>

具体表单元素的类型由input标签的 `type` 元素定义，下面分别详细说明之:

## 单行文本输入<a id="orgheadline13"></a>

单行文本输入用input标签，type类型为 `text` ，然后具体说明文字推荐用 `label` 标签。

```html
&lt;form&gt;
&lt;label&gt;name:&lt;/label&gt;
&lt;input type="text" name="yourname"&gt;&lt;/input&gt;
&lt;/form&gt;
```

然后input的 `name` 属性很重要，其值具体对应该文本输入的值的变量名（比如python的wsgi机制就将其刷成 `form.yourname` 这样的引用）。 

<form>
<label>name:</label>
<input type="text" name="yourname"></input>
</form>

## 多行文本输入<a id="orgheadline14"></a>

多行文本输入使用 `textarea` 标签生成的，现在先简单了解下即可。

```html
&lt;p&gt;:before&lt;/p&gt;

&lt;textarea rows="5"&gt;
the textarea you say something
&lt;/textarea&gt;

&lt;p&gt;:after&lt;/p&gt;
```

<p>:before</p>

<textarea rows="5">
the textarea you say something
</textarea>

<p>:after</p>

## 按钮<a id="orgheadline15"></a>

html有好几种方法创建一个按钮，w3school不推荐button标签，然后如下a标签里面加上input标签type为button的风格我也不太喜欢。

    <a href="https://www.google.com">
    <input type="button" value="click to google"></input>
    </a>

而如上面所示的input标签type为button的只是输出一个标签，并不支持额外的行为，这和我们通常意义上理解的按钮作用有点初入，所以我更喜欢用input标签然后type为 `submit` 来创建一个按钮。如下所示:

```html
&lt;form action="https://www.google.com" method="get"&gt;
&lt;input type="submit" value="click to google"&gt;&lt;/input&gt;
&lt;/form&gt;
```

<form action="https://www.google.com" method="get">
<input type="submit" value="click to google"></input>
</form>

其 `value` 属性定义了具体按钮上显示的文字。然后具体跳转行为用form标签的 `action` 属性来定义，你还可以定义 `method` 属性来具体定义HTTP的method，比如下面是一个表单提交的例子:

```html
&lt;form action="http://httpbin.org/post" method="post"&gt;
    &lt;label&gt;name:&lt;/label&gt;
    &lt;input type="text" name="name" /&gt;
    &lt;label&gt;password:&lt;/label&gt;
    &lt;input type="password" name="password" /&gt;
    &lt;input type="submit" value="提交" /&gt;
&lt;/form&gt;
```

<form action="http://httpbin.org/post" method="post">
    <label>name:</label>
    <input type="text" name="name" />
    <label>password:</label>
    <input type="password" name="password" />
    <input type="submit" value="提交" />
</form>

然后我们注意到上面还出现了一个新的type类型 `password` ，其类似单行文本输入，不同的是你是在输入密码，所以不会在屏幕上显示出来。

## required属性<a id="orgheadline16"></a>

上面的input标签元素你还可以如下所示设置 `required` 属性好让这个输入是必须填上某个信息的。

    <input type="text" name="name" required="required"/>

## 单选按钮<a id="orgheadline17"></a>

```html
&lt;form action="http://httpbin.org/get" method="get"&gt;
    &lt;label&gt;Male&lt;/label&gt; 
    &lt;input type="radio" name="Sex" value="Male" checked="checked" /&gt;
    &lt;label&gt;Female&lt;/label&gt; 
    &lt;input type="radio" name="Sex" value="Female" /&gt;
    &lt;input type ="submit" value ="提交"&gt;
&lt;/form&gt;
```

<form action="http://httpbin.org/get" method="get">
    <label>Male</label> 
    <input type="radio" name="Sex" value="Male" checked="checked" />
    <label>Female</label> 
    <input type="radio" name="Sex" value="Female" />
    <input type ="submit" value ="提交">
</form> 

上面新出现的 `checked` ，默认单选按钮和下面的复选按钮是没有选中的，而设置成为 "checked" 则默认为选中了。

## 复选按钮<a id="orgheadline18"></a>

```html
&lt;form action="http://httpbin.org/get" method="get"&gt;
    &lt;p&gt;你喜欢吃的水果:&lt;/p&gt;
    &lt;label&gt;apple&lt;/label&gt;&lt;input type="checkbox" name="fruits" value="apple"/&gt;
    &lt;label&gt;banana&lt;/label&gt;&lt;input type="checkbox" name="fruits" value="banana" /&gt;
    &lt;label&gt;pear&lt;/label&gt;&lt;input type="checkbox" name="fruits" value="pear" /&gt;
    &lt;input type="submit" value="提交" /&gt;
&lt;/form&gt;
```

<form action="http://httpbin.org/get" method="get">
    <p>你喜欢吃的水果:</p>
    <label>apple</label><input type="checkbox" name="fruits" value="apple"/>
    <label>banana</label><input type="checkbox" name="fruits" value="banana" />
    <label>pear</label><input type="checkbox" name="fruits" value="pear" />
    <input type="submit" value="提交" />
</form> 

## 其他type类型<a id="orgheadline19"></a>

-   **file:** 选择文件按钮
-   **image:** 

---

下面是html5新加的type类型:

-   email
-   url
-   number
-   range
-   Date pickers (date, month, week, time, datetime, datetime-local)
-   search
-   color

# bootstrap简介<a id="orgheadline26"></a>

bootstrap是一个非常流行的前端开发框架，其实就是一些预先定义好的css文件和js文件和部分资源文件。可以直接下载源码之后加载到html文件里面。一开始我更喜欢这种方式，这样刚开始不用费心什么其他的配置和方便阅读源码。

大致结构如下所示:

    ├── css
    │   ├── bootstrap.css
    │   ├── bootstrap.css.map
    │   ├── bootstrap.min.css
    │   ├── bootstrap-theme.css
    │   ├── bootstrap-theme.css.map
    │   └── bootstrap-theme.min.css
    ├── fonts
    │   ├── glyphicons-halflings-regular.eot
    │   ├── glyphicons-halflings-regular.svg
    │   ├── glyphicons-halflings-regular.ttf
    │   ├── glyphicons-halflings-regular.woff
    │   └── glyphicons-halflings-regular.woff2
    └── js
        ├── bootstrap.js
        ├── bootstrap.min.js
        └── npm.js

其中 `.map` 文件有其他用途，这里先不管。所以我们主要看的目前就是这三个文件:

-   bootstrap.css
-   bootstrap-theme.css
-   bootstrap.js

然后具体加载使用最好用那个什么 `.min.` 什么的文件，这样加载速度更快。具体本地使用的话如下所示:

    <link rel="stylesheet" type="text/css" href="thepath/to/bootstrap.min.css" />

## 安装js脚本<a id="orgheadline21"></a>

bootstrap的javascript脚本依赖于jquery，这里先把jquery安装简单说一下，这里是jquery的 [官网下载链接](http://jquery.com/download/) ，就下载那个 `jquery.min.js` 单js文件即可（版本号的话一般选一点几的，二点几的区别就是取消支持IE6IE8之类的了）。然后在本网页body标签最末尾加载:

    <script scr="js/jquery.min.js"></script>

然后在安装bootstrap自身的javascript脚本:

    <script scr="js/bootstrap.min.js"></script>

## viewport元数据声明<a id="orgheadline22"></a>

为了确保适当的绘制和触屏缩放，需要加上如下viewport元数据声明:

    <meta name="viewport" content="width=device-width, initial-scale=1" />

## container类<a id="orgheadline23"></a>

通过container class的 `div` 来获得一个固定宽度的响应式容器。

    <div class="container" style="background:#FFF0F5">
    我在container类里面。
    </div>

<div class="container" style="background:#FFF0F5">
我在container类里面。
</div>

此外还有一个 `container-fluid` class，区别就是container类会根据当前设备的尺寸来自动调整自身大小。一般推荐页面的某部分都应该被包围在container盒子里面。

## 栅格系统<a id="orgheadline24"></a>

栅格系统是bootstrap框架里面很有用的一个特性了，其基本思路如下:

1.  每一行 `row` 类都放在上面谈及的 `container` 类里面。
2.  然后在每一行row类里面（这里所谓的什么类实际上就是该类属性的div盒子）再添加行类。

具体行类有很多种，请参看 [这个网页](http://getbootstrap.com/examples/grid/) 和官方文档的 [这里](http://getbootstrap.com/css/#grid) 来具体设计之。

```html
&lt;div class="container" style="background:#FFF0F5"&gt;
我在container类里面。
&lt;div class="row" style="background-color:yellow"&gt;
&lt;div class="col-md-8" style="background-color:red"&gt;
  我在col-md-8盒子里面，黄色是row盒子。
&lt;/div&gt;
&lt;div class="col-md-4" style="background-color:blue"&gt;
我在col-md-4盒子里面，8+4=12，bootstrap最多12列。
&lt;/div&gt;
&lt;/div&gt;
&lt;/div&gt;
```

<div class="container" style="background:#FFF0F5">
我在container类里面。
<div class="row" style="background-color:yellow">
<div class="col-md-8" style="background-color:red">
  我在col-md-8盒子里面，黄色是row盒子。
</div>
<div class="col-md-4" style="background-color:blue">
我在col-md-4盒子里面，8+4=12，bootstrap最多12列。
</div>
</div>
</div>

## 其他常规css设置<a id="orgheadline25"></a>

其他常规css设置比如说h1-h6字体大小啊，等等其他常规标签的字体大小啊颜色啊代码背景的设置啊等等，这些都可以通过浏览器的开发者工具来查看具体的css代码设置，如果觉得默认设置不好则另外再弄个css文件重载也是可以的，这些就不多说了。

bootstrap将全局font-size 设置为 14px，line-height 设置为 1.428。这些属性直接赋予 body元素和所有段落元素。另外，p（段落）元素还被设置了等于 1/2 行高（即 10px）的底部外边距（margin）。

# lead盒子<a id="orgheadline27"></a>

后面都如此约定，所谓的 **lead盒子** 是指class属性为lead的div标签，即:

    <div class="lead" >
        ...
    </div>

```html
&lt;div class="lead" style="border:1px solid"&gt;
hi ，我在lead盒子里面，边框是额外加上去的。可以用来作为某个特别重要的话的强调。
&lt;/div&gt;
```

<div class="lead" style="border:1px solid">
hi ，我在lead盒子里面，边框是额外加上去的。可以用来作为某个特别重要的话的强调。
</div>

# jumbotron盒子<a id="orgheadline28"></a>

bootstrap提供的jumbotron盒子一般在首页用于展示某个特别重要希望读者阅读的信息。

```html
&lt;div class="jumbotron"&gt;
&lt;p&gt;大家好，我在jumbotron盒子里面。&lt;/p&gt;
&lt;/div&gt;
```

<div class="jumbotron">
<p>大家好，我在jumbotron盒子里面。</p>
</div>

# thumbnail盒子<a id="orgheadline29"></a>

# bootstrap的表单<a id="orgheadline30"></a>

# pull-left和pull-right<a id="orgheadline31"></a>

bootstrap用这个class属性来左对齐或右对齐某个标签元素。

# tabs的制作<a id="orgheadline33"></a>

利用bootstrap制作tabs，就是建立一个ul无序列表，然后class属性设置为 **nav nav-tabs** ，这样就制作了一个简单的tabs了。

```html
&lt;ul class="nav nav-tabs"&gt;
  &lt;li class="active"&gt;&lt;a href="#"&gt;Features&lt;/a&gt;&lt;/li&gt;
  &lt;li&gt;&lt;a href="#"&gt;Details&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
```

<ul class="nav nav-tabs">
  <li class="active"><a href="#">Features</a></li>
  <li><a href="#">Details</a></li>
</ul>

## pill形状tabs制作<a id="orgheadline32"></a>

```html
&lt;ul class="nav nav-pills"&gt;
  &lt;li class="active"&gt;&lt;a href="#"&gt;Features&lt;/a&gt;&lt;/li&gt;
  &lt;li&gt;&lt;a href="#"&gt;Details&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
```

<ul class="nav nav-pills">
  <li class="active"><a href="#">Features</a></li>
  <li><a href="#">Details</a></li>
</ul>

<h3>list-inline属性</h3>
给ul或ol加上 <strong>list-inline</strong> 属性，来是li列表元素水平inline-block显示，如下所示:
<ul class="list-inline">
<li>第一个li</li>
<li>第二个li</li>
</ul>

<h3>kbd标签</h3>
kbd标签用来显示按键组合: <kbd>Ctrl+X</kbd>

<h3>pre-scrollable属性的pre</h3>
代码加上滚动条了，具体显示效果见上面。

<h3>表格</h3>
表格的类属性支持很多，这里就不多说了。具体看到 <a href="<http://v3.bootcss.com/css/#tables>">这里</a> 。

一些表单元素最好都放入<strong>form-group</strong>盒子里面。

<h4>form-inline属性的form</h4>
<strong>form-inline</strong>的form标签将使其内容左对齐，并具有<code>inline-block</code>的布局。但只适用于视口（viewport）至少在 768px 宽度时，再小表单就会折叠了。

# 如何制作一个 `Bootstrap` 风格的带链接的按钮<a id="orgheadline34"></a>

参看 [这个网页](http://stackoverflow.com/questions/19981949/how-to-make-a-button-in-bootstrap-look-like-a-normal-link-in-nav-tabs) 。

我更喜欢这种写法:

    <a href="{{ message["body"] }}" target="_blank"  role="button" class="btn btn-success btn-large">Click here!</a>

# 参考资料<a id="orgheadline35"></a>

1.  [w3school cn](http://www.w3school.com.cn/)
2.  [<https://www.codecademy.com>](https://www.codecademy.com)
3.  [这个网页](https://www.youtube.com/watch?v=2W03ZymI46g) 来学习如何本地安装bootstrap

<script scr="js/jquery.min.js"></script>
<script scr="js/bootstrap.min.js"></script>