<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 前言</a></li>
<li><a href="#orgheadline33">2. javascript语言简介</a>
<ul>
<li><a href="#orgheadline2">2.1. 注释</a></li>
<li><a href="#orgheadline3">2.2. javascript代码放在那里</a></li>
<li><a href="#orgheadline4">2.3. 严格模式</a></li>
<li><a href="#orgheadline5">2.4. alert函数</a></li>
<li><a href="#orgheadline6">2.5. console.log函数</a></li>
<li><a href="#orgheadline7">2.6. confirm函数</a></li>
<li><a href="#orgheadline8">2.7. prompt函数</a></li>
<li><a href="#orgheadline9">2.8. 数据类型简介</a></li>
<li><a href="#orgheadline10">2.9. 声明变量</a></li>
<li><a href="#orgheadline11">2.10. typeof函数</a></li>
<li><a href="#orgheadline12">2.11. 数值型简介</a></li>
<li><a href="#orgheadline16">2.12. 字符串型简介</a>
<ul>
<li><a href="#orgheadline13">2.12.1. 多行字符串</a></li>
<li><a href="#orgheadline14">2.12.2. 字符串的一些方法清单</a></li>
<li><a href="#orgheadline15">2.12.3. toString方法</a></li>
</ul>
</li>
<li><a href="#orgheadline19">2.13. 数组</a>
<ul>
<li><a href="#orgheadline17">2.13.1. 数组的一些方法清单</a></li>
<li><a href="#orgheadline18">2.13.2. 比较两个数组是否相同</a></li>
</ul>
</li>
<li><a href="#orgheadline23">2.14. 对象类型简介</a>
<ul>
<li><a href="#orgheadline20">2.14.1. in语句</a></li>
<li><a href="#orgheadline21">2.14.2. delete语句</a></li>
<li><a href="#orgheadline22">2.14.3. hasOwnProperty方法</a></li>
</ul>
</li>
<li><a href="#orgheadline24">2.15. 布尔值</a></li>
<li><a href="#orgheadline25">2.16. null</a></li>
<li><a href="#orgheadline26">2.17. 条件判断结构</a></li>
<li><a href="#orgheadline28">2.18. 循环结构</a>
<ul>
<li><a href="#orgheadline27">2.18.1. while语句</a></li>
</ul>
</li>
<li><a href="#orgheadline29">2.19. 定义函数</a></li>
<li><a href="#orgheadline30">2.20. arguments用法</a></li>
<li><a href="#orgheadline31">2.21. rest用法</a></li>
<li><a href="#orgheadline32">2.22. 箭头函数</a></li>
</ul>
</li>
<li><a href="#orgheadline42">3. 面向DOM的操作</a>
<ul>
<li><a href="#orgheadline34">3.1. window</a></li>
<li><a href="#orgheadline35">3.2. navigator</a></li>
<li><a href="#orgheadline36">3.3. screen</a></li>
<li><a href="#orgheadline37">3.4. location</a></li>
<li><a href="#orgheadline41">3.5. document</a>
<ul>
<li><a href="#orgheadline38">3.5.1. getAttribute函数</a></li>
<li><a href="#orgheadline39">3.5.2. setAttribute函数</a></li>
<li><a href="#orgheadline40">3.5.3. 修改节点的文本内容</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#orgheadline43">4. 表单相关</a></li>
<li><a href="#orgheadline44">5. AJAX技术</a></li>
<li><a href="#orgheadline52">6. 附录</a>
<ul>
<li><a href="#orgheadline45">6.1. windows加载事件</a></li>
<li><a href="#orgheadline46">6.2. this关键词</a></li>
<li><a href="#orgheadline47">6.3. hello方法</a></li>
<li><a href="#orgheadline48">6.4. name属性</a></li>
<li><a href="#orgheadline49">6.5. 集合</a></li>
<li><a href="#orgheadline50">6.6. Date对象</a></li>
<li><a href="#orgheadline51">6.7. 参考资料</a></li>
</ul>
</li>
</ul>
</div>
</nav>


# 前言<a id="orgheadline1"></a>

本文主要面向那些已经熟悉一门编程语言的读者，并不十分适合编程初学者来阅读。

# javascript语言简介<a id="orgheadline33"></a>

## 注释<a id="orgheadline2"></a>

用 `//` 来标记一行注释。

```js
// This is a comment that the computer will ignore. 
// It is for your eyes only!
```

