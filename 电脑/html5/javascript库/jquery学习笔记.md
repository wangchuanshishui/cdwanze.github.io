<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. jquery选择语法</a></li>
<li><a href="#orgheadline2">2. 文档初始化之后执行的动作</a></li>
<li><a href="#orgheadline3">3. 获取屏幕的宽度和高度</a></li>
<li><a href="#orgheadline4">4. hide方法</a></li>
<li><a href="#orgheadline9">5. 给某个元素添加点击事件并绑定某个函数动作</a>
<ul>
<li><a href="#orgheadline5">5.1. 鼠标事件</a></li>
<li><a href="#orgheadline6">5.2. 键盘事件</a></li>
<li><a href="#orgheadline7">5.3. 其他事件</a></li>
<li><a href="#orgheadline8">5.4. 取消某个事件绑定</a></li>
</ul>
</li>
<li><a href="#orgheadline24">6. jquery的DOM操作</a>
<ul>
<li><a href="#orgheadline10">6.1. text方法</a></li>
<li><a href="#orgheadline11">6.2. html方法</a></li>
<li><a href="#orgheadline12">6.3. val方法</a></li>
<li><a href="#orgheadline13">6.4. attr方法</a></li>
<li><a href="#orgheadline14">6.5. removeAttr方法</a></li>
<li><a href="#orgheadline15">6.6. append方法</a></li>
<li><a href="#orgheadline16">6.7. prepend方法</a></li>
<li><a href="#orgheadline17">6.8. before方法</a></li>
<li><a href="#orgheadline18">6.9. after方法</a></li>
<li><a href="#orgheadline19">6.10. remove方法</a></li>
<li><a href="#orgheadline20">6.11. empty方法</a></li>
<li><a href="#orgheadline21">6.12. css方法</a></li>
<li><a href="#orgheadline22">6.13. 其他css操作方法</a></li>
<li><a href="#orgheadline23">6.14. 新建一个dom对象</a></li>
</ul>
</li>
<li><a href="#orgheadline27">7. ajax</a>
<ul>
<li><a href="#orgheadline25">7.1. GET</a></li>
<li><a href="#orgheadline26">7.2. POST</a></li>
</ul>
</li>
</ul>
</div>
</nav>


# jquery选择语法<a id="orgheadline1"></a>

jquery的选择语法和beautifulsoup的那种选择语法很是类似，这里不赘述了。唯一值得提醒的就是jquery这样:

    $(selector)

选择之后返回是一个数组类型。后面也许某些有特色的选择风格会加在下面。

# 文档初始化之后执行的动作<a id="orgheadline2"></a>

```js
$(document).ready(function(){

   // jQuery methods go here...

});
```

# 获取屏幕的宽度和高度<a id="orgheadline3"></a>

```js
var width = $(window).width()
var height = $(window).height()
```

这两个方法更确切的描述是返回所选元素的宽度或高度。此外还有 `innerWidth` 和 `innerHeight` 方法（包含内边距）， `outerWidth` 和 `outerHeight` 包含内边距和边框。

# hide方法<a id="orgheadline4"></a>

实际上就是css设置 `display:none` 。

```js
$('#test').hide()
```

这样将隐藏所有id为test的元素。

# 给某个元素添加点击事件并绑定某个函数动作<a id="orgheadline9"></a>

    $(selector).click(function)

类似的事件还有:

-   **dbclick:** 双击事件
-   **focus:** 焦点事件
-   **mousemove:** 鼠标悬停事件

## 鼠标事件<a id="orgheadline5"></a>

-   **click:** 鼠标单击时触发；
-   **dblclick:** 鼠标双击时触发；
-   **mouseenter:** 鼠标进入时触发；
-   **mouseleave:** 鼠标移出时触发；
-   **mousemove:** 鼠标在DOM内部移动时触发 （接受e ，e.pageX是鼠标x值，e.pageY是鼠标Y值）
-   **hover:** 鼠标进入和退出时触发两个函数，相当于mouseenter加上mouseleave。

## 键盘事件<a id="orgheadline6"></a>

键盘事件仅作用在当前焦点的DOM上，通常是<input>和<textarea>。

-   **keydown:** 键盘按下时触发；
-   **keyup:** 键盘松开时触发；
-   **keypress:** 按一次键后触发。

## 其他事件<a id="orgheadline7"></a>

focus：当DOM获得焦点时触发；
blur：当DOM失去焦点时触发；
change：当<input>、<select>或<textarea>的内容改变时触发；
submit：当<form>提交时触发；
ready：当页面被载入并且DOM树完成初始化后触发。

## 取消某个事件绑定<a id="orgheadline8"></a>

    a.off('click', hello);

# jquery的DOM操作<a id="orgheadline24"></a>

## text方法<a id="orgheadline10"></a>

返回所选元素的文本信息。如果选中了多个元素，所有的元素的字符串将合并。

设置字符串具体就是在 `text()` 方法里面，所有选中的元素的innerText都将更改。

## html方法<a id="orgheadline11"></a>

类似上面的text方法，包括HTML标记。

## val方法<a id="orgheadline12"></a>

是针对form 表单元素提取其value属性值或设置value值的。

## attr方法<a id="orgheadline13"></a>

获取某个元素的某个属性值。

设置值如下所示:

    $("button").click(function(){
      $("#w3s").attr("href","http://www.w3school.com.cn/jquery");
    });

## removeAttr方法<a id="orgheadline14"></a>

删除属性

    // <div id="test-div" name="Test" start="1">...</div>
    var div = $('#test-div');
    div.hasAttr('name'); // true
    div.attr('name'); // 'Test'
    div.attr('name', 'Hello'); // div的name属性变为'Hello'
    div.removeAttr('name'); // 删除name属性
    div.attr('name'); // undefined

## append方法<a id="orgheadline15"></a>

在所有被选中的元素末尾添加一个子节点元素

## prepend方法<a id="orgheadline16"></a>

在所有被选中的元素前面添加一个子节点。

## before方法<a id="orgheadline17"></a>

在所有被选中的元素之前（平行）添加某个节点

## after方法<a id="orgheadline18"></a>

在所有被选中的元素之后（平行）添加某个节点

## remove方法<a id="orgheadline19"></a>

删除选中的节点，包括子节点

## empty方法<a id="orgheadline20"></a>

删除选中的节点所有的子节点，选中的节点属性都还在。

## css方法<a id="orgheadline21"></a>

修改css属性

    $('#test-css li.dy>span').css('background-color', '#ffd351').css('color', 'red');

## 其他css操作方法<a id="orgheadline22"></a>

    var div = $('#test-div');
    div.hasClass('highlight'); // false， class是否包含highlight
    div.addClass('highlight'); // 添加highlight这个class
    div.removeClass('highlight'); // 删除highlight这个class

## 新建一个dom对象<a id="orgheadline23"></a>

这里参考了 [这个网页](http://stackoverflow.com/questions/759887/how-to-create-a-dom-node-as-an-object) ，样例如下: 

    var e = $("<ul><li><div class='bar'>bla</div></li></ul>");
    $('li', e).attr('id','a1234');  // set the attribute 
    $('body').append(e); // put it into the DOM

其中第一句是创建一个对应结构的dom元素，第二句也很重要，实际上可以取代find方法，也就是在对应的dom元素上执行进一步的查找操作。

# ajax<a id="orgheadline27"></a>

## GET<a id="orgheadline25"></a>

    $.get(URL, callback);

回调函数接受两个参数，传回来的data和状态码。

## POST<a id="orgheadline26"></a>

    $.post(URL,data,callback);