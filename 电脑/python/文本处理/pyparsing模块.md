<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 简介</a></li>
<li><a href="#orgheadline2">2. 空格</a></li>
<li><a href="#orgheadline3">3. <code>*</code> 有重复的含义</a></li>
<li><a href="#orgheadline4">4. srange函数</a></li>
<li><a href="#orgheadline5">5. Word类</a></li>
<li><a href="#orgheadline6">6. 刷float的进阶</a></li>
<li><a href="#orgheadline7">7. 刷化学分子式</a></li>
<li><a href="#orgheadline8">8. 刷wikipedia的infobox</a></li>
<li><a href="#orgheadline10">9. 附录</a>
<ul>
<li><a href="#orgheadline9">9.1. BNF相关</a></li>
</ul>
</li>
</ul>
</div>
</nav>


# 简介<a id="orgheadline1"></a>

pyparsing模块是一个用BNF思维（不同于正则表达式的思维）来进行文本处理的模块，借助pyparsing模块，我们可以写出很强大的text parser。

其最简单的例子如下所示:

```python
from pyparsing import Word, alphas

# define grammar
greet = Word( alphas ) + "," + Word( alphas ) + "!"

# input string
hello = "Hello, World!"

# parse input string
print(hello, "-&gt;", greet.parseString( hello ))
```

首先我们需要定义BNF text parser 模板，然后调用其 `parseString` 方法来具体进行parse操作。如果使用parseString而输入字符串并不复合规则，则会出错。我似乎更喜欢 `scanString` 方法，其并不出错，然后返回的结果是一个生成器对象，如果展开则如下所示:

    test: Hello, World! from python -> [((['Hello', ',', 'World', '!'], {}), 6, 19)]

其第一个是parse match的部分，然后第二个值是命中的start，第三个值是命中end的索引值。

# 空格<a id="orgheadline2"></a>

pyparsing默认是忽略空格的，

加入我们要匹配 `3.1415926` 这样的float，若是:

    real = Word(nums) + '.' + Word(nums)

则 `3 . 14` 也会匹配进去，这可能是你想要的，也可能不是。如果要精确匹配一个浮点数不允许中间出现空格，则要使用 `Combine` :

    real = Combine( Word(nums) + '.' + Word(nums) )

这里 `Combine` 的作用就是将多个匹配token连接为一个匹配字符串。

# `*` 有重复的含义<a id="orgheadline3"></a>

    expr*3 is equivalent to expr + expr + expr
    expr*(2,3) is equivalent to expr + expr + Optional(expr)
    expr*(n,None) or expr*(n,) is equivalent to expr*n + ZeroOrMore(expr) (read as "at least n instances of expr")
    expr*(None,n) is equivalent to expr*(0,n) (read as "0 to n instances of expr")
    expr*(None,None) is equivalent to ZeroOrMore(expr)
    expr*(1,None) is equivalent to OneOrMore(expr)

# srange函数<a id="orgheadline4"></a>

    >>> srange(r"[a-z]")
    'abcdefghijklmnopqrstuvwxyz'

srange函数里面大体有点类似于正则表达式的那种，但不能当成正则表达式，就类似上面那么写个范围即是了。

# Word类<a id="orgheadline5"></a>

下面这个token paser的意思是开头 `字母加上_` ，然后该词后面可以是 `字母加数字加_` 。

    Word( alphas+"_", alphanums+"_" )

Word类可以如上接受两个参数，其中第一个是必填参数，说明这个词的开头可选字符，然后第二个可选参数是用来说明这个词的body，也就是后面的可选字符。该类还可以接受如下可选项:

-   **min:** 最小字符长度
-   **max:** 最大字符长度
-   **exact:** 确切字符长度

# 刷float的进阶<a id="orgheadline6"></a>

之前写的:

    real = Combine( Word(nums) + '.' + Word(nums) )

还是较为粗糙，下面是一个简单完善点了的刷float的token paser:

    cs_real = set(nums + '.+-')
    
    pe_real = Combine(Optional(Word('+-')) +  Word(nums) + '.' + Word(nums) )
    tp_real = WordStart(cs_real) + pe_real + WordEnd(cs_real)

首先我们看到 `Optional(Word('+-'))` ，这样将可能有的正负号加进去了。然后当我们parse `x=-3.14` 的时候还是将其刷不进去，因为我们还没有很好的定义词头和词尾。一个不错的做法是将该词可能的charset加进来。如上所示，这样明确词头和词尾了，我们就可以顺利的将 `x=-3.14` 这种格式刷出float来了。

# 刷化学分子式<a id="orgheadline7"></a>

这个借鉴了官方examples的 `chemicalFormulas.py` 。我们注意看每个parser element后面是可以参数的，这个参数就是具体parse得到的结果。然后Optional可以设置默认值。然后 `Group` 这里的用途就是对于 `ZeroOrMore` 或者 `OneOrMore` 这样的parser element enhancement 更好的关闭。

    cs_formula = set(alphanums)
    pe_element = Regex("A[cglmrstu]|B[aehikr]?|C[adeflmorsu]?|D[bsy]|"
                    "E[rsu]|F[emr]?|G[ade]|H[efgos]?|I[nr]?|Kr?|L[airu]|"
                    "M[dgnot]|N[abdeiop]?|Os?|P[abdmortu]?|R[abefghnu]|"
                    "S[bcegimnr]?|T[abcehilm]|U(u[bhopqst])?|V|W|Xe|Yb?|Z[nr]")
    
    pe_elementnum = Group( pe_element("element") + Optional( Word( nums ), default="1" )("num"))
    tp_formula = WordStart(cs_formula) + OneOrMore( pe_elementnum ) + WordEnd(cs_formula)

# 刷wikipedia的infobox<a id="orgheadline8"></a>

wikipedia的infobox具体的值都有这样的形式:

    | SMILES = c1ccccc1
    | EINECS = 200-753-7
    | InChI = 1/C6H6/c1-2-4-6-5-3-1/h1-6H

我们可以建立如下parser:

```python
equation = Word(alphanums+'-_')("key").setParseAction(lambda s,l,t: t["key"].strip()) + '=' + restOfLine("value").setParseAction(action_value)
oneline = Group(LineStart() + "|" + equation + LineEnd())
# parse input string
token = oneline
```

这里每一行都由 `LineStart()` `|` `equation` `LineEnd()` 组成。

其中 `LineStart()` 和 `LineEnd()` 定义了一行的开始和一行的结束，基于 `\n` 。

然后我们看到 `equation` ，注意看 `Word(alphanums+'-_')("key")` ，这种表达也就是 `Word(alphanums+'-_')` 刷匹配的内容将以 `key` 存储进去。后面 `setParseAction` 是对该匹配的部分进行额外的动作，我们看到可以通过 `t["key"]` 来获得该值。 然后 `restOfLine()` 匹配之后到行结束的所有的内容。

# 附录<a id="orgheadline10"></a>

## BNF相关<a id="orgheadline9"></a>

本小节主要参考了 [这个网页](http://eikke.com/text-parsing-formal-grammars-and-bnf-introduction/index.html) 和 [这个网页](http://eikke.com/pyparsing-introduction-bnf-to-code/) 。

所谓 BNF ，即 Backus–Naur Form ，中文名字叫巴科斯范式。其用来表示一种上下无关文法的语言。

这一块术语挺绕口的，后面有时间再整理一下。