用 `/*   */` 来标记多行注释，不过用 `//` 来标记多行注释也是可以的，这个看编辑器方不方便。

## javascript代码放在那里<a id="orgheadline3"></a>

javascript的代码一般推荐是放在 `</body>` 之前，这样能够让浏览器更快地加载页面。至于其他倒没有特别的要求，刚开始简单的javascript代码就直接写上去也是可以的:

    <script>
    your awesome javascript code
    </script>
    </body>

这样更方便早期的调试。如果javascript代码量有一点了那么当然还是推荐另外单独放在一个js文件上，然后如下引入进来:

    <script src="where"></script>

然后一个网页内如果没有特别的理由的话，那么javascript代码最好就放在一个文件里面，方便网页加载。

## 严格模式<a id="orgheadline4"></a>

这个也不是必须的，不写也不能说你错，写上了当然更好。一般推荐编写javascript代码打开严格模式。

    "use strict";

## alert函数<a id="orgheadline5"></a>

弹出一段警告信息

    alert("hello")

## console.log函数<a id="orgheadline6"></a>

不同于alert函数，这个函数是在开发者工具的控制台那里显示。更加方便调试和debug javascript程序。

    console.log("hello")

## confirm函数<a id="orgheadline7"></a>

弹出一个对话框，可以和用户互动点击确定或取消。根据用户的点击返回true或false。

    confirm('This is an example of using JS to create some interaction on a website. Click OK to continue!');

## prompt函数<a id="orgheadline8"></a>

弹出一个对话框，具体是一个输入框，输入的值就是该函数的返回值。

    var age = prompt("what's your age");

## 数据类型简介<a id="orgheadline9"></a>

数值型，字符串型（javascript同python一样单引号双引号都可以），布尔型（javascript是 `true` 和 `false` ），然后其他常规数值运算和逻辑运算（如 `&&` `||` `!` 之类）和比较运算（这里值得一提的是和python的 `==` 对应的javascript的比较运算符应该是 `===` ，三个等号，这算是javascript的一个历史遗留语法瑕疵问题。）等都大体相同。python中的None对应的是javascript的 `null` 。

然后高级数据类型各个编程语言差异就很大了，不过javascript似乎和python在基本高级数据类型上也很接近，比如说javascript的数组就类似于python的列表:

    [1, 2, 3.14, 'Hello', null, true];

其索引index编号法则也和python一致。

然后javascript还有一个什么对象的概念，其大体可以看作python中的字典类型。

    var person = {
        name: 'Bob',
        age: 20,
        tags: ['js', 'web', 'mobile'],
        city: 'Beijing',
        zipcode: null
    };

如下所示具体调用各个数值也是类似的:

    person['name']
    "Bob"
    person.name
    "Bob"

## 声明变量<a id="orgheadline10"></a>

很多资料都会谈论这个问题，javascript代码声明变量都推荐加上 `var` 这个关键词，如下所示。

```js
var x;
var count = 2;
```

这样的话变量的作用域就很符合我们在其他编程语言中的常识，比如在函数里面就是局部变量等。

## typeof函数<a id="orgheadline11"></a>

相当于python中的 `type` 函数，查看某个对象的对象类型。

## 数值型简介<a id="orgheadline12"></a>

javascript整数和浮点数都不分了，都统一表示为Number，然后数值型那些运算，比如加减乘除之类的就不用多说了。其中 `%` 和python一样也是求余操作。在python3中有 `5//2` 是求商的概念，javascript没有这个概念，我们需要如下来获得类似的效果。

    console.log(parseInt(5/2))

## 字符串型简介<a id="orgheadline16"></a>

javascript的字符串类型和python非常类似，比如 `string[0]` 是支持的。然后不可以这样用string[0:2]，幸运的是javascript提供了类似python中的那种切片概念，就是使用 `slice` 方法

    console.log("hello".slice(0,2))
    console.log([1,3,4,5].slice(0,2))

