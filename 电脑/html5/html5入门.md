<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline3">1. html的第一个模板</a>
<ul>
<li><a href="#orgheadline1">1.1. doctype声明</a></li>
<li><a href="#orgheadline2">1.2. 字符集设置为utf-8</a></li>
</ul>
</li>
<li><a href="#orgheadline7">2. 一个基本的html网页</a>
<ul>
<li><a href="#orgheadline4">2.1. 常用html标签清单</a></li>
<li><a href="#orgheadline5">2.2. 文字强调的html5规范</a></li>
<li><a href="#orgheadline6">2.3. 绝对路径和相对路径</a></li>
</ul>
</li>
<li><a href="#orgheadline19">3. 从html到css</a>
<ul>
<li><a href="#orgheadline8">3.1. 注释</a></li>
<li><a href="#orgheadline9">3.2. 有序列表里面带无序列表</a></li>
<li><a href="#orgheadline10">3.3. table</a></li>
<li><a href="#orgheadline11">3.4. div和span</a></li>
<li><a href="#orgheadline17">3.5. inline css</a>
<ul>
<li><a href="#orgheadline12">3.5.1. font-size</a></li>
<li><a href="#orgheadline13">3.5.2. color</a></li>
<li><a href="#orgheadline14">3.5.3. font-family</a></li>
<li><a href="#orgheadline15">3.5.4. background-color</a></li>
<li><a href="#orgheadline16">3.5.5. text-align</a></li>
</ul>
</li>
<li><a href="#orgheadline18">3.6. 外部css</a></li>
</ul>
</li>
<li><a href="#orgheadline44">4. css入门</a>
<ul>
<li><a href="#orgheadline25">4.1. css选择器</a>
<ul>
<li><a href="#orgheadline20">4.1.1. 多级选择</a></li>
<li><a href="#orgheadline21">4.1.2. 带上其他属性选择</a></li>
<li><a href="#orgheadline24">4.1.3. 伪类选定</a>
<ul>
<li><a href="#orgheadline22">4.1.3.1. first-child伪类</a></li>
<li><a href="#orgheadline23">4.1.3.2. nth-child伪类</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#orgheadline26">4.2. css的长度单位</a></li>
<li><a href="#orgheadline28">4.3. css的盒子模型</a>
<ul>
<li><a href="#orgheadline27">4.3.1. border属性</a></li>
</ul>
</li>
<li><a href="#orgheadline41">4.4. css布局</a>
<ul>
<li><a href="#orgheadline33">4.4.1. display属性</a>
<ul>
<li><a href="#orgheadline29">4.4.1.1. 块级元素</a></li>
<li><a href="#orgheadline30">4.4.1.2. inline元素</a></li>
<li><a href="#orgheadline31">4.4.1.3. inline-block</a></li>
<li><a href="#orgheadline32">4.4.1.4. none</a></li>
</ul>
</li>
<li><a href="#orgheadline34">4.4.2. float属性</a></li>
<li><a href="#orgheadline35">4.4.3. clear属性</a></li>
<li><a href="#orgheadline40">4.4.4. position属性</a>
<ul>
<li><a href="#orgheadline36">4.4.4.1. static</a></li>
<li><a href="#orgheadline37">4.4.4.2. relative</a></li>
<li><a href="#orgheadline38">4.4.4.3. fixed</a></li>
<li><a href="#orgheadline39">4.4.4.4. absolute</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#orgheadline42">4.5. 其他零零碎碎的css属性</a></li>
<li><a href="#orgheadline43">4.6. css框架</a></li>
</ul>
</li>
<li><a href="#orgheadline47">5. 附录</a>
<ul>
<li><a href="#orgheadline45">5.1. !important 用法</a></li>
<li><a href="#orgheadline46">5.2. 参考资料</a></li>
</ul>
</li>
</ul>
</div>
</nav>


# html的第一个模板<a id="orgheadline3"></a>

