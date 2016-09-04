<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 魔兽争霸</a></li>
<li><a href="#orgheadline2">2. 魔兽世界</a></li>
<li><a href="#orgheadline3">3. 风暴英雄</a></li>
<li><a href="#orgheadline4">4. 星际争霸2</a></li>
<li><a href="#orgheadline5">5. 炉石传说</a></li>
<li><a href="#orgheadline6">6. 暗黑3</a></li>
<li><a href="#orgheadline11">7. 技术附录</a>
<ul>
<li><a href="#orgheadline7">7.1. 升级到最新的wine1.8</a></li>
<li><a href="#orgheadline8">7.2. wine换成32位</a></li>
<li><a href="#orgheadline9">7.3. 自建可运行的桌面图标</a></li>
<li><a href="#orgheadline10">7.4. 参考资料</a></li>
</ul>
</li>
</ul>
</div>
</nav>


# 魔兽争霸<a id="orgheadline1"></a>

具体就是用wine来运行之。魔兽争霸以前测试过，最早期的wine1.4就能够完美运行了。

# 魔兽世界<a id="orgheadline2"></a>

然后魔兽世界 wine1.6 我测试过，基本上运行没有任何问题。你需要做的就是把wine换成32位环境，下面会说的。然后推荐把系统图形驱动换成Navida官方闭源最新的那个。如果你只玩魔兽世界，那么就没有必要升级最新的wine1.8了，然后执行64位是不行的，直接运行那个32位的Wow.exe即可。然后你还需要做的就是将 `World of Warcraft/WTF` 这个文件夹删掉，并且给其可读可写权限。

    chmod -R 766 WTF

然后基本上就没有其他问题了，网上说的opengl设置没有必要了。

# 风暴英雄<a id="orgheadline3"></a>

升级到最新的wine1.8。（wine1.6我测试地面纹理渲染有问题。）

先下载battle.net的官方安装文件，用wine运行之，记得把 `dbghelp` 停用了，如下图所示:
![img](images/wine_停用dbghelp.png)

停用 `dbghelp` 是为了 battle.net 这个程序能够正常运行。如果你要玩炉石传说，事情可能会更加麻烦一点，如果不玩，那么这么配置之后就没问题了。

# 星际争霸2<a id="orgheadline4"></a>

虽然没有测试，但因为风暴英雄就是星际争霸2的引擎，我估计问题不大。

# 炉石传说<a id="orgheadline5"></a>

1.  升级到最新的wine1.8
2.  通过停用 `dbghelp` 把battle.net安装上。
3.  还是在wine的配置那里，把 `msvcp100` 添加上，如上面图片所示。
4.  运行  `winetricks wininet` , 不确定是不是必须的。

*特别提醒* :: 我测试还是会出错，然后把那个 `dbghelp` 又开启过来，不管是原装先于内建或者内建先于原装都行，就可以正常运行了。但是你第一次开启 battle.net的时候还需要再把那个 `dbghelp` 停用，没有办法。 最新的战网更新显示 `dbghelp` 就默认为原装先于内建然后一点问题都没有了。

# 暗黑3<a id="orgheadline6"></a>

没有测试。

# 技术附录<a id="orgheadline11"></a>

## 升级到最新的wine1.8<a id="orgheadline7"></a>

    sudo add-apt-repository ppa:ubuntu-wine/ppa
    sudo apt-get update
    sudo apt-get install wine1.8

## wine换成32位<a id="orgheadline8"></a>

如果你是64位系统，推荐将wine的整个环境都换成32位，先做好备份工作，然后将 `.wine` 这个文件夹删除。然后运行:

    WINEARCH=win32 WINEPREFIX=~/.wine winecfg

## 自建可运行的桌面图标<a id="orgheadline9"></a>

没有必要做了，wine会自动创建一个桌面图标，这里写上主要是ubuntu的技术细节吧:

1.  新建一个 battlenet.desktop文件

    sudo gedit ~/.local/share/applications/battlenet.desktop

    [Desktop Entry]
    Name=battlenet
    Exec=wine "C:\\Program Files\\Battle.net\\Battle.net.exe"
    Icon=battlenet.png
    Terminal=false
    Type=Application
    Categories=Application;Game;
    StartupNotify=false

1.  弄一个 battlenet.png 图片放到主文件夹的 `.icons` 文件夹里面，没有则新建。

然后在ubuntu左上角开始搜索，你就可以看到这个运行图标了。通过 `ln -s` 创建软链接到那个desktop文件则可以生成桌面点击方式。

## 参考资料<a id="orgheadline10"></a>

1.  [<http://www.webupd8.org/2014/09/how-to-install-world-of-warcraft-in.html>](http://www.webupd8.org/2014/09/how-to-install-world-of-warcraft-in.html)