不过javascript的slice方法和python的切片操作还是有点区别的，其只有 `(start,end)` 两个参数，然后其也有负数从末尾算起的概念，不过其不会倒着来，都是从左到右的那种顺序。具体请参看 [这里](http://www.w3school.com.cn/jsref/jsref_slice_string.asp) 。

### 多行字符串<a id="orgheadline13"></a>

这个对应的是python的 ''' 三引号情况。javascript是这样表示的:

    `多行
    字符串
    `

即使用那个反斜点符号包围之。

### 字符串的一些方法清单<a id="orgheadline14"></a>

-   **length:** 字符串长度
-   **toUpperCase:** 变成大写
-   **toLowerCase:** 变成小写
-   **indexOf:** 返回子字符串出现的索引位置，index索引编号规则和python相同。
-   **substring:** 返回子字符串，如果熟悉python的那种切片规则的话，那么推荐就直接使用 `slice` 方法。

### toString方法<a id="orgheadline15"></a>

javascript的数值、布尔值、对象和字符串都有一个 `toString` 方法，大体类似于python的 `str` 函数。不过推荐类似的也使用 `String` 来将某个javascript对象转变成为字符串。

## 数组<a id="orgheadline19"></a>

对应于python中的列表，javascript这里称为数组。如下所示我们看到其也是可变的。

    lst
    [1, 2, 3, 4, 5]
    lst[0] = 2
    2
    lst
    [2, 2, 3, 4, 5]

### 数组的一些方法清单<a id="orgheadline17"></a>

-   **length:** 数组长度
-   **indexOf:** 返回数组某个子元素的索引位置
-   **slice:** 切片操作，类似于python的 `lst[0:2]` 那种表达方法。
-   **push:** 末尾添加一个元素
-   **pop:** 最后一个元素删除
-   **unshift:** 数组头部添加一个或多个元素，返回新数组的长度
-   **shift:** 数组头部删除一个元素
-   **sort:** 排序，破坏型。值得一提的是对于数字排序并不是按照从大到小的顺序来的，不太清楚为何:

    > var lst = [1,5,2,3,51,4,45,545,541,48,77]
    undefined
    > lst.sort()
    [ 1,
      2,
      3,
      4,
      45,
      48,
      5,
      51,
      541,
      545,
      77 ]

在python中最多说字符串就这样，但这里是number类型啊。然后要正常排序，我们需要如下操作（参看 [这个网页](http://www.w3school.com.cn/jsref/jsref_sort.asp) ）:

    var lst = [1,5,2,3,51,4,45,545,541,48,77]
    function sortNumber(a,b){
        return a - b
    }
    lst.sort(sortNumber)
    alert(lst)

这里sort方法接受一个函数参数，这个函数接受两个参量，用来判断a和b的值大小，如果返回值小于0，则a放在前面。如果返回值大于0，则a放在后面。这种排序方法也支持数字字符串的情况。javascript在处理这种 `字符串 - 字符串` 的情况是会尝试做转换成number类型的才做。 

-   **reverse:** 反转，破坏型。
-   **splice:** 从指定的索引删除某些元素，然后在此处添加某些元素，相当于update更新了。

    > var arr = ['Microsoft', 'Apple', 'Yahoo', 'AOL', 'Excite', 'Oracle'];
    undefined
    > arr.splice(2, 3, 'Google', 'Facebook'); 
    ["Yahoo", "AOL", "Excite"]
    > arr
    ["Microsoft", "Apple", "Google", "Facebook", "Oracle"]

参数意思是从索引2开始删除3个元素，然后添加后面的元素。从上面的例子可以看出splice方法是破坏型的方法，然后其返回的是删除了的那是那个元素。

splice方法也可以用于只删除不添加也就是纯删除操作，或只添加不删除的纯添加操作。

    // 只删除,不添加:
    arr.splice(2, 2);
    // 只添加,不删除:
    arr.splice(2, 0, 'Google', 'Facebook');

-   **concat:** 连接两个数组，非破坏型。

    > var lst1 = [1,2,3]
    undefined
    > var lst2 = ['a','b','c']
    undefined
    > lst1.concat(lst2)
    [1, 2, 3, "a", "b", "c"]

-   **join:** 类似于python字符串的join方法，如下所示:

    var arr = ['A', 'B', 'C', 1, 2, 3];
    arr.join('-'); // 'A-B-C-1-2-3'

### 比较两个数组是否相同<a id="orgheadline18"></a>

参考了 [这个网页](http://stackoverflow.com/questions/3115982/how-to-check-if-two-arrays-are-equal-with-javascript) 。

```js
function arraysEqual(a, b) {
  if (a === b) return true;
  if (a == null || b == null) return false;
  if (a.length != b.length) return false;

  // If you don't care about the order of the elements inside
  // the array, you should sort both arrays here.

  for (var i = 0; i &lt; a.length; ++i) {
    if (a[i] !== b[i]) return false;
  }
  return true;
}
```

## 对象类型简介<a id="orgheadline23"></a>

其大致可以对应到python中的字典的概念。

    var person = {
        name: 'Bob',
        age: 20,
        tags: ['js', 'web', 'mobile'],
        city: 'Beijing',
        zipcode: null
    };

javascript的对象的value还可以是某个函数，这样的话其实际上就类似于python中的类一样，成了一个方法了。然后类似python的self，其也有一个 `this` 关键词来表示本对象实例。

### in语句<a id="orgheadline20"></a>

    'name' in xiaoming;

    > var d = {}
    undefined
    > d['a'] = 1
    1
    > d
    Object {a: 1}
    > 'a' in d
    true
    > 1 in [1,2,3]
    true

### delete语句<a id="orgheadline21"></a>

其对应的就是python的del语句。然后我们看到javascript的 `delete` 语句删除不存在键也不会报错。

    > d
    Object {a: 1}
    > delete(d.b)
    true
    > d
    Object {a: 1}
    > delete(d.a)
    true
    > d
    Object {}

### hasOwnProperty方法<a id="orgheadline22"></a>

对应于python2的has\_key方法，不过python2已经移除了，推荐用in语句。

    d = {'a':1}
    Object {a: 1}
    d.hasOwnProperty('a')
    true

## 布尔值<a id="orgheadline24"></a>

javascript的布尔值是 `true` 和 `false` 。然后需要额外强调的是，类似python的比较判断（==）符号在javascript中是 `===` ，三个等号，这不是什么别出心裁，也没有任何实际的好处，就是javascript的历史遗留问题罢了。

    === Equal to
    !== Not equal to

## null<a id="orgheadline25"></a>

javascript的是 `null` 。其也是一个单独的对象。类似于python的 `None` ，然后还有一个什么 `undefined` 。比如函数没有明确return值就会默认返回 `undefined` ，感兴趣的可能查一下这两个的区别，我看了一下，觉得挺无聊的。上面谈到 `==` 和 `===` 的区别，如果用 `===` ，则 `undefined` 是不等于 `null` 的，如果用 `==` ，则javascript会额外做一些类型转换工作，这两个又会看作相等的。所以一个简单的做法就是:

    result == null

那些可能undefined的情况都视作null来处理之。

## 条件判断结构<a id="orgheadline26"></a>

条件判断结构，和python大同小异，除了那些圆括号（记住这个圆括号必须加上）和花括号。

```js
var feedback = 10
if(feedback &gt; 8){
    console.log("Thank you! We should race at the next concert!")}
else{
    console.log("I'll keep practicing coding and racing.")}
```

虽然javascript不像python那样强制缩进风格，但还是推荐用缩进来增强你的代码可读性和逻辑清晰性，如:

```js
age = 20
if(age &lt; 6){
    console.log('kid')}
else if(age &gt;= 18){
    console.log('adult')}
else{
    console.log('teenager')}
```

这种写法使得代码更加接近python风格，然后我们可以把第一个花括号视作python缩进区块开始的冒号，然后后面的花括号视作某个区块部分语句结束的标识。

所以我们下面写一个更加复杂点的例子（具体这些小脚本的试验推荐在ubuntu下安装nodejs，然后执行 `nodejs test.js` 即可。）。原python脚本如下:

```python
x=-2
if x&gt;0:
    print('x大于0')
    if x&gt;2:
        print('x&gt;2')
    elif x&lt;2:
        print('0&lt;x&lt;2')
    else:
        print('x=2')
elif x&lt;0:
    print('x小于0')
else:
    print('x等于0')
```

改写成为:

```js
var x = -1
if(x&gt;0){
    console.log('x大于0')
    if(x&gt;2){
        console.log('x&gt;2')}
    else if(x&lt;2){
        console.log('0&lt;x&lt;2')}
    else{
        console.log('x=2')}}
else if(x&lt;0){
    console.log('x小于0')}
else{
    console.log('x等于0')}
```

读者可以用不同的x值来测试一下，这里的关键性问题不是区块开始那里，而是区块什么时候结束。然后就是程序结构最好清清晰晰的用 if else 或者 if else if else if else 等这类语句表达出来。关于多个else if语句的组合平行表达，读者可以自己试验一下，我简单写了下面这个例子:

```js
age = 5
if(age &lt; 6){
    console.log('age 小于 6')}
else if(age &gt;= 25){
    console.log('age 大于等于 25')}
else if(age &gt;= 18){
    console.log('age 大于等于18且小于25')}
else{
    console.log('age 大于等于6且小于18')}
```

javascript有switch语句，作为我们pythoner你懂的，用多个else if语句也是可以的。

## 循环结构<a id="orgheadline28"></a>

javascript和python都有while语句，但while语句用的较少，更多的是使用for语句。

然后递归遍历字典的key也是可以的:

```js
for(var i in {'a':1,'b':2}){
    console.log(i)}
```

### while语句<a id="orgheadline27"></a>

while语句简单了解下吧，熟悉c语言的简单看一下就清楚了。

```js
var x = 0;
var n = 99;
while (n &gt; 0) {
    x = x + n;
    n = n - 2;
}
```

还有do while 语句

```js
var n = 0;
do {
    n = n + 1;
}while (n &lt; 100);
```

## 定义函数<a id="orgheadline29"></a>

一个简单的函数定义和使用如下所示:

    var greeting = function(name){
        console.log(name);
    }
    greeting('hello')

我们看到javascript明确将函数名作为一个变量，这是唯一要值得注意的，不过你也可以采用这种写法，这样更加为我们所熟悉了:

```js
function abs(x){
    if(x &gt;= 0){
        return x;} 
    else{
        return -x;}
}
```

这两种定义风格是完全等价的。这里值得一提的是如果函数没有确定return值，则视作返回的undefined。

## arguments用法<a id="orgheadline30"></a>

javascript的函数内部可以直接使用arguments这个变量，其不是一个Array，但可以如下使用:

    arguments[0]
    arguments.length

其会接受传入函数的所有参量。

## rest用法<a id="orgheadline31"></a>

这个有点类似于lisp语言的rest参量控制概念，也就是如下

    function func(a,b,...rest){
        console.log(rest)
    }

rest是表示除了a和b之外的所有其余参量。注意前面三个点号: `...rest` 。

## 箭头函数<a id="orgheadline32"></a>

就是匿名函数lambda的一种写法。暂时不太关心、

# 面向DOM的操作<a id="orgheadline42"></a>

如果读者熟悉python的beautifulsoup或者类似的爬取网页领域，那么对于javascript所谈论的DOM是个什么东西是无需多言的。下面开始介绍那些对象吧。

## window<a id="orgheadline34"></a>

window是一个全局变量，表示本浏览器的窗口。

-   **innerWidth:** 本窗口的内部宽度，所谓的内部宽度是指除去菜单栏工具栏等具体显示网页的净宽度。
-   **innerHeight:** 本窗口的内部高度，内部高度含义类似上面谈及的内部宽度。
-   **outerWidth:** 本窗口的外部宽度
-   **outerHeight:** 本窗口的外部高度

## navigator<a id="orgheadline35"></a>

其有属性如下所示:

-   **appName:** 浏览器名称；
-   **appVersion:** 浏览器版本；
-   **language:** 浏览器设置的语言；
-   **platform:** 操作系统类型；
-   **userAgent:** 浏览器设定的User-Agent字符串。

## screen<a id="orgheadline36"></a>

-   **width:** 屏幕宽度
-   **height:** 屏幕高度
-   **colorDepth:** 颜色位数

## location<a id="orgheadline37"></a>

-   **href:** 完整路径
-   **protocol:** 如下所示:

    > location.protocol
    "http:"

-   **host:** 对应python urlsplit之后的netloc
-   **port:** 端口号
-   **pathname:** 对应python urlsplit之后的path
-   **search:** 参数字段
-   **hash:** 也就是segement

---

-   **assign():** 刷新当前页面
-   **reload():** 重载当前页面

## document<a id="orgheadline41"></a>

你可以认为这是beautifulsoup刷过之后的网页文档树，这是以后我们操作文档的主要交互对象。比如简单的写入html代码:

```js
document.write("&lt;h1&gt;This is a heading&lt;/h1&gt;");
document.write("&lt;p&gt;This is a paragraph.&lt;/p&gt;");
```

这会在网页文档里面附加一些内容。

按钮点击一下则执行什么javascript代码。

```js
&lt;button type="button" onclick="alert('Welcome!')"&gt;点击这里&lt;/button&gt;
```

javascript改变HTML内容

```html
&lt;script&gt;
function myFunction()
{
x=document.getElementById("demo");  // 找到元素
x.innerHTML="Hello JavaScript!";    // 改变内容
}
&lt;/script&gt;

&lt;button type="button" onclick="myFunction()"&gt;点击这里&lt;/button&gt;
```

-   **title:** title标签内所含的内容
-   **cookie:** 获取cookie的内容
-   **getElementById():** 该方法用于根据Id来提取网页内容的某个DOM子节点
-   **getElementsByTagName():** 该方法用于根据Tag标签名字来提取某个DOM子节点（看到那个Elements的s，其将返回多个命中目标。记住带s的这些将返回的是一个数组对象）
-   **getElementsByClassName():** 该方法用于根据css来进行选择某些DOM子节点。

返回的所谓DOM子节点对象，可以如同document对象一样使用这三个方法，相当于在第一次查找结果之上进一步查找。

-   **querySelector():** 类似beautifulsoup的selector选择语法:

    var ps = q1.querySelectorAll('div.highlighted > p');

-   **querySelectorAll():** 类似上面，但返回所有结果。

找到目标标签元素之后，各个样式属性可以如下直接引用:

    document.querySelector('a').href

### getAttribute函数<a id="orgheadline38"></a>

找到元素之后我们可以使用 `getAttribute` 函数来获取其属性。比如获取title属性:

    object.getAttribute("title")

### setAttribute函数<a id="orgheadline39"></a>

设置某个元素节点的属性值。

    object.setAttribute(attribute,value)

### 修改节点的文本内容<a id="orgheadline40"></a>

-   **innerHTML:** 对应该DOM节点标签内的文本内容
-   **innerText:** 类似上面的innerHTML，但不可设置任何HTML标签

-   **createElement():** 创建一个标签元素对象:

    var haskell = document.createElement('p');
    haskell.id = 'haskell';
    haskell.innerText = 'Haskell';

上面的haskell具体内容就是: `<p id=​"haskell">​Haskell​</p>​` 。

-   **appendChild():** 本标签元素为所谓的父节点，给自己添加一个子节点标签元素。（可以把找到的标签元素视作一个列表，然后执行append某个子节点操作）
-   **insertBefore():** 本标签元素为所谓的父节点，然后在其内的某个标签元素之前插入某个子节点标签元素:

    parentElement.insertBefore(newElement, referenceElement);

-   **insertAfter():** javascript原生没有，需要自己定义:

```js
function insertAfter(newElement, targetElement){
    var parent = targetElement.parentNode;
    if (parent.lastChild == targetElement){
        parent.appendChild(newElement);
    }
    else{
        parent.insertBefore(newElement, targetElement.nextSibling);
    }
}
```

-   **parentElement:** 返回本标签元素对象的父标签元素对象
-   **removeChild():** 本标签元素为父节点，删除本父节点的某个子节点

但是实际使用中推荐用jquery来操作各个DOM节点。

# 表单相关<a id="orgheadline43"></a>

<http://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/001434499922277b890fd537901490a84fc24b2b8b8867e000>

# AJAX技术<a id="orgheadline44"></a>

AJAX技术英文全名是: Asynchronous JavaScript and XML ，什么异步的JavaScript与XML技术。简单的了解就是网页开着，然后javascript开启了某个类似于python的requests模块的网页请求，一般是向本地的网页服务器发送的吧，但也可以跨站请求。然后其是异步的，如果不异步，那么网页阻塞了，用户无法继续阅读或点击了，这当然是不行的。

基本的使用过程是新建然后 `XMLHttpRequest()` 对象，然后通过这个对象来进行后续的操作。如下所示:

    var request = new XMLHttpRequest();

然后就是定义request的行为:

    request.onreadystatechange = function(){
        do something;
    }

我们看得出来这是一个什么 `onreadystatechange` 事件，然后挂载了某个函数。然后request有如下几个 `readyState` 状态:

-   0 未初始化
-   1 正在加载
-   2 加载完毕
-   3 正在交互
-   4 完成

请求的HTTP状态码返回通过 `request.status` 获得，请求的响应文本通过 `request.responseText` 获得，此外还有一个 `responseXML` 属性，如果服务器响应是XML则用它。

    var request = new XMLHttpRequest(); // 新建XMLHttpRequest对象
    
    request.onreadystatechange = function () { // 状态发生变化时，函数被回调
        if (request.readyState === 4) { // 成功完成
            // 判断响应结果:
            if (request.status === 200) {
                // 成功，通过responseText拿到响应的文本:
                return success(request.responseText);
            } else {
                // 失败，根据响应码判断失败原因:
                return fail(request.status);
            }
        } else {
            // HTTP请求还在继续...
        }
    }
    
    // 发送请求:
    request.open('GET', '/api/categories');
    request.send();

然后就是通过request的 `open` 方法和 `send` 方法来实际发送请求了。比如 'GET'

    request.open('GET',url,true)
    request.send()

第三个参数是异步否，一般设置为true。

如果是 'POST' 则send还可以发送一些东西作为POST请求的额外数据。下面是来自w3school的一个例子:

    xmlhttp.open("POST","ajax_test.asp",true);
    xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xmlhttp.send("fname=Bill&lname=Gates");

这里的 `setRequestHeader` 是设置请求头的，然后send的是string字符串，也就是说我们想要发送json或者那种字典格式，是需要额外处理的。（我注意到jquery提供的data这个东西可以直接是字典值。）

然后在处理request过程，我们一般是需要等到readyState为4然后http状态码为200才进行某个动作，也就是廖雪峰的这个例子所展示的sucess情况:

    request.onreadystatechange = function () { // 状态发生变化时，函数被回调
        if (request.readyState === 4) { // 成功完成
            // 判断响应结果:
            if (request.status === 200) {
                // 成功，通过responseText拿到响应的文本:
                return success(request.responseText);
            } else {
                // 失败，根据响应码判断失败原因:
                return fail(request.status);
            }
        } else {
            // HTTP请求还在继续...
        }
    }

我注意到jquery里面有个sucess这个东西，应该对应的就是这里的success的情况，难怪jquery那么流行，就是ajax这里就带来了很大的便利，更不用提 `document. getElementById()` 等等那些冗长的语法了。关于jquery另外一篇文章讨论吧。

# 附录<a id="orgheadline52"></a>

一些零碎的东西拾遗。

## windows加载事件<a id="orgheadline45"></a>

```js
function addLoadEvent(func){
    console.log("window onload event");
    var oldonload = window.onload;
    if (typeof window.onload != 'function'){
        window.onload = func;
    }
    else{
        window.onload = function (){
            oldonload();
            func();
        }
    }
}
```

## this关键词<a id="orgheadline46"></a>

this关键词的内容挺丰富的，总的来说this就是指对象本身:

1.  this在函数内部表示本函数自身
2.  如果在方法里面（这里强调方法是指对象的某个数值的值是函数对象），则this是本对象。

## hello方法<a id="orgheadline47"></a>

重定义hello方法相当于python的重定义 `__init__` 方法，其为该对象的重构函数，这样你就可以使用 `new` 来新建一个实例了。

    s = new Student('John')

## name属性<a id="orgheadline48"></a>

name属性是一个特殊的属性，常用来表示该对象的名字。

## 集合<a id="orgheadline49"></a>

javascript中的集合Set大体也和python中的集合概念相近。

    var s1 = new Set(); // 空Set
    var s2 = new Set([1, 2, 3]); // 含1, 2, 3

然后其也有 `add` 方法用于添加一个元素。用 `delete` 方法来删除某个元素。

## Date对象<a id="orgheadline50"></a>

    var now = new Date();
    now; // Wed Jun 24 2015 19:49:22 GMT+0800 (CST)
    now.getFullYear(); // 2015, 年份
    now.getMonth(); // 5, 月份，注意月份范围是0~11，5表示六月
    now.getDate(); // 24, 表示24号
    now.getDay(); // 3, 表示星期三
    now.getHours(); // 19, 24小时制
    now.getMinutes(); // 49, 分钟
    now.getSeconds(); // 22, 秒
    now.getMilliseconds(); // 875, 毫秒数
    now.getTime(); // 1435146562875, 以number形式表示的时间戳

## 参考资料<a id="orgheadline51"></a>

1.  <https://www.codecademy.com>
2.  [廖雪峰的javascript教程](http://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000)
3.  javascript DOM编程艺术第二版: Jeremy Keith, Jeffrey Sambells著; 杨涛 王建桥 杨晓云等译.