```html
&lt;!DOCTYPE html&gt;
&lt;html lang="zh"&gt;
    &lt;head&gt;
    &lt;meta charset="utf-8" /&gt;

    &lt;link rel="stylesheet"  href="templates/index.css"/&gt;

    &lt;title&gt;your awesome title&lt;/title&gt;

    &lt;/head&gt;


    &lt;body&gt;

    &lt;/body&gt;
&lt;/html&gt;
```

## doctype声明<a id="orgheadline1"></a>

现在html5的doctype声明非常简单了，开头加入如下简单一行即可:

    <!DOCTYPE html>

然后进入 **html** 标签，然后进入 **head** 标签，在head标签里面的内容不会显示在网页上，主要是一些关于本网页的配置信息。

## 字符集设置为utf-8<a id="orgheadline2"></a>

现在html5使用如下更简洁的语法了:

    <meta charset="utf-8" />

然后 **body** 标签里面存放这实际要显示的网页内容。

# 一个基本的html网页<a id="orgheadline7"></a>

```html
&lt;!DOCTYPE html&gt;
&lt;html lang="zh"&gt;
    &lt;head&gt;
    &lt;meta charset="utf-8"&gt;
    &lt;title&gt;basic html&lt;/title&gt;
    &lt;/head&gt;

    &lt;body&gt;
        &lt;nav&gt;
            &lt;ul&gt;
                &lt;li&gt;&lt;a href="#"&gt;Home&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#"&gt;About&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#"&gt;Products&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#"&gt;Contact Us&lt;/a&gt;&lt;/li&gt;
            &lt;/ul&gt;
        &lt;/nav&gt;

    &lt;header&gt;
        &lt;h1&gt;&lt;a href="#"&gt;Very Basic Document&lt;/a&gt;&lt;/h1&gt;
        &lt;h2&gt;A tag line might go here&lt;/h2&gt;
    &lt;/header&gt;

    &lt;section&gt;
        &lt;article&gt;
            &lt;h3&gt;&lt;a href="#"&gt;First Article Title&lt;/a&gt;&lt;/h3&gt;
            &lt;p&gt;Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. &lt;/p&gt;
        &lt;/article&gt;

        &lt;article&gt;
            &lt;h3&gt;&lt;a href="#"&gt;Second Article Title&lt;/a&gt;&lt;/h3&gt;
            &lt;p&gt;Praesent libero. Sed cursus ante dapibus diam.&lt;/p&gt;
            &lt;/article&gt;
        &lt;/section&gt;

        &lt;aside&gt;
            &lt;h4&gt;Connect With Us&lt;/h4&gt;
            &lt;ul&gt;
                &lt;li&gt;&lt;a href="#"&gt;Twitter&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#"&gt;Facebook&lt;/a&gt;&lt;/li&gt;
            &lt;/ul&gt;
        &lt;/aside&gt;

        &lt;footer&gt;
            &lt;p&gt;All rights reserved.&lt;/p&gt;
        &lt;/footer&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

html5新加入了很多关于文档结构的标签，这些标签并没有任何布局含义，相当于一个自带名字的div，也就是默认标签的意思。其主要作用就是html内容分组(group)。

下面是常用的这些标签含义，在实际使用中，应该尽量规范使用这些标签。

-   **header:** 一个网页总要有个头，推荐都使用这个标签。
-   **nav:** 一般是目录或者导航菜单。
-   **section:** 一般是本网页的主体信息部分或者主页面——类似于GUI的主要显示窗口。
-   **article:** section下面的某一独立内容部分。
-   **aside:** 和网页主体信息不太相关的其他信息。
-   **footer:** 一般是关于作者，版权或者其他比如脚注等信息。

这些都可以通过div然后class或者id写法来取代，在实际使用中如果上面的默认标签能够满足需求，那么就应该使用html5的这些默认标签。

上面的例子已经出现了一些标签，然后还有一些很常用的标签，下面承接上面所将的继续补充写一个常用html标签清单。

## 常用html标签清单<a id="orgheadline4"></a>

-   **ul:** 不编号列表，也叫无序列表（Unordered list）。里面的item用 **li** 标签封装。
-   **ol:** 编号列表，也叫有序列表（Ordered list）。里面的item用 **li** 标签封装。
-   **a:** 引用链接标签，其中常用的属性是 **href** ，指明具体的引用地址。
-   **h1,h2,h3&#x2026;:** 标题标签，数字表示各个标题的层级。
-   **p:** 段落标签。
-   **b:** 文字加粗
-   **i:** 文字斜体
-   **<br />:** 换行
-   **<hr />:** 水平线
-   **img:** 加入图片，其中最常用的属性是 **src** ，指明具体图片引用地址。

## 文字强调的html5规范<a id="orgheadline5"></a>

按照html5提出的规范，并不推荐用<b>标签作为文字的强调用途（我一般使用的文字加粗是那个词提醒读者这个词需要特别记忆）。其推荐的是<em>标签作为一级强调，然后<strong>标签作为更进一步的强调。在默认样式中，<em>是斜体，然后<strong>是粗体。显然html5的意思是将表达文字的样式这样的标签<b><i>尽可能不用直到废弃，然后对于文字强调都推荐使用<em>和<strong>标签。其设计思路是html完全成为一个描述文档内容结构的标签系统，而不带有任何内容表现形式的东西。还是推荐按照html5规范来，少用<b>标签和<i>标签。请参看 [这个网页](http://stackoverflow.com/questions/271743/whats-the-difference-between-b-and-strong-i-and-em) 的讨论。

## 绝对路径和相对路径<a id="orgheadline6"></a>

# 从html到css<a id="orgheadline19"></a>

## 注释<a id="orgheadline8"></a>

```html
&lt;!-- Make me into a comment. --&gt;
```

## 有序列表里面带无序列表<a id="orgheadline9"></a>

就是把无序列表嵌套进去即可。

```html
&lt;ol&gt;
    &lt;li&gt;ol li1&lt;/li&gt;
    &lt;li&gt;ol li2&lt;/li&gt;
    &lt;ul&gt;
        &lt;li&gt;ul li1&lt;/li&gt;
        &lt;li&gt;ul li2&lt;/li&gt;
    &lt;/ul&gt;
