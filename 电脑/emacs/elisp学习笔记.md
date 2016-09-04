<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline3">1. 前言</a>
<ul>
<li><a href="#orgheadline1">1.1. quote函数</a></li>
<li><a href="#orgheadline2">1.2. 链表结构</a></li>
</ul>
</li>
<li><a href="#orgheadline48">2. elisp基础</a>
<ul>
<li><a href="#orgheadline4">2.1. 注释</a></li>
<li><a href="#orgheadline5">2.2. 程序中的操作对象</a></li>
<li><a href="#orgheadline8">2.3. 类型检测</a>
<ul>
<li><a href="#orgheadline6">2.3.1. type-of</a></li>
<li><a href="#orgheadline7">2.3.2. 其他p型函数</a></li>
</ul>
</li>
<li><a href="#orgheadline11">2.4. 相等判断</a>
<ul>
<li><a href="#orgheadline9">2.4.1. eq</a></li>
<li><a href="#orgheadline10">2.4.2. equal</a></li>
</ul>
</li>
<li><a href="#orgheadline16">2.5. 定义变量</a>
<ul>
<li><a href="#orgheadline12">2.5.1. defvar</a></li>
<li><a href="#orgheadline13">2.5.2. defconst</a></li>
<li><a href="#orgheadline14">2.5.3. defcustom</a></li>
<li><a href="#orgheadline15">2.5.4. defgroup</a></li>
</ul>
</li>
<li><a href="#orgheadline17">2.6. eval-last-sexp</a></li>
<li><a href="#orgheadline18">2.7. concat函数</a></li>
<li><a href="#orgheadline19">2.8. substring函数</a></li>
<li><a href="#orgheadline20">2.9. buffer-name</a></li>
<li><a href="#orgheadline21">2.10. buffer-file-name</a></li>
<li><a href="#orgheadline22">2.11. load-file-name</a></li>
<li><a href="#orgheadline23">2.12. file-name-directory</a></li>
<li><a href="#orgheadline24">2.13. 读取某个文件内容</a></li>
<li><a href="#orgheadline25">2.14. if函数</a></li>
<li><a href="#orgheadline26">2.15. and</a></li>
<li><a href="#orgheadline27">2.16. or</a></li>
<li><a href="#orgheadline28">2.17. cond</a></li>
<li><a href="#orgheadline29">2.18. defun定义自己的函数</a></li>
<li><a href="#orgheadline30">2.19. let创建局部变量</a></li>
<li><a href="#orgheadline31">2.20. 基本lisp链表操作元函数</a></li>
<li><a href="#orgheadline35">2.21. alist和plist</a>
<ul>
<li><a href="#orgheadline32">2.21.1. plist-get</a></li>
<li><a href="#orgheadline33">2.21.2. assoc</a></li>
<li><a href="#orgheadline34">2.21.3. assq</a></li>
</ul>
</li>
<li><a href="#orgheadline36">2.22. reverse函数</a></li>
<li><a href="#orgheadline37">2.23. nth</a></li>
<li><a href="#orgheadline38">2.24. nthcdr</a></li>
<li><a href="#orgheadline39">2.25. last</a></li>
<li><a href="#orgheadline40">2.26. remove</a></li>
<li><a href="#orgheadline47">2.27. 集合相关函数</a>
<ul>
<li><a href="#orgheadline41">2.27.1. member</a></li>
<li><a href="#orgheadline42">2.27.2. intersection</a></li>
<li><a href="#orgheadline43">2.27.3. union</a></li>
<li><a href="#orgheadline44">2.27.4. set-difference</a></li>
<li><a href="#orgheadline45">2.27.5. subsetp</a></li>
<li><a href="#orgheadline46">2.27.6. set-exclusive-or</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#orgheadline76">3. elisp进阶</a>
<ul>
<li><a href="#orgheadline49">3.1. current-buffer</a></li>
<li><a href="#orgheadline50">3.2. other-buffer</a></li>
<li><a href="#orgheadline51">3.3. switch-to-buffer</a></li>
<li><a href="#orgheadline52">3.4. buffer-size</a></li>
<li><a href="#orgheadline53">3.5. point对象</a></li>
<li><a href="#orgheadline54">3.6. interactive</a></li>
<li><a href="#orgheadline55">3.7. save-excursion</a></li>
<li><a href="#orgheadline56">3.8. next-line</a></li>
<li><a href="#orgheadline57">3.9. mark-whole-buffer</a></li>
<li><a href="#orgheadline58">3.10. subst</a></li>
<li><a href="#orgheadline59">3.11. sublis</a></li>
<li><a href="#orgheadline60">3.12. funcall</a></li>
<li><a href="#orgheadline61">3.13. mapcar</a></li>
<li><a href="#orgheadline62">3.14. lambda</a></li>
<li><a href="#orgheadline63">3.15. find-if</a></li>
<li><a href="#orgheadline64">3.16. remove-if-not</a></li>
<li><a href="#orgheadline65">3.17. remove-if</a></li>
<li><a href="#orgheadline66">3.18. reduce</a></li>
<li><a href="#orgheadline67">3.19. every</a></li>
<li><a href="#orgheadline68">3.20. incf</a></li>
<li><a href="#orgheadline69">3.21. decf</a></li>
<li><a href="#orgheadline70">3.22. push</a></li>
<li><a href="#orgheadline71">3.23. pop</a></li>
<li><a href="#orgheadline72">3.24. when</a></li>
<li><a href="#orgheadline73">3.25. unless</a></li>
<li><a href="#orgheadline74">3.26. dotimes 和dolist函数</a></li>
<li><a href="#orgheadline75">3.27. 理解递归</a></li>
</ul>
</li>
<li><a href="#orgheadline77">4. 定义自己的包</a></li>
<li><a href="#orgheadline81">5. 附录</a>
<ul>
<li><a href="#orgheadline78">5.1. emacs中使用common-lisp</a></li>
<li><a href="#orgheadline79">5.2. 命令行执行emacs里面的命令</a></li>
<li><a href="#orgheadline80">5.3. 参考资料</a></li>
</ul>
</li>
</ul>
</div>
</nav>


