<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 额外的属性支持</a></li>
<li><a href="#orgheadline2">2. 某一列的额外的别名</a></li>
<li><a href="#orgheadline3">3. 多列组合唯一性约束</a></li>
<li><a href="#orgheadline4">4. ORM层的内省</a></li>
</ul>
</div>
</nav>


# 额外的属性支持<a id="orgheadline1"></a>

所谓的额外的属性并不是基于SQL表格的某一列的属性，而是在ORM之上建立起来的额外的属性，其一般是基于SQL表格的某一列或某些列的，是ORM封装之上提供的更加便利的属性接口。

```python
class EmailAddress(Base):
    __tablename__ = 'email_address'

    id = Column(Integer, primary_key=True)

    _email = Column("email", String)

    @hybrid_property
    def email(self):
        """Return the value of _email up until the last twelve
        characters."""

        return self._email[:-12]

    @email.setter
    def email(self, email):
        """Set the value of _email, tacking on the twelve character
        value @example.com."""

        self._email = email + "@example.com"
```

# 某一列的额外的别名<a id="orgheadline2"></a>

这里所谓的某一列额外的别名指并没有创建额外的列，而是在ORM层针对某一列可以用额外的别名来做类似的操作。

```python
from sqlalchemy.ext.declarative import synonym_for

class MyClass(Base):
    __tablename__ = 'my_table'

    id = Column(Integer, primary_key=True)
    status = Column(String(50))

    @synonym_for("status")
    @property
    def job_status(self):
        return "Status: " + self.status
```

其等于:

```python
class MyClass(Base):
    __tablename__ = 'my_table'

    id = Column(Integer, primary_key=True)
    status = Column(String(50))

    @property
    def job_status(self):
        return "Status: " + self.status

    job_status = synonym("status", descriptor=job_status)
```

也就是具体该列在ORM层可以通过 `status` 或者 `job_status` 来操作。具体参考 [这里](http://docs.sqlalchemy.org/en/latest/orm/mapped_attributes.html) 。

# 多列组合唯一性约束<a id="orgheadline3"></a>

请参看 [这个网页](http://stackoverflow.com/questions/10059345/sqlalchemy-unique-across-multiple-columns) 。

如果是ORM层，则是:

    class Location(Base):
        __tablename__ = 'locations'
        id = Column(Integer, primary_key = True)
        customer_id = Column(Integer, ForeignKey('customers.customer_id'), nullable=False)
        location_code = Column(Unicode(10), nullable=False)
        __table_args__ = (UniqueConstraint('customer_id', 'location_code', name='_customer_location_uc'),
                         )

上面flask\_sqlalchemy的话可以使用 `db.UniqueConstraint` 。 比如:

    __table_args__ = (
        db.UniqueConstraint("main_directory", "sub_directory","filename",
            "filext"),
        )

如果是Core层，则是:

    mytable = Table('mytable', meta,
        # ...
        Column('customer_id', Integer, ForeignKey('customers.customer_id')),
        Column('location_code', Unicode(10)),
    
        UniqueConstraint('customer_id', 'location_code', name='uix_1')
        )

# ORM层的内省<a id="orgheadline4"></a>

Table层直接利用已经存在的数据库表格就是 `reflect` 的概念，因为ORM层多了很多额外的东西，其中最关键的是 relationship 的概念，而sqlalchemy的Automap这一章主要就是解决ORM层内省这个问题的。更详细的讨论请参看 [官方文档](http://docs.sqlalchemy.org/en/rel_1_0/orm/extensions/automap.html) 。

最基本的应用就是 建立一个 `automap_base` 对象: 

    from sqlalchemy.ext.automap import automap_base
    
    Base = automap_base()

然后运行其 `prepare` 方法进行内省:

    Base.prepare(engine, reflect=True)

然后对应的sqlalchemy ORM层的那些类就可以如下获得了:

    User = Base.classes.user
    #或 Base.classes.get('user')

对于一般的属性引用，这是没有问题的。就是relationship可能还是有问题，那么我们可以预先定义一些属性，在 `prepare` 之前，那么预先定义的那些东西也将覆盖后面的自动reflect那部分定义，这可以起到矫正的作用。然后预先定义的那个类就是后面要使用的类了，就不要用 `Base.classes.what` 这种风格再获取了。