&lt;/ol&gt;
```

## table<a id="orgheadline10"></a>

table表格有时也可用于布局，不过不推荐这种风格，因为html标签应该尽可能是文本结构层而非表现形式层。一个完整的table模板如下所示:

```html
&lt;table&gt;
&lt;caption&gt;表格的标题用caption标签&lt;/caption&gt;
&lt;thead&gt;
&lt;tr&gt;&lt;th&gt;标签&lt;/th&gt;&lt;th&gt;fullname&lt;/th&gt;&lt;th&gt;说明&lt;/th&gt;&lt;/tr&gt;
&lt;/thead&gt;
&lt;tbody&gt;
&lt;tr&gt;&lt;td&gt;tr&lt;/td&gt;&lt;td&gt;table row&lt;/td&gt;&lt;td&gt;表格中的一行&lt;/td&gt;&lt;/tr&gt;
&lt;tr&gt;&lt;td&gt;th&lt;/td&gt;&lt;td&gt;table head&lt;/td&gt;&lt;td&gt;表格的列名&lt;/td&gt;&lt;/tr&gt;
&lt;tr&gt;&lt;td&gt;td&lt;/td&gt;&lt;td&gt;table data&lt;/td&gt;&lt;td&gt;表格具体要展示的数据&lt;/td&gt;&lt;/tr&gt;
&lt;/tbody&gt;
&lt;/table&gt;
```

<table>
<caption>表格的标题用caption标签</caption>
<thead>
<tr><th>标签</th><th>fullname</th><th>说明</th></tr>
</thead>
<tbody>
<tr><td>tr</td><td>table row</td><td>表格中的一行</td></tr>
<tr><td>th</td><td>table head</td><td>表格的列名</td></tr>
<tr><td>td</td><td>table data</td><td>表格具体要展示的数据</td></tr>
</tbody>
</table>

这里的三线表样式使用下面的简单css配置完成的:

```css
table{
    border-top: 2px solid ;
    border-bottom: 2px solid ;
}
thead{
    border-bottom: 1px solid ;
}
```

大体在html上画表格就如上所示了，其他一些更漂亮的表格制作都是通过css来完成的，这里先略过了。

## div和span<a id="orgheadline11"></a>

div（division）在html标记语言中主要是区块的意思。我们知道html页面要显示的元素就好比一个个盒子逐步排布下来，而 `div` 可以看作一个这样自定义的盒子。html中有两种显示风格的盒子，一种是块状区块，比如p段落标签；还有一种是inline盒子，比如说em标签，其不会换行。

div标签更确切的表达是块状区块，可以看作其display属性是 `block` （但不一定，不过推荐接受这样的设定）；此外还有所谓的inline区块，用 `span` 标签来表示这样的元素，可以理解为改标签元素的display属性是 `inline` 。

## inline css<a id="orgheadline17"></a>

最基本的css属性可以通过inline css模式直接在html标签中通过 **style** 属性来加上。

### font-size<a id="orgheadline12"></a>

字体大小

```html
&lt;p style="font-size:12pt"&gt;paragraph&lt;/p&gt;
```

### color<a id="orgheadline13"></a>

字体颜色， 这是css支持的 [color关键词清单](http://www.w3.org/TR/css3-color/#svg-color) 。

```html
&lt;h2 style="color:green"&gt;paragraph&lt;/h2&gt;
```

### font-family<a id="orgheadline14"></a>

字族， 这是css一般支持的 [字族信息](http://www.w3.org/TR/CSS21/fonts.html#generic-font-families) 。

```html
&lt;ol&gt;
    &lt;li style="font-family:Arial"&gt;Arial&lt;/li&gt;
