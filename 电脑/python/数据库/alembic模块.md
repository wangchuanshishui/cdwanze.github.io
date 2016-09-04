<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. init</a></li>
<li><a href="#orgheadline3">2. revision</a>
<ul>
<li><a href="#orgheadline2">2.1. autogenerate的局限性</a></li>
</ul>
</li>
</ul>
</div>
</nav>

alembic模块基于SQLAlchemy模块，并建立了一种类似git的数据库版本控制机制。安装就用pip安装之。官方文档在 [这里](http://alembic.readthedocs.org/en/latest/index.html) 。

# init<a id="orgheadline1"></a>

一般在你的项目主文件夹下运行命令:

    alembic init alembic

后面的 `alembic` 是新建的文件夹名字，随意。

然后我们会看到 `alembic.ini` 这个文件，其内有个东西我们需要设置，那就是 `sqlalchemy.url` ，这个还是和flask那种处理风格一样，放入 `instance` 文件夹中，然后git不跟踪。然后后面讲到的所有 `alembic` 开头的命令，都应该如下使用:

    alembic -c instance/alembic.ini  ...

# revision<a id="orgheadline3"></a>

有点类似于git的commit吧。手工写那些觉得太麻烦了，先考虑使用 `autogenerate` 吧。然后就是 `env.py` 如下修改:

    import sys,os
    sys.path.append(os.path.abspath('.'))##add main folder
    from project.models import db
    target_metadata = db.metadata

然后我们就可以运行了:

    alembic -c instance/alembic.ini revision --autogenerate  -m 'init'

## autogenerate的局限性<a id="orgheadline2"></a>

autogenerate不是万能的，下面内容来自文档，需要了解一下，如果遇到不能解决的地方，那么就需要手工修改代码了。

可以解决的有:

-   表格增减
-   列增减
-   改变列nullable状态
-   索引的基本改变和明确的有名unique限定（>0.6.1）
-   foreign key限定的基本改变（>0.7.1）

可以部分解决的:

-   改变列的数据类型，如果你设置 `EnvironmentContext.configure.compare_type` to True，这大多数情况都工作得很好，但有个别情况可能不是很顺利。

-   改变默认server。如果你设置 `EnvironmentContext.configure.compare_server_default` to True。同样在某些情况可能会有问题。

不能解决的问题:

-   改变表格名字。你需要手工增减表格来完成之。
-   改变列的名字。类似上面。
-   匿名限定
-   特别的数据类型比如 `Enum`

这些还没解决将来要解决（0.8.6）

-   独立限定符的增减 比如 CHECK, PRIMARY KEY
-   序列的增减, （这里似乎指AUTO\_INCREMENT）