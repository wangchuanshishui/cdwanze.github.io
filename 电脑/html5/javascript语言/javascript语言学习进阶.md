<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline3">1. JSON对象</a>
<ul>
<li><a href="#orgheadline1">1.1. stringify函数</a></li>
<li><a href="#orgheadline2">1.2. parse函数</a></li>
</ul>
</li>
<li><a href="#orgheadline4">2. 用javascript改变网页全局的css设置</a></li>
<li><a href="#orgheadline5">3. 参考资料</a></li>
</ul>
</div>
</nav>


# JSON对象<a id="orgheadline3"></a>

json之前了解过一些了:

    number：和JavaScript的number完全一致；
    boolean：就是JavaScript的true或false；
    string：就是JavaScript的string；
    null：就是JavaScript的null；
    array：就是JavaScript的Array表示方式——[]；
    object：就是JavaScript的{ ... }表示方式。

## stringify函数<a id="orgheadline1"></a>

某个javascript对象字符串化。

    JSON.stringify(xiaoming, null, '  ');

## parse函数<a id="orgheadline2"></a>

将某个javascript对象刷成json对象。

    JSON.parse('[1,2,3,true]');

# 用javascript改变网页全局的css设置<a id="orgheadline4"></a>

参考了 [这个网页](http://stackoverflow.com/questions/566203/changing-css-values-with-javascript) 。

```js
function change_general_css(selector, property, value) {
    for (var i=0; i&lt;document.styleSheets.length;i++) {//Loop through all styles
        //Try add rule
        try { document.styleSheets[i].insertRule(selector+ ' {'+property+':'+value+'}', document.styleSheets[i].cssRules.length);
        } catch(err) {try { document.styleSheets[i].addRule(selector, property+':'+value);} catch(err) {}}//IE
    }
}
```

# 参考资料<a id="orgheadline5"></a>

1.  [javascript秘密花园](http://bonsaiden.github.io/JavaScript-Garden/zh/)