&lt;/ol&gt;
```

一般有文字的标签都可以用上面的三个属性来控制其内文字的大小，颜色和字族。虽然现在都推荐用css来控制，但思路顺序应该是优先inline css，太过普遍多次出现的情况下才考虑单独css控制。

### background-color<a id="orgheadline15"></a>

背景颜色。如果读者熟悉LaTeX排版系统的，那么我们都清楚LaTeX排版很核心的一个概念就是盒子。在html这里，我们似乎也可以把一个个标签看作一个个排版用的盒子。然后这里的background-color就是控制这一个盒子的背景颜色。

```html
&lt;body style="background-color:yellow"&gt;
&lt;/body&gt;
```

### text-align<a id="orgheadline16"></a>

文字在标签盒子里的对齐方式。可选参数有: left, right, center。

```html
&lt;h3 style="text-align:center"&gt;居中对齐的标题&lt;/h3&gt;
```

## 外部css<a id="orgheadline18"></a>

有一种说法，是将放在html <head> 标签里面的css和具体外部的css文件引用区分开来，在我看来区别不大吧。然后网络上还有一种说法认为html <head> 标签里面应该多用id的css定义，而外部css文件应该只用class定义好做到普适性，在我看来也有点削足适履了。额，目前的国内网络环境大家都懂的，所以我喜欢少用css文件引用，尽量将一些css定义都放在 <head> 标签里面，就是为了加载快一点，至于其他，倒没什么特别好讲究的。不过在使用css定义前应该用class，只有觉得某些元素需要个别处理的时候才用id属性控制，我想这是没有问题的。

放在<head>标签里面的css大致如下格式引入进来:

```html
&lt;style type="text/css"&gt;
这里的格式和外部css文件格式完全一致
&lt;/style&gt;
```

引入外部文件css如下:

```html
&lt;link rel="stylesheet"  href="main.css"/&gt;
```

然后在外部css文件里面你还可以如下进一步引用其他的css文件:

```css
@import url("http://getbootstrap.com/dist/css/bootstrap.min.css");
```

这种引用语句后面的分号不太清楚是不是必须的，不太关心这个，没事就加上吧。参考了 [这个网页](http://stackoverflow.com/questions/147500/is-it-possible-to-include-one-css-file-in-another) 。

# css入门<a id="orgheadline44"></a>

前面谈到的inline css因为肯定是作用于本标签，所以写法就简化了，style引入之后后面加入一些属性即可。然后前面谈到的外部css，其写法都是如下所示:

```css
p{
    text-indent:2em;/*段落缩进*/
    line-height:180%;/*行间距*/
    }