# 前言<a id="orgheadline3"></a>

编写emacs插件的过程实际上就是熟悉elisp这门语言的过程。lisp语言在很多方面都和我们接触的其他大部分语言与众不同。要理解这点最关键的就是要理解lisp语言的链表数据结构。

因为我以前折腾过一段时间的common-lisp了，所以下面的谈论就大致回顾一下lisp的最核心的一些特性（也不会拘泥于某些语法细节）:

lisp语言里面最基本的元素是atom的，是atom类型的元素可以直接eval，你可以在emacs下输入 `M-x ielm` 来进入elisp的交互环境试着输入 1 或者 "abc" 来看一下。你可以如下来看看某个元素是不是数字:

```emacs-lisp
ELISP&gt; (numberp 1.1)
t
```

类似的我们有 `stringp` 来判断目标元素是不是字符串。lisp的 `t` 和 `nil` 就是布尔真和布尔假。然后空表()也表示nil，然后其他所有东西都看作真。除开上面讲的有具体值atom元素，第二大类元素就是符号(symbol)，所谓symbol就是你在lisp里面简单输入一个x，其就是一个符号，这个符号具体的值可以对应为某个函数，或者某个值。

然后接下来lisp的第二大概念就是列表，lisp的一个表达式就是一个列表。比如:

```emacs-lisp
ELISP&gt; (+ 2 5)
7
ELISP&gt; (* 5 5)
25
```

若这个列表被eval执行，也就是如上输入，则该列表第一个元素总认为是一个函数，然后后面的都是该函数的各个参数。具体函数定义细节这里略过。

## quote函数<a id="orgheadline1"></a>

在lisp系统中，quote是一个特殊的函数，其意思是:

    (eval (quote x)) = x

也就是后面的元素跳过eval，直接返回自身。上面的 (quote x) 还有一种简写形式 'x ，你可以直接输入'x来返回某个符号对象。

```emacs-lisp
ELISP&gt; 'x
x
ELISP&gt; '(1 2 3)
(1 2 3)
```

这里需要读者深刻理解，因为在lisp语言中，任何一个列表都将被eval的，而具体就是递归遍历列表内的各个元素，将各个元素都求出值出来，这里所谓的求出值，就是最终元素为上面讲的atom元素类型，或者数字或者字符串。如果是列表套列表结构（或者说得不规范点，括号套括号结构），那么里面的子列表可以看作大列表内的子元素，然后其又将继续eval之。如此递归循环，直到得出某个结果。然后对于每个列表的eval都将其内的第一个元素视作函数。

因此quote函数被lisp语言里面广泛使用，被用作表达本符号自身，然后出了第一个eval列表之后，到达父列表，其就是x也就是被eval出该符号对应的值了。所以我们也可以把引用包装某个符号看作将该符号的值传递给父环境列表中。

因为其他编程语言的列表和lisp语言里面的列表相去甚远，所以最好称之为链表。下面将介绍一下lisp语言的链表结构，理解这点对于理解lisp语言和编程模式是很关键的。

