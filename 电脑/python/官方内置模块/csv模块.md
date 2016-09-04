<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 简介</a></li>
<li><a href="#orgheadline2">2. 方言总的讨论</a></li>
<li><a href="#orgheadline3">3. 我写的sv方言</a></li>
<li><a href="#orgheadline4">4. 另外两个类接口</a></li>
<li><a href="#orgheadline5">5. 测试例子</a></li>
</ul>
</div>
</nav>


# 简介<a id="orgheadline1"></a>

csv（Comma Separated Values），逗号分隔值文件格式。虽然名字是逗号分隔值，而且csv的[RFC 4180标准](http://tools.ietf.org/html/rfc4180.html) 也要求csv文件用逗号作为分隔，但我感觉这实际上降低了csv的灵活性，我更愿意接受一种广义的csv标准作为小型数据（主要侧重表格数据）的存储和交互方案。

我给自己定义的一种csv方言如下所示：

1.  换行符表示每一行，每一行一条记录。我想这可能是所有csv都统一的一条，所以csv文件最好叫做行记录文件？
2.  如果数据是数值那么只有float类型，不需要加双引号。法文的csv小数是这种 `3,14159` ，这也太不规范了，应该废弃。小数统一为点标记， `3.14` 。然后float型都需要加上.标记，即使是 `3` 这样的形式，也应写为 `3.0` 这样的形式。
3.  如果数据是字符串，那么必须用双引号标记。
4.  为了控制csv文件的简单性，除了float，str之外的不再提供额外的数据类型支持了。
5.  基于前面的描述，那么每一行的记录实际上不加额外的分隔符，就使用空白字符（空格），各个数据也能很好的表示出来了。
6.  整个csv数据视作一个列表，然后每一行视作列表的子元素，每一个子元素也是一个列表，表头为第一行。即这样的形式：[[表头],[],[]&#x2026;]
7.  True,False会写成"True" "False"，None 对应"" 即空字符串。

# 方言总的讨论<a id="orgheadline2"></a>

python3的官方文档链接在[这里](https://docs.python.org/3.4/library/csv.html) ，wiki的csv页面对于基本规则讨论比较好了，链接在[这里](http://zh.wikipedia.org/zh/%E9%80%97%E5%8F%B7%E5%88%86%E9%9A%94%E5%80%BC) 。那里讨论的规则主要是狭义的csv规则，比如必须逗号作为分隔等等。下面将讨论各种csv方言，也就是作为广义的csv来讨论。最后讨论我上面提及的我喜欢的那种csv方言。

python csv模块默认的csv方言是 `excel` ，其定义如下所示：

    class excel(Dialect):
        """Describe the usual properties of Excel-generated CSV files."""
        delimiter = ','
        quotechar = '"'
        doublequote = True
        skipinitialspace = False
        lineterminator = '\r\n'
        quoting = QUOTE_MINIMAL
    register_dialect("excel", excel)

一般程式导出的csv文件都是对应这里的excel方言，比如分隔符(delimiter)是逗号；引号符号(quotechar)是双引号；doublequote用于处理双引号在字符中的情况，如果设置为True，那么下面的情况：

    1997,Ford,E350,"Super, ""luxurious"" truck"

第四项将会被正确处理。一般设置为True吧。

skipinitialspace选项，默认是False，因为这里是逗号作为分隔符。在空格作为分隔符时还有点意义，此时额外的空格将会被忽略。

lineterminator选项，对于这个 `\r\n` 看不太懂，一般就是 `\n` 吧。

quoting选项，这个选项有几个设置值：

-   csv.QUOTE\_MINIMAL 意思是只有在需要的情况下才加上双引号，比如逗号在字符串里面，双引号在字符串里面，换行符号在字符串里面等等。
-   csv.QUOTE\_ALL 意思是都加上双引号，即使是数字。
-   csv.QUOTE\_NONNUMERIC 数字不加，字符串都加上双引号。（只有在这种情况下csv模块才会正确将数字解析为float类型）
-   csv.QUOTE\_NONE 都不加（此时需要设置好escapechar选项）

# 我写的sv方言<a id="orgheadline3"></a>

具体代码如下所示：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

class sv(csv.Dialect):
    delimiter = ' '#一个空格
    quotechar = '"'
    doublequote = True
    skipinitialspace = True
    lineterminator = '\n'
    quoting = csv.QUOTE_NONNUMERIC


csv.register_dialect("sv", sv)
```

其继承自csv的Dialect类，然后通过csv模块的register\_dialect函数进行注册。

类里面就是前面谈及的一些参数设置，具体就是我在上面谈论的最简化的csv格式：delimiter设置为一个空格，skipinitialspace设置为True，这是必要的。然后重要的quoting设置为 `csv.QUOTE_NONNUMERIC` ，让除数字外的都加上双引号。

# 另外两个类接口<a id="orgheadline4"></a>

此外还写了两个类接口，提供了一些方便的查看或设置数据的接口。

```python
class Reader():
    def __init__(self,f,dialect='sv'):
        self.lines = []
        for line in csv.reader(f, dialect):
            line = [self.to_float(e) for e in line]
            self.lines.append(line)

    def getrow(self,num):
        return self.lines[num-1]

    def getcol(self,head):
        index = self.getrow(1).index(head)
        lst = []
        for line in self.lines:
            lst.append(line[index])
        return lst

    def getdata(self):
        return self.lines

    @staticmethod
    def to_float(e):
        try:
            return float(e)
        except ValueError:
            return e

class Writer():
    def __init__(self,f,dialect='sv'):
        self.lines = []
        self.writer = csv.writer(f, dialect)

    def addrow(self,row):
        self.lines.append(row)

    def addcol(self,col):
        for index in range(len(self.lines)):
            self.lines[index].append(col[index])

    def setrow(self,num,row):
        self.lines[num-1] = row
    def setcol(self,num,col):
        for index in range(len(self.lines)):
            self.lines[index][num-1] = col[index]

    def set(self,row,col,e):
        self.lines[row-1][col-1] = e

    def setdata(self,data):
        self.lines = data

    def write(self):
        for line in self.lines:
            self.writer.writerow(line)
```

# 测试例子<a id="orgheadline5"></a>

根据上面的谈论，我们进行了如下测试例子：

```python
from wanze.csv import Reader,Writer

with open('test.csv',newline='') as f:
    reader = Reader(f,'excel')
    data = reader.getdata()
    print(data)

with open('test2.csv','w',newline='') as f:
    writer = Writer(f,'sv')
    writer.setdata(data)
    writer.write()

with open('test2.csv',newline='') as f:
    reader = Reader(f)
    data = reader.getdata()
    print(data)
```

其中test.csv你随便找一个csv文件即可，这里假设它是最常见的excel csv格式，然后读入，然后将其写成前面提及的sv（Reader和Writer类的默认dialect），然后在读入。读者可以自己检验测试以下。

关于Reader和Writer类，提供了很多对应的函数接口，比如Reader类有

-   getrow 取某一行的值
-   getcol 取某一列的值
-   getdata 取整个表格的数据值，如下形式

    [['x', 'y'], [1.0, 2.0], [3.0, 4.0], [4.5, 5.5]]

关于Writer类有：

-   addrow 添加一行值
-   addcol 添加一列值
-   set 设置某行某列的某个值为什么
-   setdata 设置整个表格为，即为如下形式[[][]&#x2026;]
-   write 实际写入到文件中去。