```

第一个元素我们可以简单称之为css选择器，在网络抓取中也有类似的概念。然后花括号里面就是类似 inline css 一样的格式了，用分号隔开，换行不换行都是无所谓的，具体为了美观一般都一个属性占一行吧。

## css选择器<a id="orgheadline25"></a>

这里以html5为例，html5内置的标签都是可以直接引用的，比如body，article，video，table，figure等等。如果你在css中引用section，那么意思就是整个文档的section标签那些元素被选中了。

我们知道html5中可以通过 **class** 属性来将某个元素归于某一类，现在假设有:

    <p class="emph">hello</p>

那么我们使用 `p.emph` 其意思就是将选中p标签然后class属性为emph的那些标签。

我们在css中经常看到这样的形式：

```html
.hightlight
```

其完整形式为 `*.hightlight` ，也就是所有class属性为hightlight的元素都将被选中。

然后id属性可用来定义某个标签的唯一id，一般就用 `#idname` 选中那个标签即可。

### 多级选择<a id="orgheadline20"></a>

在前面选择标签的基础上，加个空格继续写上其他标签就成了多级选择的意思了。也就是前一选择的标签之下（结构包含关系）的某个标签。比如 `figure p` 其选择的就是所有figure标签元素里面的p标签元素。前面谈及的那些标签元素表示方法你都可以用的，比如 `#footer .emph` 选择的就是id为footer的那个标签里面class属性为emph的标签。

此外还有一种更为严格的多级选择（可以称之为逐级选择）， 比如 `h1 > strong` ，其只严格选择h1标签下strong标签，这里的下是严格意义上的父子标签包含关系的下，如果某个strong标签在em标签里面，然后这个em标签在h1标签里面，则该strong元素是不会被这里所谓的严格逐级选择选中的。