## 链表结构<a id="orgheadline2"></a>

本小节的例子使用的是common-lisp，但这里具体是要理解lisp语言底层的链表结构，这一点各个lisp方言包括emacs-lisp都是一致的。

首先推荐读者到 [这里](http://www.cs.cmu.edu/~dst/Lisp/sdraw/sdraw.generic) 下载该网页文件保存为 `sdraw.lisp` 。然后在slime中加载如下所示:

```lisp
CL-USER&gt; (load "~/sdraw.lisp")
;; Loading file /home/wanze/sdraw.lisp ...
;; Loaded file /home/wanze/sdraw.lisp
T
CL-USER&gt; (sdraw '("a"))

[*|*]---&gt;NIL
 |
 v
"a"
; No value
```

这里 **load** 函数就是加载某个lisp脚本，这个lisp脚本提供了一个 **sdraw** 函数，其可以画出你给出的链表的结构图，是个不错的工具。

我们看到上面的例子，链表("a")里面就一个元素，其实际上是由两个部分组成的，第一个是car，也就是链表头，第二个是cdr，也就是链表尾。如下所示:

```lisp
CL-USER&gt; (car '("a"))
"a"
CL-USER&gt; (cdr '("a"))
NIL
CL-USER&gt;
```

然后我们再来看两个元素的情况:

```lisp
CL-USER&gt; (sdraw '("a" "b"))

[*|*]---&gt;[*|*]---&gt;NIL
 |        |
 v        v
"a"      "b"
```

我们看到lisp的链表大致由叫做cons cell的东西链接起来的，这个cons cell分为两部分，一个头（car），一个尾（cdr），然后头或尾可以具体指向某个值，其中头或者尾指向某个具体的值则表明该链接终止了。一般的链表就如同上面所示，头指向某个具体的值，尾链接其他cons cell或者最终指向nil终止。但实际上还有一种结构:

```lisp
CL-USER&gt; (sdraw '("a" . "b"))

[*|*]---&gt;"b"
 |
 v
"a"
```

下面再贴一个链表之内还有一个链表的情况:

```lisp
CL-USER&gt; (sdraw '("a" ("b" "c")))

[*|*]---&gt;[*|*]---&gt;NIL
 |        |
 v        v
"a"      [*|*]---&gt;[*|*]---&gt;NIL
          |        |
          v        v
         "b"      "c"
```

实际上这里所谓的 cons cell 的cons是英文单词链接concatenate的缩写，你可以如下来自己构建一个链表结构:

```lisp
CL-USER&gt; (cons "a" nil)
("a")
CL-USER&gt; (cons "a" '("b" "c"))
("a" "b" "c")
CL-USER&gt; (cons "a" '(("b" "c")))
("a" ("b" "c"))
CL-USER&gt;
```

这里就是构建一个cons cell，car指向第一个参数，cdr指向第二个参数。

上面谈及的lisp语言系最通用的一些概念，具有普适性。然后接下来lisp编程的故事就是各种各样的函数——官方内置的或者你自己定义的了。这其中各个lisp方言之间差异就很大了。我们后面再详细讨论之。

# elisp基础<a id="orgheadline48"></a>

## 注释<a id="orgheadline4"></a>

注释用 `;` 符号开始。

## 程序中的操作对象<a id="orgheadline5"></a>

-   integer float 同样存在数值范围限制，这个程序员注意点就可以了

-   character 这个比较特殊，不是 'a' 这样的表达，而是 ?a 这样的输入，然后字符实际上就是一个数值，此外特殊的字符还有:

    ?\a ⇒ 7    ; control-g, C-g
    ?\b ⇒ 8    ; backspace, BS, C-h
    ?\t ⇒ 9    ; tab, TAB, C-i
    ?\n ⇒ 10   ; newline, C-j
    ?\v ⇒ 11   ; vertical tab, C-k
    ?\f ⇒ 12   ; formfeed character, C-l
    ?\r ⇒ 13   ; carriage return, RET, C-m
    ?\e ⇒ 27   ; escape character, ESC, C-[
    ?\s ⇒ 32   ; space character, SPC
    ?\\ ⇒ 92   ; backslash character, \
    ?\d ⇒ 127  ; delete character, DEL

特殊符号的转义，这些符号应该用 \\ 来进行转义:

    ( ) \ | ; " # . ,

官方文档还有单左引号和单右引号 ’‘ ，似乎在英文中并没使用这两个符号啊？

-   symbol 可以看作其他语言的变量名

-   sequence 其包括 list（） 和 array（arrayp） 。array是定长数组，其又可以分为: string vector char-table（char-table-p） bool-table 。sequence不可以读两次？
    -   string 一大段字符串可以用 \\ 换行  char-or-string-p
    -   vertor  
        
            ELISP> [1 2 3]
            [1 2 3]

bool-vector-p

-   cons cell 结构，这个就是lisp语言的底层了。 consp
-   dotted pair notation 其实也是一种更 cons cell 结构，只是两端都有值 (a . b)
-   association list  基于前面的dotted pair notation:

## 类型检测<a id="orgheadline8"></a>

### type-of<a id="orgheadline6"></a>

### 其他p型函数<a id="orgheadline7"></a>

atom
arrayp
bool-vector-p
bufferp
byte-code-function-p
case-table-p
char-or-string-p
char-table-p
commandp 
consp 
custom-variable-p
display-table-p
floatp
fontp
frame-configuration-p
frame-live-p
framep
functionp
hash-table-p
integer-or-marker-p
integerp
keymapp 
keywordp
listp 
markerp
wholenump
nlistp 
numberp 
number-or-marker-p
overlayp
processp
sequencep
stringp 
subrp 
symbolp
syntax-table-p
vectorp
window-configuration-p
window-live-p
windowp 
booleanp
string-or-null-p

## 相等判断<a id="orgheadline11"></a>

相等判断：equal   eq   eql  =  equalp
eq是运算最快的了，它只比较地址。
equal比较内容。
eql类似eq，比较地址，还专门针对不同类型的数字。
= 专门针对不同类型的数字
equalp和equal差不多，但是忽略字符中的大小写。

### eq<a id="orgheadline9"></a>

test if the same object

    (eq object1 object2)

### equal<a id="orgheadline10"></a>

test if has the same components

    (equal object1 object2)

equal-including-properties object1 object2

## 定义变量<a id="orgheadline16"></a>

setq是最基本的，上面已经有所介绍了。然后是defvar和defconst，一般推荐使用defvar和defconst，其中defvar用于声明变量，然后defconst用于声明常量，此外还有defcustom，defcustom比较复杂，等下再详细讨论，其和defvar，defconst的区别是defcustom适用于接口开放给用户的变量，好方便用户来定制。defvar和defconst和setq的区别是其可以接受一段字符串作为自身的描述信息，所以一般推荐使用这个。然后这几个本质上应该都是基于setq的，也就是都是定义的全局变量。

### defvar<a id="orgheadline12"></a>

    defvar symbol [ value [ doc-string ]]

### defconst<a id="orgheadline13"></a>

    defconst symbol value [ doc-string ]

### defcustom<a id="orgheadline14"></a>

defcustom参数和defvar比较起来多了一些可选项关键词参数可以填，然后前面三个意思是变量名字，初始值和说明文档。

    defcustom option standard doc [ keyword value ]

凡是需要对外开放给用户配置的变量都推荐使用defcustom，然后通过 `custom-set-variables` 来配置这些变量。如下所示:

    (custom-set-variables
     '(cua-mode t nil (cua-base))
     '(custom-enabled-themes (quote (tango-dark))))

`custom-set-variables` 里面定制的格式，第一个是变量名，第二个是具体的值，这都是好理解的。然后后面是一些可选的参数，now request和comment。其中now如果non-nil则该变量的值没有evaluate也进行赋值，然后request是一个feature列表，这个后面再说。comment就是一些定制说明了。

defcustom的大致格式如下:

    (defcustom org-html-use-infojs 'when-configured
      "Non-nil when Sebastian Rose's Java Script org-info.js should be active.
    This option can be nil or t to never or always use the script.
    It can also be the symbol `when-configured', meaning that the
    script will be linked into the export file if and only if there
    is a \"#+INFOJS_OPT:\" line in the buffer.  See also the variable
    `org-html-infojs-options'."
      :group 'org-export-html
      :version "24.4"
      :package-version '(Org . "8.0")
      :type '(choice
              (const :tag "Never" nil)
              (const :tag "When configured in buffer" when-configured)
              (const :tag "Always" t)))

每一个关键词前面都应该加上 `:` ，下面详细讨论这些关键词:

-   :type 数据类型定义
-   :options 关于该变量的一系列的建议值
-   :group 该变量属于那个群组

### defgroup<a id="orgheadline15"></a>

定义一个群组

    defgroup group members doc [ keyword value ]

如果其接受 :group ，则表示该群组属于那个群组。

## eval-last-sexp<a id="orgheadline17"></a>

eval最后一个s表达式，这个快捷键很常用 `C-x C-e` ，用来执行最后一个S表达式，方便快速测试。然后还有 `C-:` 在minibuffer下进行互动。比如下面写上这么一行，然后在行尾执行 `C-x C-e`

(defun hello () (message "hello world"))

这个定义的hello命令就进入elisp环境了，然后输入 `C-:` ，在minibuffer下来输入 (hello) 来看一下效果。

## concat函数<a id="orgheadline18"></a>

字符串拼接函数
(concat "abc" "abc")

## substring函数<a id="orgheadline19"></a>

(substring "test" 0 2)
相当于python的 "test"[0:2]

## buffer-name<a id="orgheadline20"></a>

(buffer-name)
目前buffer的name

## buffer-file-name<a id="orgheadline21"></a>

(buffer-file-name)
目前buffer在系统的中的文件路径名

## load-file-name<a id="orgheadline22"></a>

load-file-name 返回该脚本所在的文件路径名，参考了 [这个网页](http://stackoverflow.com/questions/4088681/get-path-to-current-emacs-script-file-when-loaded-with-l-parameter) 。

## file-name-directory<a id="orgheadline23"></a>

如下面的代码将返回本脚本所在的目录路径，字符串形式。

```emacs-lisp
(file-name-directory load-file-name)
```

如果你需要将这个值存储进某个变量中，那么推荐使用defvar或defcustom。

## 读取某个文件内容<a id="orgheadline24"></a>

参考了 [这个网页](http://ergoemacs.org/emacs/elisp_read_file_content.html) 。

```emacs-lisp
(defun get-string-from-file (filePath)
  "Return filePath's file content."
  (with-temp-buffer
    (insert-file-contents filePath)
    (buffer-string)))
```

## if函数<a id="orgheadline25"></a>

if函数最简单的理解如下所示:

```lisp
CL-USER&gt; (if t 5 3)
5
CL-USER&gt; (if nil 5 3)
3
CL-USER&gt;
```

如果第二个元素估值为t，则返回第三个元素的值，如果是nil则返回第四个元素的值。然后第四个元素可以不填，也就是nil的时候什么都不做或者说返回nil。

## and<a id="orgheadline26"></a>

and是先evaluate一个，如果是真，那么going on to evaluate，如果是nil，那么返回nil。
and还有一个有趣的性质，那就是如果都为真，那么最后返回的不是t，而是最后那个信息的结果。

## or<a id="orgheadline27"></a>

or是先evaluate一个，如果是真就report，同样返回这个信息的结果，如果是nil，keep going on to search。
(or nil nil 'apple 'blue)-&#x2014;>apple

## cond<a id="orgheadline28"></a>

cond函数相当于c语言的switch语句。

## defun定义自己的函数<a id="orgheadline29"></a>

在lisp中讲到定义函数就不得不提lambda表达式，对lambda表达式有兴趣的请上网搜索相关信息了解之。简单来说就是如这样的 `(lambda (x) (* x x))` 一种匿名函数表示方法。该列表第二项定义的该函数的入口参数，然后第三项定义的是该函数的结果返回形式。对应的通过 **defun** 来定义自己的函数如下所示:

```lisp
(defun square (x) (* x x))
```

通过defun定义的有名函数，底层实质就是lambda函数机制，不过是给具体的那个lambda函数对象赋了一个名字罢了。我们前面说道lisp在eval一个链表的时候，其第一项将被默认认为是一个函数对象，其实质就是指向了一个lambda函数对象。

elisp下的defun多了两个内容，一是文档，其实可选的:

    (defun multiply-by-seven (number)
    "Multiply NUMBER by seven."
    (* 7 number))

二是对用户接口的开放，其也是可选的，interactive函数，这个后面再谈论。

    (defun function-name (arguments...)
    "optional-documentation..."
    (interactive argument-passing-info)
    body...)

## let创建局部变量<a id="orgheadline30"></a>

let 主要用于创造local  variables

let 在body中遇到不认识的变量了，首先在自己内部找，如果找不到，那么在global variable中找。
然后没定义一个defun其函数内部都有自己独立的语境，即用自己的局域变量，找不到就用广义变量。还找不到就说出现错误

let\*和let的区别就是一次只运算赋值一个本地变量，然后再第二个。也就是说如果第二个的赋值依赖于第一个的话，那么推荐用let\*。比如说我先赋值r，然后赋值面积等于2 \* pai\*r，那么第二个赋值就依赖于第二个。这种情况用let就会出现错误。但是编程一般用let，为了竟可能减少程序间的依赖关系，方便理解

## 基本lisp链表操作元函数<a id="orgheadline31"></a>

也就是car cdr caddr 之类的，elisp同样也是支持的。

(cadr '(1 2 3))
=> 2

cadr 等于 second 

(second '(1 2 3))

caddr 等于 third 

(third '(1 2 3))
=> 3

然后 cons list append 函数，这些也是很基本的，elisp同样也支持。

cons这个命令就是创建cons cell结构，通常用于把元素添加到列表头上。
(cons "a" '("b" "c"))
=> ("a" "b" "c")

list命令就是创建一个列表，将这些元素用括号包围起来:
(list 1 2 3)
=> (1 2 3)

append命令用于往列表后面加入某个元素:
(append '(5 4) '(3))
=> (5 4 3)
需要注意的是第二个元素必须是列表，所以append命令对应可以看作python中的两个列表的extend或者+操作。

值得一提的是append命令第二个元素如果不是列表，而是一个元素的话，程序不会出错，而是返回这样的dot list。
(append '("a") 1)
=> ("a" . 1)

这可以用于构建alist，然后cons命令如果第二个参数是元素，构建的也是这样的dot list:
(cons "a" 1)
=> ("a" . 1) 

然后append命令第一个元素必须是列表，否则会出现错误。
(append 'a '(b c))&#x2014;>error!!

## alist和plist<a id="orgheadline35"></a>

alist是这样的结构:
alist  ((key1 . value1)
  (key2 . value2)
  (key3 . value3))

plist 是这样的结构:
plist 
(key1 value1
  key2 value2
  key3 value3)

参看了 [这个网页](http://www.emacswiki.org/emacs/AlistVsPlist) ，alist可以简单来模拟类似python语言的字典结构，但如果需要考虑效率了，则推荐使用hash table结构。然后plist一般推荐在key不变的情况下使用。

### plist-get<a id="orgheadline32"></a>

提取plist的某个值:
(plist-get '(foo 4) 'foo)
=> 4

### assoc<a id="orgheadline33"></a>

提取alist的某个值:
(assoc 'key alist)

### assq<a id="orgheadline34"></a>

assq  alist的配套查询函数  类似 assoc 只是用 'eq' 替代了 'equal'

## reverse函数<a id="orgheadline36"></a>

reverse函数，列表翻转函数，这里强调的是列表的第一层元素:
(reverse '((a b) (c d) (e f)))
=> ((e f) (c d) (a b))

(reverse '(1 2 3))
=> (3 2 1)

## nth<a id="orgheadline37"></a>

提取列表的第几个元素:
(nth 0 '(a b c))
=> a

## nthcdr<a id="orgheadline38"></a>

cdr命令我们是知道的，nth就是做几次cdr命令。所以做0次就是原列表，做一次cdr等等。
需要注意的就是：
(cdr nil)
=> nil

也就是对空列表cdr还是空列表，所以如果cdr过头了就会得到nil，但是有一个例外，那就是dotted list。
因为dotted list是以一个元素作结尾，这样将会导致错误。因为cdr只能对列表进行操作。
(nthcdr 2 '(a b c))
=> (c)

## last<a id="orgheadline39"></a>

last返回的是列表的最后一个cons cell结构。
(last nil)&#x2014;>nil

对于正常的列表就是返回最后一个元素，不过是加了列表符号的。
(last '(a b c))&#x2014;>(c)

对于dotted list则是所谓的最后一个cons cell:
(last '("a" . 1)) -> '("a" . 1)
这是因为(c) 的完整结构是 [c|nil] 

## remove<a id="orgheadline40"></a>

remove就是把某个列表中出现的某个元素给移去。
(remove 'a '(b a n a n a))&#x2014;>(b n n)

## 集合相关函数<a id="orgheadline47"></a>

### member<a id="orgheadline41"></a>

member函数的作用就是核对某个value值是不是在后面列表中。如果是那么返回真值，包括开始为真的那个值也包括后面的元素。是假那么返回nil。

### intersection<a id="orgheadline42"></a>

交集

### union<a id="orgheadline43"></a>

补集

### set-difference<a id="orgheadline44"></a>

差集

### subsetp<a id="orgheadline45"></a>

判断第一个集合是不是第二个集合的子集，是就返回T，这里是确定的t。假返回nil。

### set-exclusive-or<a id="orgheadline46"></a>

XOR逻辑

# elisp进阶<a id="orgheadline76"></a>

## current-buffer<a id="orgheadline49"></a>

(current-buffer)
返回目前的buffer对象，(buffer-name)返回的只是当前buffer的名字。

## other-buffer<a id="orgheadline50"></a>

(other-buffer)
下一个buffer对象

## switch-to-buffer<a id="orgheadline51"></a>

编辑器切换buffer，这个函数是面向用户的，elisp程序员推荐使用 set-buffer。
(switch-to-buffer (other-buffer))

对应的快捷键是 C-x b

## buffer-size<a id="orgheadline52"></a>

(buffer-size)
当前buffer的size

## point对象<a id="orgheadline53"></a>

(point)

(point)其返回的(point)计数是从buffer的开始到目前cursor所做所包含的字符数。
12185  &#x2013; 12196 = 11 （这显示中文字符也是只占一个字符位，奇怪。）

(point-min)  1 一般都是1
(point-max)

通常用 (point-min) 到 (point-max) 来选中整个buffer的文本内容。

## interactive<a id="orgheadline54"></a>

(interactive)

这样你定义函数就可以通过 M-x 来执行了。在minibuffer下的回显可以通过 message 函数来做到。

如果是最简单的命令不需要输入参数，那么直接写上 (interactive) 即可，如果需要输入参数，具体情况很复杂，请参看 [这个网页](http://www.gnu.org/software/emacs/manual/html_node/elisp/Using-Interactive.html) 。

用prefix argument，比如下面这种写法:

    (defun multiply-by-seven (number)
    "Multiply NUMBER by seven."
    (interactive "p") 
    (message "The result is %d" (* 7 number)))

这里的小写字母 p 的意思是接受一个prefix 参数，数值型。或者大写字母 P（raw prefix argument）。然后具体使用是 `C-u 5 M-x commond` 。

这种用法我不太喜欢，还有一种参数定义方法，如下所示:

```elisp
(defun multiply-by-seven (number)
"Multiply NUMBER by seven."
(interactive "nplease input a number:\n") 
(message "The result is %d" (* 7 number)))
```

这里的第一个字母 `n` 的意思是接受一个数值参数，然后后面的字符都是提示信息文字， `\n` 表示结束，若要再定义一个参数则继续写:

```elisp
(defun multiply-by-seven (number str)
"Multiply NUMBER by seven."
(interactive "nplease input a number:\nsplease input a string:\n") 
(message "The result is %d" (* 7 number))
(message "your input is: %s" str))
```

当然一般用户接口不推荐很多参数，最多一个参数就有了。

## save-excursion<a id="orgheadline55"></a>

It saves the location of point and mark

C-SPC (set-mark-command). If a mark has been set, you can use the
command C-x C-x (exchange-point-and-mark)
set-mark-command

The mark is another position in the buffer; its value can be set with a com-
mand such as C-SPC (set-mark-command). If a mark has been set, you can use the
command C-x C-x (exchange-point-and-mark) to cause the cursor to jump to the
mark and set the mark to be the previous position of point. In addition, if you set
another mark, the position of the previous mark is saved in the mark ring. Many
mark positions can be saved this way. You can jump the cursor to a saved mark by
typing C-u C-SPC one or more times.
The part of the buffer between point and mark is called the region. Numerous
commands work on the region, including center-region, count-lines-region,
kill-region, and print-region.

In addition to recording the values of point and mark, save-excursion keeps
track of the current buffer, and restores it, too. This means you can write code that
will change the buffer and have save-excursion switch you back to the original
buffer.
In Emacs Lisp code, a save-excursion expression often occurs within the body
of a let expression. It looks like this:
(let varlist
(save-excursion
body&#x2026;))

## next-line<a id="orgheadline56"></a>

跳到下一行 对应快捷键 C-n

## mark-whole-buffer<a id="orgheadline57"></a>

也就是编辑器的全选命令。对应快捷键 C-x h

## subst<a id="orgheadline58"></a>

## sublis<a id="orgheadline59"></a>

## funcall<a id="orgheadline60"></a>

## mapcar<a id="orgheadline61"></a>

## lambda<a id="orgheadline62"></a>

## find-if<a id="orgheadline63"></a>

## remove-if-not<a id="orgheadline64"></a>

## remove-if<a id="orgheadline65"></a>

## reduce<a id="orgheadline66"></a>

## every<a id="orgheadline67"></a>

## incf<a id="orgheadline68"></a>

## decf<a id="orgheadline69"></a>

## push<a id="orgheadline70"></a>

## pop<a id="orgheadline71"></a>

## when<a id="orgheadline72"></a>

## unless<a id="orgheadline73"></a>

## dotimes 和dolist函数<a id="orgheadline74"></a>

这篇文章介绍了的函数有：
factorial -&#x2014;阶乘函数
fibonnaci&#x2013;&#x2014;斐波拉契数列函数
insert  &#x2014;&#x2014;插入函数
arrange  &#x2013;&#x2014;排列函数
while和until  宏

;;;while macro
(defmacro while (test  &rest body)
  \`(do ()
       ((not ,test))
       ,@body))

;;;until macro
(defmacro until (test &rest body)
  \`(do ()
       (,test)
       ,@body))

## 理解递归<a id="orgheadline75"></a>

> (defun our-member (obj lst)
   (if (null lst)
       nil
   (if (eql (car lst) obj)
       lst
       (our-member obj (cdr lst)))))
OUR-MEMBER

(defun median (list)
       (let ((sortlist (sort list #'<))
         (long (length list)))
         (if (oddp long) (nth (/ (- long 1) 2) sortlist) 
         (/ (+ (nth (- (/ long 2) 1) sortlist ) (nth (/ long 2) sortlist)) 2.0)))) 

defparameter

# 定义自己的包<a id="orgheadline77"></a>

(defun p (x y)
                          (cond  ((zerop y) 1)
                                     ((= y (1- x)) 1)
                                     (t  (+ (p (1- x) (1- y)) (p (1- x) y)))))

(defun pascal (n)
                          (loop  for  i  from 0  to (1- n)
                               collect (p n i)))

(defun pascal-triangle (x)
                          (loop for i from 1 to x
                             for s = '(1) then (pascal i)
                                 do  (format t "~&~s" s)))

(defmacro show-series (f a z &optional (step 1))
  \`(loop for n from ,a to ,z by ,step
for y = ,f
collect y ))

(defmacro sum (f a z &optional (step 1))
  \`(loop for n from ,a to ,z by ,step
for y = ,f
collect y into lst
finally (return (reduce #'+ lst))))

(defmacro product (f a z &optional (step 1))
  \`(loop for n from ,a to ,z by ,step
for y = ,f
collect y into lst
finally (return (reduce #'\* lst))))

(defmacro sum (f x a b &optional (step 1))
  \`(loop for ,x from ,a to ,b by ,step
for y = ,f
collect y into lst
finally (return (reduce #'+ lst)))

 (defmacro show-series (f x a z &optional (step 1))
  \`(loop for ,x from ,a to ,z by ,step
for y = ,f
collect y ))
(defmacro product (f x a z &optional (step 1))
   \`(loop for ,x from ,a to ,z by ,step
for y = ,f
 collect y into lst
 finally (return (reduce #'\* lst))))

 (defmacro s-integrate (f x a b &optional (n 100))
\`(let ((h (/ (- ,b ,a) ,n)))
  (\* (\* h 1/3) 
     (+ 
(let ((,x ,a)) 
    ,f)
      (\* 4 (sum ,f ,x (+ ,a h) ,b (\* 2 h)))
      (\* 2 (sum ,f ,x (+ ,a (\* 2 h)) (- ,b h) (\* 2 h)))
(let ((,x ,b))
  ,f)))))

# 附录<a id="orgheadline81"></a>

## emacs中使用common-lisp<a id="orgheadline78"></a>

在deb系系统中推荐直接用apt-get安装之:

```bash
apt-get install slime
```

这样安装之后连配置都不用配置了，直接输入 `M-x slime` 即可，不过你可能还没有装一个common-lisp的解释器，gnu的 `clisp` 或者 `sbcl` 都还行吧。

## 命令行执行emacs里面的命令<a id="orgheadline79"></a>

参考了 [这个网页](http://stackoverflow.com/questions/22072773/batch-export-of-org-mode-files-from-the-command-line) 。

如下所示，将以batch批处理模式加载test.org，然后执行命令"org-html-export-to-html" 。然后这里的 `-u` 是指定以某个用户的身份来运行emacs（主要是一些配置文件相关）。

```emacs-lisp
emacs test.org -u "$(id -un)" --batch  -f org-html-export-to-html
```

## 参考资料<a id="orgheadline80"></a>

1.  COMMON LISP: A Gentle Introduction to Symbolic Computation ; Author: David S. Touretzky
2.  [ANSI Common Lisp 中文](http://acl.readthedocs.org/en/latest/)

    (add-to-list 'load-path "~/workspace/myemacs/myorg/org")
    (require 'org)

add-to-list

```elisp
ELISP&gt; (setq x nil)
nil
ELISP&gt; (add-to-list 'x "a")
("a")

ELISP&gt; x
("a")
```

我们常见的 load-path 就是emacs启动时搜索插件路径的列表，所以我们加入某个搜索路径有如下命令:

    (add-to-list 'load-path "~/workspace/myemacs/myorg/org")

eval-after-load

eval-when-compile

declare-function

global-set-key