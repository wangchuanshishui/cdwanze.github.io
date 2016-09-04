gfm的官方文档在 [这里](https://help.github.com/articles/github-flavored-markdown/) 。本文大体简要说明一下。

关于markdown最基本的语法简介，我写了 [一篇文章](https://a358003542.gitbooks.io/markdown-learning-notes/content/) ，读者可以看一下。

github flavored markdown 也就是github的markdown方言，其主要区别有:

1.  下划线直接为下划线，下划线确实更多的是表现层而非内容层的东西，实际上org-mode我都希望下划线取消掉算了。

2.  URL 直接输入，比如 <http://www.google.com> ，其将直接转化成为链接。具体读者可以在 [这个网页](https://stackedit.io/editor) 上测试一下，其在google chrome里有个插件，叫 *StackEdit* 。这个只是一个新功能支持，实际上原来的链接插入方式一样有效。

3.  删除线 用:

    ~~删除线~~

属于添加的新特性。这个据我所指org-mode里面也是没有的。

1.  当然最有名的就是代码块的染色支持了。

    ```elisp
    (+ 1 1)
    ```

其中语言列表可以参看 [这里](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml) 。

1.  表格的额外特性支持，暂时我不太关心，略过了。

2.  html代码可以直接写进去，这个似乎讲起来markdown原义也是支持的。