更多css选择信息请参看w3school的 [css元素选择详解部分](http://www.w3school.com.cn/css/css_selector_type.asp) ，但这一块最好不要弄得太复杂。实际上这样的选择逻辑弄得越复杂后面css代码的维护就越困难，最好的实践还是用 **class** 和 **id** 来管理各个css属性。

### 带上其他属性选择<a id="orgheadline21"></a>

有href属性的a标签才应用样式:

    a[href] {color:red;}

有href属性和title属性的a标签才应用样式:

    a[href][title] {color:red;}

具体属性是什么值也指定了:

    a[href="http://www.w3school.com.cn/about_us.asp"] {color: red;}

### 伪类选定<a id="orgheadline24"></a>

带个:冒号后面跟着该标签的伪类，主要是值该标签的某种特殊状态，最常见的是a标签的各个状态，如下所示:

    a:link {color: #FF0000}         /* 未访问的链接 */
    a:visited {color: #00FF00}      /* 已访问的链接 */
    a:hover {color: #FF00FF}        /* 鼠标移动到链接上 */
    a:active {color: #0000FF}       /* 选定的链接 */

#### first-child伪类<a id="orgheadline22"></a>

    p:first-child {
        color: red;
    }

只有是父标签的第一个子标签元素才会被选定。

#### nth-child伪类<a id="orgheadline23"></a>

    p:nth-child(2) {
        color: red;
    }

是父标签的第几个子标签元素才会被选定。

## css的长度单位<a id="orgheadline26"></a>

css有很多长度单位，这些单位如果你熟悉 \(\LaTeX\) 的话你就会对这些单位很眼熟。其中绝对长度单位有：1in = 2.54cm = 25.4mm = 72pt = 6pc ，这些并不推荐使用。[这篇网页](http://www.w3.org/Style/Examples/007/units.en.html) 推荐多使用 `px` ， `em` 和 `%` 这样的长度单位。其中"px"和"%"是css特有的，其会根据显示屏而变动，然后1em我们知道就是当前字体M的宽度（TeX里面的情况）。其中px值得引起我们的注意，其会根据显示设备而有很好的调整，更多信息请参看上面提到的那个参考网页。

## css的盒子模型<a id="orgheadline28"></a>

html的显示布局和 \(TeX\) 的显示布局一样也是采用的浮动盒子模型，从上到下，从左到右，一个个盒子排下来，只是 \(TeX\) 更复杂，还有一个分页算法。简言之就是每一个标签元素都是一个盒子<sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup> 。

下面这个图片来自 [这个网页](http://www.hicksdesign.co.uk/boxmodel/) 。

![img](images/html_box_model.png "html\_box\_model")

[这篇文章](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model/Introduction_to_the_CSS_box_model) 讲解得很好，下面简要介绍之，下面放在短代码环境的都是可以用作css属性的。盒子最中心的是content区域，如果该盒子的 `box-sizing` 是默认值的话，那么 `width` 控制的就是content区域的宽度。如果将 `box-sizing` 设置为 `border-box` ，那么 `width` 对应的就是整个盒子的宽度。这个只是一点简单的数学加减法把戏罢了，没什么大不了的。

然后类似的 `height` 默认是控制content区域的高度，然后有 `min-width` , `min-height` 来控制盒子content区域的最小宽度和最小高度，然后有 `max-width` , `max-height` 来控制盒子content区域的最大宽度和最大高度，类似的这几个属性如果 `box-sizing` 设置为 `border-box` ，那么对应的都是整个盒子的宽度或高度。

content区域外围是padding区域，padding区域是透明的，如果整个盒子设置 `background-color` 或 `backgroud-image` ，这是你会看到他们。padding区域有如下属性来控制上面下面左边右边的长度: `padding-top` , `padding-bottom` , `padding-left` , `padding-right` 。 还有一个简便的写法 `padding` ，这种写法设置一个值控制上面四个量还是很方便的，但其还可以接多个值，有一定顺序，不太喜欢这种用法。

padding区域外面是border区域，通常我们在网页中看到的一条条边框线就是它了， 用 `border-width` 来控制边框线的宽度。这实际上是一个简写，类似上面的 `padding` ，可以跟四个值:

上，右，下，左:

    border-width: 1px 2em 0 4rem;

或者三个值:

上，右和左，下:

    border-width: 1px 2em 1.5cm;

或者两个值:

上下，左右:

    border-width: 2px 1.5em;

此外还有: `border-top-width` 对应上宽度， `border-bottom-width` 等。

border区域外面就是margin边距区域。其有如下属性，含义大家一看应该就明白了: `margin-top` , `margin-bottom` , `margin-left` , `margin-right` , `margin` 。

### border属性<a id="orgheadline27"></a>

border属性可以跟上三个值，分别是: border-width border-style border-color

    img {
    border: 1px solid #4682b4
    }

border-style情况比较多，常见的有 **solid** 实线 **dashed** 虚线 **double** 双线 **dotted** 点线等，更多请参看 [这个网页](http://www.w3school.com.cn/cssref/pr_border-style.asp) 。

## css布局<a id="orgheadline41"></a>

这个网站专门介绍 [css布局](http://zh.learnlayout.com/) ，深入浅出讲的还是很好的，css布局是css里面很重要的课题，建立认真学习一下。

### display属性<a id="orgheadline33"></a>

#### 块级元素<a id="orgheadline29"></a>

块级元素，占满自身右边所有行的行空间。 div元素和p默认就是所谓的block元素，display属性为 **block** 。

    display:block;

#### inline元素<a id="orgheadline30"></a>

span元素默认是 **inline** 。

    display:inline;

就占据我需要的宽度，其他盒子元素可以继续填满这一行。

比如:

    li{
        display:inline;
    }

这样你的无序列表和有序列表的各个item不会另起一行了。其默认的是 `display:list-item;` 。

#### inline-block<a id="orgheadline31"></a>

inline-block的意思是块级元素还是块级元素，只是几个块级元素对外排布是 inline 模式排布的，这是css较新的一个特性。如果对块状元素设置display属性为 **inline** ，则这些块状元素都会失去自己内部的尺寸布局，这可能不是你想要的。

#### none<a id="orgheadline32"></a>

    display:none

该元素不会显示。和 `visibility:hidden` 的区别是其本该显示的空间不会保留了。

### float属性<a id="orgheadline34"></a>

元素居右放置

    float:right;

### clear属性<a id="orgheadline35"></a>

两侧都不能出现浮动元素

    clear:both;

### position属性<a id="orgheadline40"></a>

css布局控制中，positon是一个很关键的属性。参考了 [这个网页](http://zh.learnlayout.com/position.html) 和 [这个网页](http://www.cnblogs.com/polk6/p/3214847.html) 。position属性有如下四个值可以设置:

#### static<a id="orgheadline36"></a>

static是默认值，没有什么其他额外的位置调整行为，表示它不会被"positioned"。

#### relative<a id="orgheadline37"></a>

relative和static类似，除非你还有其他的属性设置。比如 `top` , `right` , `bottom` , `left` 这些属性来调整，具体相对的含义是相对于原本它应该在的地方。相对调整之后留下来的地方会被保留下来，没有后续处理动作了。

#### fixed<a id="orgheadline38"></a>

fixed的应用就是将某个元素总是显示在页面上，比如说某些弹窗广告。  `top` , `right` , `bottom` , `left` 这些属性可以辅助来调整这个弹窗具体的位置。

#### absolute<a id="orgheadline39"></a>

absolute类似于fixed，不过其不是相对于视窗固定，而是相对于页面固定。比如下面这个aside设置:

```html
aside {
    margin-left: -200px;
    width: 181px;
    position: absolute;
    background-color:#FDF6E3;
}
```

这个aside是个目录，就放在正文的左边的，如果不用absolute布局的话，右边空间就不会释放出来。请参看 [这个网页的那个nav标签元素](http://zh.learnlayout.com/position-example.html) 。

## 其他零零碎碎的css属性<a id="orgheadline42"></a>

其他零零碎碎的css属性不建议初学者真的专门去学，在后面的探索过程中遇到了就查一下即可，一般 [w3school](http://www.w3school.com.cn/index.html) 网站上都会有的。

## css框架<a id="orgheadline43"></a>

再了解上面的概念基础上，实际开发还是要利用前人做出来的一些css框架，好做出更加美观和专业的网页。

-   Bootstrap似乎很流行评价也不错，有点重量级。
-   Pure在github上很流行，很轻量级，我似乎更加喜欢这个一点。

本文html5入门到此就告一段落吧。

# 附录<a id="orgheadline47"></a>

## !important 用法<a id="orgheadline45"></a>

css设置有时不可避免会发生样式重叠覆盖，当然一般是尽可能统一css设置，但有时嫌麻烦懒得弄了，你可以用 `!important` 来手工提高某个css设置的优先级<sup><a id="fnr.2" class="footref" href="#fn.2">2</a></sup>。如下所示：

```css
table, th, td
{
    margin:0 auto;
    min-width:2em;
    text-align:center !important ;
    padding: 5px;
}
```

上面严格控制表格各项都居中对齐。

## 参考资料<a id="orgheadline46"></a>

1.  [html.net](http://zh.html.net/) 网站提供的入门教程。
2.  [w3school](http://www.w3school.com.cn/index.html) 网站。

<div id="footnotes">
<h2 class="footnotes">Footnotes: </h2>
<div id="text-footnotes">

<div class="footdef"><sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> <div class="footpara">我还不太确定一个个字是不是一个盒子，在 \(TeX\) 里面一个个字都是一个盒子。</div></div>

<div class="footdef"><sup><a id="fn.2" class="footnum" href="#fnr.2">2</a></sup> <div class="footpara">参考了  [这个网页](http://www.cnblogs.com/qieqing/articles/1224085.html) 。</div></div>


</div>
</div>