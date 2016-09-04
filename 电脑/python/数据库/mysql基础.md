<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 简介</a></li>
<li><a href="#orgheadline16">2. mysql入门</a>
<ul>
<li><a href="#orgheadline2">2.1. 登录</a></li>
<li><a href="#orgheadline3">2.2. mysql数据库</a></li>
<li><a href="#orgheadline4">2.3. 查看数据库情况</a></li>
<li><a href="#orgheadline5">2.4. 切换数据库</a></li>
<li><a href="#orgheadline6">2.5. 查看表格情况</a></li>
<li><a href="#orgheadline7">2.6. 简单检索某个表格</a></li>
<li><a href="#orgheadline8">2.7. 创建用户</a></li>
<li><a href="#orgheadline9">2.8. 删除用户</a></li>
<li><a href="#orgheadline10">2.9. 更新记录</a></li>
<li><a href="#orgheadline11">2.10. 创建数据库</a></li>
<li><a href="#orgheadline12">2.11. 创建表格</a></li>
<li><a href="#orgheadline13">2.12. 插入数据</a></li>
<li><a href="#orgheadline14">2.13. 删除table</a></li>
<li><a href="#orgheadline15">2.14. 删除database</a></li>
</ul>
</li>
<li><a href="#orgheadline25">3. mysql进阶</a>
<ul>
<li><a href="#orgheadline17">3.1. 创建表格</a></li>
<li><a href="#orgheadline24">3.2. 插入数据</a>
<ul>
<li><a href="#orgheadline18">3.2.1. 子查询</a></li>
<li><a href="#orgheadline19">3.2.2. insert where语句</a></li>
<li><a href="#orgheadline20">3.2.3. 交叉连接</a></li>
<li><a href="#orgheadline21">3.2.4. 内连接</a></li>
<li><a href="#orgheadline22">3.2.5. union all</a></li>
<li><a href="#orgheadline23">3.2.6. 不能重复刷的部分</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#orgheadline26">4. 别名</a></li>
<li><a href="#orgheadline27">5. 去除重复的行</a></li>
<li><a href="#orgheadline30">6. 附录</a>
<ul>
<li><a href="#orgheadline28">6.1. 演示例子的补充信息</a></li>
<li><a href="#orgheadline29">6.2. 参考资料</a></li>
</ul>
</li>
</ul>
</div>
</nav>


# 简介<a id="orgheadline1"></a>

本文已经假设读者对sql有一个初步的认识了，然后更加具体的讨论mysql的相关细节。安装在ubuntu下就简单用apt-get安装之，如下所示，不赘述了。

```bash
sudo apt-get  install mysql-server mysql-client
```

# mysql入门<a id="orgheadline16"></a>

本小节的代码依次演示了第一个例子，好让读者对mysql有个初步的认识。

## 登录<a id="orgheadline2"></a>

以root用户登录

    mysql -u root -p

具体密码是多少要根据你安装mysql时的情况来，若没有设置密码则直接按Enter。

## mysql数据库<a id="orgheadline3"></a>

mysql里面默认有个和自身配置相关的数据库，名字就叫做mysql。

## 查看数据库情况<a id="orgheadline4"></a>

```mysql
show databases;
```

## 切换数据库<a id="orgheadline5"></a>

我们先切换到那个mysql数据库看一下。

```mysql
use mysql;
```

## 查看表格情况<a id="orgheadline6"></a>

```mysql
show tables;
```

上面描述的这些过程你也可以用GUI程序（比如 **emma** 等）来点开看一下。我们先看到user这个表格，这个表格里面存储着mysql用户的一些信息。

## 简单检索某个表格<a id="orgheadline7"></a>

```mysql
select * from user;
```

因为内容较多，可能显示效果不太好。

## 创建用户<a id="orgheadline8"></a>

给user表格插入一条记录实际上就是新建一个新的mysql用户，如下所示:

```mysql
insert into user(host,user,password,select_priv,insert_priv)
values('localhost','wanze',password('123456'),'Y','Y');
```

## 删除用户<a id="orgheadline9"></a>

给user表格删除一条记录就是删除某个mysql用户，让我们把前面创建的这个用户删除了:

```mysql
delete from user where user = 'wanze';
```

好吧，继续再把那个用户加进去，然后我们注意到之前只给了那个用户select和insert的权限的，现在让我们再多给他几个权限。

## 更新记录<a id="orgheadline10"></a>

```mysql
mysql&gt; update user
    -&gt; set update_priv = 'Y',
    -&gt; delete_priv = 'Y',
    -&gt; create_priv = 'Y',
    -&gt; drop_priv = 'Y'
    -&gt; where user = 'wanze';
```

现在这个用户又新加上了update，delete，create和drop权限了。然后我们看到用户还有很多其他权限设置，

然后还有一种方式是赋予该用户之于某个数据库所有的权限。

```mysql
grant all privileges on test.* to 'test'@'localhost';
```

这里的test是具体的database name，第二个test是新加入的用户名【这里后面还可以加上 identified by 'thepassword' 来控制新加用户的密码。】。这种方式除了user里面加入了test这个新用户之外，在mysql数据库的db表格里面还加入了一条新的记录。前面那种用户设置权限的应该是对所有数据库都有权限，而这里只针对某一数据库有权限。具体权限管理还有很多内容，这里先略过了。

## 创建数据库<a id="orgheadline11"></a>

我们先创建一个新的数据库:

```mysql
create database test;
```

## 创建表格<a id="orgheadline12"></a>

```mysql
mysql&gt; create table test(x int,y integer,z integer);
```

这里就简单创建了一个名叫test的表格，然后定义表头为三个整数，integer和int是一个意思。

## 插入数据<a id="orgheadline13"></a>

插入数据和其他sql数据库一样还是insert into这样的语句格式。

```mysql
mysql&gt; insert into test(x,y,z) values(1,2,3) ;
```

第一个例子就到这里了，简单了解了一下mysql的情况，下面继续详细的讨论。

## 删除table<a id="orgheadline14"></a>

```mysql
drop table test;
```

## 删除database<a id="orgheadline15"></a>

```mysql
drop database test;
```

至此我们新建的那个数据库的所有信息都被删除了，下面进入第二个例子，我们将建立更具有现实意义的数据库。

# mysql进阶<a id="orgheadline25"></a>

第二个例子绝不是一个很小型的例子，而是一个几乎涉及mysql数据库方方面面的例子，内容是很丰富的，我们慢慢继续下去吧。

首先创建learning\_example database。然后创建一个student用户，其对learning\_example database拥有所有的权限。

```mysql
mysql -u root
mysql&gt; create database learning_example;
mysql&gt; grant all privileges on learning_example.* to 'student'@'localhost';
```

## 创建表格<a id="orgheadline17"></a>

写好sql语句文件然后刷进去，如下所示:

    mysql -u student learning_example < mysql_learning_example.sql

这里的 `-u` 接用户名，然后后面跟要操作的database名字。

现在这个文件就简单写上这么一句:

```mysql
create table department
 (dept_id smallint unsigned not null auto_increment,
  name varchar(20) not null,
  constraint pk_department primary key (dept_id)
 );
```

这里前面的意思是很明显的，就是新建department这个table，然后定义一列dept\_id ，其为 `smallint` ， `unsigned` （就是从0到65535），然后 `not null` 说这列不能为空，然后 `auto_increment` 说这列的数值自动增加（主要是主键id需要这个）；然后name这一列是 `varchar(20)` ，是变长字符串，最大长度20，类似的还有 `char(20)` ，其为定长字符串，后面都会 <span class="underline">自动填充空格</span> ，同样not null限定非空。然后后面的约束语句需要额外说一下。

`constraint` 是约束的意思，然后后面跟pk\_department（这个名字貌似是随意的）指约束department这个table的primary key，后面跟上primary key (dept\_id) ，即约束table department的主键值为 `dept_id` 这一列。

继续往下讨论，现在文件改成这个样子:

```mysql
create table if not exists department
 (dept_id smallint unsigned not null auto_increment,
  name varchar(20) not null,
  constraint pk_department primary key (dept_id)
 );

 create table if not exists branch
 (branch_id smallint unsigned not null auto_increment,
  name varchar(20) not null,
  address varchar(30),
  city varchar(20),
  state varchar(2),
  zip varchar(12),
  constraint pk_branch primary key (branch_id)
 );
```

注意前面的创建department表格语句那里加上了 `if not exists` ，这样如果表格不存在才会新建该table，从而避免了sql文件重复刷的时候出错。下面那个新建branch表格的sql语句并没有增加新的东西，所以我们继续往下看。

```mysql
create table if not exists employee
 (emp_id smallint unsigned not null auto_increment,
  fname varchar(20) not null,
  lname varchar(20) not null,
  start_date date not null,
  end_date date,
  superior_emp_id smallint unsigned,
  dept_id smallint unsigned,
  title varchar(20),
  assigned_branch_id smallint unsigned,
  constraint fk_e_emp_id
    foreign key (superior_emp_id) references employee (emp_id),
  constraint fk_dept_id
    foreign key (dept_id) references department (dept_id),
  constraint fk_e_branch_id
    foreign key (assigned_branch_id) references branch (branch_id),
  constraint pk_employee primary key (emp_id)
 );
```

我们继续来看这个创建employee table语句，fname是first name的缩写，然后lname是lastname的缩写。start\_date和end\_date应该是雇佣时间和解聘时间的意思，其中解聘时间可以为空，就说明该雇员还在公司工作。然后其都为 `date` 数据类型。值得一提的是mysql的date类型只能存储公元前1000年到公元9999年之间的date。

后面superior\_emp\_id是该雇员的上司的id号，然后dept\_id是该雇员所在部门号，然后assigned\_branch\_id是对于该雇员分配的分公司id号。该table的约束主键值是emp\_id。

接下来重点讲一下 `foreign key` 约束的写法。

    constraint fk_e_emp_id
      foreign key (superior_emp_id) references employee (emp_id),

这里fk\_e\_emp\_id这个名字带有一定的随意性，大致表达出fk\_然后某个table下的某一列即可。然后 foreign key 外键值 (superior\_emp\_id) 即这一列是外键值，具体references 引用自 employee 这个表格的(emp\_id) 这一列。总的意思就是superiro\_emp\_id这一列是一个外键值约束列，其值只可能取自employee表格的emp\_id这一列，因为这里具体的逻辑含义就是其值引用自它。比如说雇员张三在这里的id是3，张三的上司是张三丰，其id是4。那么张三如果要修改自己的上司值，就必须是本雇员列表已经有了的id号的其他雇员。（外键引用主要用于SQL表格中所谓的one to many 或者 many to one 的情况，具体就是用内连接查询，这样该外键值约束列的可能对应取值是另外一个表格的很多列，这个后面再详细讨论。）

继续刷下去，强烈推荐读者用emma或者其他什么GUI程序来实时查看一下:

```mysql
create table if not exists product_type
 (product_type_cd varchar(10) not null,
  name varchar(50) not null,
  constraint pk_product_type primary key (product_type_cd)
 );

 create table if not exists product
 (product_cd varchar(10) not null,
  name varchar(50) not null,
  product_type_cd varchar(10) not null,
  date_offered date,
  date_retired date,
  constraint fk_product_type_cd foreign key (product_type_cd)
    references product_type (product_type_cd),
  constraint pk_product primary key (product_cd)
 );

 create table if not exists customer
 (cust_id integer unsigned not null auto_increment,
  fed_id varchar(12) not null,
  cust_type_cd enum('I','B') not null,
  address varchar(30),
  city varchar(20),
  state varchar(20),
  postal_code varchar(10),
  constraint pk_customer primary key (cust_id)
 );

 create table if not exists individual
 (cust_id integer unsigned not null,
  fname varchar(30) not null,
  lname varchar(30) not null,
  birth_date date,
  constraint fk_i_cust_id foreign key (cust_id)
    references customer (cust_id),
  constraint pk_individual primary key (cust_id)
 );

 create table if not exists business
 (cust_id integer unsigned not null,
  name varchar(40) not null,
  state_id varchar(10) not null,
  incorp_date date,
  constraint fk_b_cust_id foreign key (cust_id)
    references customer (cust_id),
  constraint pk_business primary key (cust_id)
 );


 create table if not exists officer
 (officer_id smallint unsigned not null auto_increment,
  cust_id integer unsigned not null,
  fname varchar(30) not null,
  lname varchar(30) not null,
  title varchar(20),
  start_date date not null,
  end_date date,
  constraint fk_o_cust_id foreign key (cust_id)
    references business (cust_id),
  constraint pk_officer primary key (officer_id)
 );

 create table if not exists account
 (account_id integer unsigned not null auto_increment,
  product_cd varchar(10) not null,
  cust_id integer unsigned not null,
  open_date date not null,
  close_date date,
  last_activity_date date,
  status enum('ACTIVE','CLOSED','FROZEN'),
  open_branch_id smallint unsigned,
  open_emp_id smallint unsigned,
  avail_balance float(10,2),
  pending_balance float(10,2),
  constraint fk_product_cd foreign key (product_cd)
    references product (product_cd),
  constraint fk_a_cust_id foreign key (cust_id)
    references customer (cust_id),
  constraint fk_a_branch_id foreign key (open_branch_id)
    references branch (branch_id),
  constraint fk_a_emp_id foreign key (open_emp_id)
    references employee (emp_id),
  constraint pk_account primary key (account_id)
 );

 create table if not exists transaction
 (txn_id integer unsigned not null auto_increment,
  txn_date datetime not null,
  account_id integer unsigned not null,
  txn_type_cd enum('DBT','CDT'),
  amount double(10,2) not null,
  teller_emp_id smallint unsigned,
  execution_branch_id smallint unsigned,
  funds_avail_date datetime,
  constraint fk_t_account_id foreign key (account_id)
    references account (account_id),
  constraint fk_teller_emp_id foreign key (teller_emp_id)
    references employee (emp_id),
  constraint fk_exec_branch_id foreign key (execution_branch_id)
    references branch (branch_id),
  constraint pk_transaction primary key (txn_id)
 );
```

这里值得一讲的有:

    cust_type_cd enum('I','B') not null,

mysql的枚举类型，在这里cust\_type\_cd这一列只能取'I'和'B'这两个值。

## 插入数据<a id="orgheadline24"></a>

现在我们加入如下代码:

```mysql
insert into department (dept_id, name)
values (null, 'Operations');
insert into department (dept_id, name)
values (null, 'Loans');
insert into department (dept_id, name)
values (null, 'Administration');
```

department的dept\_id已经打开了auto\_increment特性，那么简单的给这一列赋值 `null` 即可，其会自动添加一个主键数字。

在前面创建表格的时候有if not exists逻辑，这样sql脚本可以重复刷都没有问题，那么插入数据也有这样的if not exists逻辑吗？请参看 [这个网页](http://bogdan.org.ua/2007/10/18/mysql-insert-if-not-exists-syntax.html) 。我们可以使用 `insert ignore` 语句来避免重复插入，这是插入语句改成这个样子了:

```mysql
insert ignore into department (dept_id, name)
values (1, 'Operations');
insert ignore into department (dept_id, name)
values (2, 'Loans');
insert ignore into department (dept_id, name)
values (3, 'Administration');
```

注意这里id直接赋值了，因为其为primarykey，如果设置为null这里的语句还是会重复插入，只有primarykey重复了，这个insert语句才不会继续插入了。

让我继续插入一些数据:

```mysql
insert ignore into branch (branch_id, name, address, city, state, zip)
values (1, 'Headquarters', '3882 Main St.', 'Waltham', 'MA', '02451');
insert ignore into branch (branch_id, name, address, city, state, zip)
values (2, 'Woburn Branch', '422 Maple St.', 'Woburn', 'MA', '01801');
insert ignore into branch (branch_id, name, address, city, state, zip)
values (3, 'Quincy Branch', '125 Presidential Way', 'Quincy', 'MA', '02169');
insert ignore into branch (branch_id, name, address, city, state, zip)
values (4, 'So. NH Branch', '378 Maynard Ln.', 'Salem', 'NH', '03079');
```

上面没啥好讲的，然后我们看到下面这句:

```mysql
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (1, 'Michael', 'Smith', '2001-06-22',
  (select dept_id from department where name = 'Administration'),
  'President',
  (select branch_id from branch where name = 'Headquarters'));
```

### 子查询<a id="orgheadline18"></a>

SQL有三种类型的表: 一种是大家常见的实际存储的那种SQL表格；第二种是临时表格，也就是子查询返回的表格；还有一种就是虚拟表，比如视图。

所谓的子查询实际上就是一个select语句其将返回一个临时的SQL表格，最简单的应用就是直接跟在另一个select语句的from语句后面，然后还有一种用法常用于表格多列值的复制转移操作，也就是所谓的 `insert select` 语句，其是由一个insert语句和一个select语句组合而成。如下所示<sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup>:

    INSERT INTO Customers (CustomerName, Country)
    SELECT SupplierName, Country FROM Suppliers;

这个SQL语句将把Suppliers表格里面的SupplierName和Country这两列的值都复制到Customers这个表格中去，具体是对应的CustomerName和Country这两列。

而上面的例子就是第三种用法，其是一个select语句然后 <span class="underline">用括号()括起来了</span> 。其需要返回一列值，然后像上面的情况必须是只有一个值，而这个值将提取出来被insert into语句作为value使用，然后也有返回多个值的情况，比如过滤条件where what in (select &#x2026;) ，这种子查询就可以返回多个值。

下面类似的这些语句就不赘述了:

```mysql
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (2, 'Susan', 'Barker', '2002-09-12',
  (select dept_id from department where name = 'Administration'),
  'Vice President',
  (select branch_id from branch where name = 'Headquarters'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (3, 'Robert', 'Tyler', '2000-02-09',
  (select dept_id from department where name = 'Administration'),
  'Treasurer',
  (select branch_id from branch where name = 'Headquarters'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (4, 'Susan', 'Hawthorne', '2002-04-24',
  (select dept_id from department where name = 'Operations'),
  'Operations Manager',
  (select branch_id from branch where name = 'Headquarters'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (5, 'John', 'Gooding', '2003-11-14',
  (select dept_id from department where name = 'Loans'),
  'Loan Manager',
  (select branch_id from branch where name = 'Headquarters'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (6, 'Helen', 'Fleming', '2004-03-17',
  (select dept_id from department where name = 'Operations'),
  'Head Teller',
  (select branch_id from branch where name = 'Headquarters'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (7, 'Chris', 'Tucker', '2004-09-15',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Headquarters'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (8, 'Sarah', 'Parker', '2002-12-02',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Headquarters'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (9, 'Jane', 'Grossman', '2002-05-03',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Headquarters'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (10, 'Paula', 'Roberts', '2002-07-27',
  (select dept_id from department where name = 'Operations'),
  'Head Teller',
  (select branch_id from branch where name = 'Woburn Branch'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (11, 'Thomas', 'Ziegler', '2000-10-23',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Woburn Branch'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (12, 'Samantha', 'Jameson', '2003-01-08',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Woburn Branch'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (13, 'John', 'Blake', '2000-05-11',
  (select dept_id from department where name = 'Operations'),
  'Head Teller',
  (select branch_id from branch where name = 'Quincy Branch'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (14, 'Cindy', 'Mason', '2002-08-09',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Quincy Branch'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (15, 'Frank', 'Portman', '2003-04-01',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Quincy Branch'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (16, 'Theresa', 'Markham', '2001-03-15',
  (select dept_id from department where name = 'Operations'),
  'Head Teller',
  (select branch_id from branch where name = 'So. NH Branch'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (17, 'Beth', 'Fowler', '2002-06-29',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'So. NH Branch'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (18, 'Rick', 'Tulman', '2002-12-12',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'So. NH Branch'));
```

我们继续往下看:

```mysql
create temporary table emp_tmp as
select emp_id, fname, lname from employee;

update employee set superior_emp_id =
 (select emp_id from emp_tmp where lname = 'Smith' and fname = 'Michael')
where ((lname = 'Barker' and fname = 'Susan')
  or (lname = 'Tyler' and fname = 'Robert'));
```

这里的 `create temporary table` 语句是根据某个select语句创建了一个临时表格，临时表格只有当前的session看得到，退出session之后该临时表格会自动drop掉。

update语句基本格式我们是熟悉的，关键是理解where字句这个过滤条件。该SQL语句的意思是:将employee表格中Barker Susan和Tyler Robert这两个伙计的上司设置为Michael Smith的emp\_id。这里的过滤条件or逻辑还有and逻辑我想熟悉编程的都很清楚了，这里就不赘述了。

下面情况类似:

```mysql
update employee set superior_emp_id =
 (select emp_id from emp_tmp where lname = 'Tyler' and fname = 'Robert')
where lname = 'Hawthorne' and fname = 'Susan';
update employee set superior_emp_id =
 (select emp_id from emp_tmp where lname = 'Hawthorne' and fname = 'Susan')
where ((lname = 'Gooding' and fname = 'John')
  or (lname = 'Fleming' and fname = 'Helen')
  or (lname = 'Roberts' and fname = 'Paula') 
  or (lname = 'Blake' and fname = 'John') 
  or (lname = 'Markham' and fname = 'Theresa')); 
update employee set superior_emp_id =
 (select emp_id from emp_tmp where lname = 'Fleming' and fname = 'Helen')
where ((lname = 'Tucker' and fname = 'Chris') 
  or (lname = 'Parker' and fname = 'Sarah') 
  or (lname = 'Grossman' and fname = 'Jane'));  
update employee set superior_emp_id =
 (select emp_id from emp_tmp where lname = 'Roberts' and fname = 'Paula')
where ((lname = 'Ziegler' and fname = 'Thomas')  
  or (lname = 'Jameson' and fname = 'Samantha'));   
update employee set superior_emp_id =
 (select emp_id from emp_tmp where lname = 'Blake' and fname = 'John')
where ((lname = 'Mason' and fname = 'Cindy')   
  or (lname = 'Portman' and fname = 'Frank'));    
update employee set superior_emp_id =
 (select emp_id from emp_tmp where lname = 'Markham' and fname = 'Theresa')
where ((lname = 'Fowler' and fname = 'Beth')   
  or (lname = 'Tulman' and fname = 'Rick'));    

drop table emp_tmp;
```

然后加入product和product\_type的数据，看了一下，没啥好说的:

```mysql
/* product type data */
insert ignore into product_type (product_type_cd, name)
values ('ACCOUNT','Customer Accounts');
insert ignore into product_type (product_type_cd, name)
values ('LOAN','Individual and Business Loans');
insert ignore into product_type (product_type_cd, name)
values ('INSURANCE','Insurance Offerings');


/* product data */
insert ignore into product (product_cd, name, product_type_cd, date_offered)
values ('CHK','checking account','ACCOUNT','2000-01-01');
insert ignore into product (product_cd, name, product_type_cd, date_offered)
values ('SAV','savings account','ACCOUNT','2000-01-01');
insert ignore into product (product_cd, name, product_type_cd, date_offered)
values ('MM','money market account','ACCOUNT','2000-01-01');
insert ignore into product (product_cd, name, product_type_cd, date_offered)
values ('CD','certificate of deposit','ACCOUNT','2000-01-01');
insert ignore into product (product_cd, name, product_type_cd, date_offered)
values ('MRT','home mortgage','LOAN','2000-01-01');
insert ignore into product (product_cd, name, product_type_cd, date_offered)
values ('AUT','auto loan','LOAN','2000-01-01');
insert ignore into product (product_cd, name, product_type_cd, date_offered)
values ('BUS','business line of credit','LOAN','2000-01-01');
insert ignore into product (product_cd, name, product_type_cd, date_offered)
values ('SBL','small business loan','LOAN','2000-01-01');
```

然后下面是插入customer表格的数据，也没啥好说的:

```mysql
insert ignore into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (1, '111-11-1111', 'I', '47 Mockingbird Ln', 'Lynnfield', 'MA', '01940');
insert ignore into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (2, '222-22-2222', 'I', '372 Clearwater Blvd', 'Woburn', 'MA', '01801');
insert ignore into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (3, '333-33-3333', 'I', '18 Jessup Rd', 'Quincy', 'MA', '02169');
insert ignore into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (4, '444-44-4444', 'I', '12 Buchanan Ln', 'Waltham', 'MA', '02451');
insert ignore into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (5, '555-55-5555', 'I', '2341 Main St', 'Salem', 'NH', '03079');
insert ignore into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (6, '666-66-6666', 'I', '12 Blaylock Ln', 'Waltham', 'MA', '02451');
insert ignore into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (7, '777-77-7777', 'I', '29 Admiral Ln', 'Wilmington', 'MA', '01887');
insert ignore into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (8, '888-88-8888', 'I', '472 Freedom Rd', 'Salem', 'NH', '03079');
insert ignore into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (9, '999-99-9999', 'I', '29 Maple St', 'Newton', 'MA', '02458');
insert ignore into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (10, '04-1111111', 'B', '7 Industrial Way', 'Salem', 'NH', '03079');
insert ignore into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (11, '04-2222222', 'B', '287A Corporate Ave', 'Wilmington', 'MA', '01887');
insert ignore into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (12, '04-3333333', 'B', '789 Main St', 'Salem', 'NH', '03079');
insert ignore into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (13, '04-4444444', 'B', '4772 Presidential Way', 'Quincy', 'MA', '02169');
```

### insert where语句<a id="orgheadline19"></a>

下面往individual表格插入数据的操作就是前面谈论过的insert where语句。

```mysql
insert ignore into individual (cust_id, fname, lname, birth_date)
select cust_id, 'James', 'Hadley', '1972-04-22' from customer
where fed_id = '111-11-1111';
insert ignore into individual (cust_id, fname, lname, birth_date)
select cust_id, 'Susan', 'Tingley', '1968-08-15' from customer
where fed_id = '222-22-2222';
insert ignore into individual (cust_id, fname, lname, birth_date)
select cust_id, 'Frank', 'Tucker', '1958-02-06' from customer
where fed_id = '333-33-3333';
insert ignore into individual (cust_id, fname, lname, birth_date)
select cust_id, 'John', 'Hayward', '1966-12-22' from customer
where fed_id = '444-44-4444';
insert ignore into individual (cust_id, fname, lname, birth_date)
select cust_id, 'Charles', 'Frasier', '1971-08-25' from customer
where fed_id = '555-55-5555';
insert ignore into individual (cust_id, fname, lname, birth_date)
select cust_id, 'John', 'Spencer', '1962-09-14' from customer
where fed_id = '666-66-6666';
insert ignore into individual (cust_id, fname, lname, birth_date)
select cust_id, 'Margaret', 'Young', '1947-03-19' from customer
where fed_id = '777-77-7777';
insert ignore into individual (cust_id, fname, lname, birth_date)
select cust_id, 'Louis', 'Blake', '1977-07-01' from customer
where fed_id = '888-88-8888';
insert ignore into individual (cust_id, fname, lname, birth_date)
select cust_id, 'Richard', 'Farley', '1968-06-16' from customer
where fed_id = '999-99-9999';


insert ignore into business (cust_id, name, state_id, incorp_date)
select cust_id, 'Chilton Engineering', '12-345-678', '1995-05-01' from customer
where fed_id = '04-1111111';
insert ignore into business (cust_id, name, state_id, incorp_date)
select cust_id, 'Northeast Cooling Inc.', '23-456-789', '2001-01-01' from customer
where fed_id = '04-2222222';
insert ignore into business (cust_id, name, state_id, incorp_date)
select cust_id, 'Superior Auto Body', '34-567-890', '2002-06-30' from customer
where fed_id = '04-3333333';
insert ignore into business (cust_id, name, state_id, incorp_date)
select cust_id, 'AAA Insurance Inc.', '45-678-901', '1999-05-01' from customer
where fed_id = '04-4444444';

insert ignore into officer (officer_id, cust_id, fname, lname,
  title, start_date)
select 1, cust_id, 'John', 'Chilton', 'President', '1995-05-01'
from customer
where fed_id = '04-1111111';
insert ignore into officer (officer_id, cust_id, fname, lname,
  title, start_date)
select 2, cust_id, 'Paul', 'Hardy', 'President', '2001-01-01'
from customer
where fed_id = '04-2222222';
insert ignore into officer (officer_id, cust_id, fname, lname,
  title, start_date)
select 3, cust_id, 'Carl', 'Lutz', 'President', '2002-06-30'
from customer
where fed_id = '04-3333333';
insert ignore into officer (officer_id, cust_id, fname, lname,
  title, start_date)
select 4, cust_id, 'Stanley', 'Cheswick', 'President', '1999-05-01'
from customer
where fed_id = '04-4444444';
```

### 交叉连接<a id="orgheadline20"></a>

接下来的这个语句显得更加复杂了:

```mysql
insert ignore into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 1, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Woburn' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2000-01-15' open_date, '2005-01-04' last_date,
    1057.75 avail, 1057.75 pend union all
  select 'SAV' prod_cd, '2000-01-15' open_date, '2004-12-19' last_date,
    500.00 avail, 500.00 pend union all
  select 'CD' prod_cd, '2004-06-30' open_date, '2004-06-30' last_date,
    3000.00 avail, 3000.00 pend) a
where c.fed_id = '111-11-1111';
```

该SQL语句主体是insert select语句，然后显得复杂的部分就是那个select语句是有customer（别名c）和一个子查询语句生成的表格（别名e）和另外一个子查询语句生成的表格（别名a）的 `cross join` 而成的一个复杂的表格。

这里我们需要理解cross join这个概念，不知道读者之前接触过inner join，内连接的概念没有，如果接触过那么一定了解了SQL表格在join的时候不加任何过滤条件其生成的表格就是所谓的这两个SQL表格的笛卡尔积。所谓的笛卡尔积就是，假设一个表格有三行，a行b行c行，然后假设另外一个表格有两行，1行和2行，那么这两个表格的笛卡尔积就是生成一个大表格，具体是(a1行a2行b1行b2行c1行c2行)，一共3\*2=6行。

而所谓的cross join交叉连接实际上就是多个表格之间进行笛卡尔积运算之后组合成为一个更大的表格。

### 内连接<a id="orgheadline21"></a>

我们又看到上面的例子中第一个子查询语句里面还有 `inner join` 关键词，其是所谓的内连接。内连接可以看作是在交叉连接生成的表格的基础上进一步加上了某些过滤条件从而将某些行给删除掉了。

我们首先来看一下:

    select b.branch_id, e.emp_id, e.assigned_branch_id from branch b cross join employee e ;

branch表格有4条记录，branch有18条记录，所以cross join之后将组合出72条记录。

然后我们再来看这个查询:

    select b.branch_id, e.emp_id from branch b inner join employee e on e.assigned_branch_id = b.branch_id;

通常两个SQL表格cross join之后出来的大SQL表格里面有些数据组合是实际可能并不存在的，而上面inner join通过on关键词过滤将使得生成的大SQL表格更具有现实意义。比如这里每一个雇员只可能在某一个分公司，而cross join让每个雇员都有可能在四个分公司了，这里的inner join加上on主要就是控制雇员具体分配的那个分公司正是连接的那个分公司号。这样实现更有现实意义的连接。我们也可以这样理解，雇员的分公司属性id为1，那么在连接分公司表格的时候，只有确定了这个，才能保证分公司表格的其他属性也是属于该雇员的。

现在我们进行到这里了:

    mysql> select b.branch_id, e.emp_id,b.city from branch b inner join employee e on e.assigned_branch_id = b.branch_id;
    +-----------+--------+---------+
    | branch_id | emp_id | city    |
    +-----------+--------+---------+
    |         1 |      1 | Waltham |
    |         1 |      2 | Waltham |
    |         1 |      3 | Waltham |
    |         1 |      4 | Waltham |
    |         1 |      5 | Waltham |
    |         1 |      6 | Waltham |
    |         1 |      7 | Waltham |
    |         1 |      8 | Waltham |
    |         1 |      9 | Waltham |
    |         2 |     10 | Woburn  |
    |         2 |     11 | Woburn  |
    |         2 |     12 | Woburn  |
    |         3 |     13 | Quincy  |
    |         3 |     14 | Quincy  |
    |         3 |     15 | Quincy  |
    |         4 |     16 | Salem   |
    |         4 |     17 | Salem   |
    |         4 |     18 | Salem   |
    +-----------+--------+---------+
    18 rows in set (0.00 sec)

然后通过  where b.city = 'Woburn' 这实际上就限定为具体某一个分公司了。

    mysql> select b.branch_id, e.emp_id,b.city from branch b inner join employee e on e.assigned_branch_id = b.branch_id where b.city='Woburn';
    +-----------+--------+--------+
    | branch_id | emp_id | city   |
    +-----------+--------+--------+
    |         2 |     10 | Woburn |
    |         2 |     11 | Woburn |
    |         2 |     12 | Woburn |
    +-----------+--------+--------+
    3 rows in set (0.00 sec)

然后后面跟了 `limit 1` 这样将只返回一条记录了。然后我们注意到最终cross join生成的大表格还加上了过滤条件 

    where c.fed_id = '111-11-1111';

由于每一个顾客的fed\_id都是唯一的，所以实际上custom表格真正交叉连接的也只有一条记录，这样这个三个表格cross join这个复杂的情况就等同于前面两个表格一条记录属性都加上，再cross 第三个表格，第三个表格有三条记录，这样最终的大表格有三条记录。

### union all<a id="orgheadline22"></a>

`union all` 将多个数据集进行合并。此外还有一种 `union` 的用法，其中 `union`  会删除重复项，而union all只是单纯的合并。如下所示:

    mysql> select 'CHK' prod_cd, '2000-01-15' open_date, '2005-01-04' last_date,
        ->     1057.75 avail, 1057.75 pend union all
        ->   select 'SAV' prod_cd, '2000-01-15' open_date, '2004-12-19' last_date,
        ->     500.00 avail, 500.00 pend union all
        ->   select 'CD' prod_cd, '2004-06-30' open_date, '2004-06-30' last_date,
        ->     3000.00 avail, 3000.00 pend;
    +---------+------------+------------+---------+---------+
    | prod_cd | open_date  | last_date  | avail   | pend    |
    +---------+------------+------------+---------+---------+
    | CHK     | 2000-01-15 | 2005-01-04 | 1057.75 | 1057.75 |
    | SAV     | 2000-01-15 | 2004-12-19 |  500.00 |  500.00 |
    | CD      | 2004-06-30 | 2004-06-30 | 3000.00 | 3000.00 |
    +---------+------------+------------+---------+---------+
    3 rows in set (0.01 sec)

这样下面这些我们应该也大致能够看明白了:

```mysql
insert ignore into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 2, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Woburn' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2001-03-12' open_date, '2004-12-27' last_date,
    2258.02 avail, 2258.02 pend union all
  select 'SAV' prod_cd, '2001-03-12' open_date, '2004-12-11' last_date,
    200.00 avail, 200.00 pend) a
where c.fed_id = '222-22-2222';
insert ignore into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 3, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Quincy' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2002-11-23' open_date, '2004-11-30' last_date,
    1057.75 avail, 1057.75 pend union all
  select 'MM' prod_cd, '2002-12-15' open_date, '2004-12-05' last_date,
    2212.50 avail, 2212.50 pend) a
where c.fed_id = '333-33-3333';
insert ignore into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 4, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Waltham' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2003-09-12' open_date, '2005-01-03' last_date,
    534.12 avail, 534.12 pend union all
  select 'SAV' prod_cd, '2000-01-15' open_date, '2004-10-24' last_date,
    767.77 avail, 767.77 pend union all
  select 'MM' prod_cd, '2004-09-30' open_date, '2004-11-11' last_date,
    5487.09 avail, 5487.09 pend) a
where c.fed_id = '444-44-4444';
insert ignore into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 5, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Salem' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2004-01-27' open_date, '2005-01-05' last_date,
    2237.97 avail, 2897.97 pend) a
where c.fed_id = '555-55-5555';
insert ignore into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 6, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Waltham' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2002-08-24' open_date, '2004-11-29' last_date,
    122.37 avail, 122.37 pend union all
  select 'CD' prod_cd, '2004-12-28' open_date, '2004-12-28' last_date,
    10000.00 avail, 10000.00 pend) a
where c.fed_id = '666-66-6666';
insert ignore into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 7, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Woburn' limit 1) e
  cross join
 (select 'CD' prod_cd, '2004-01-12' open_date, '2004-01-12' last_date,
    5000.00 avail, 5000.00 pend) a
where c.fed_id = '777-77-7777';
insert ignore into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 8, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Salem' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2001-05-23' open_date, '2005-01-03' last_date,
    3487.19 avail, 3487.19 pend union all
  select 'SAV' prod_cd, '2001-05-23' open_date, '2004-10-12' last_date,
    387.99 avail, 387.99 pend) a
where c.fed_id = '888-88-8888';
insert ignore into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 9, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Waltham' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2003-07-30' open_date, '2004-12-15' last_date,
    125.67 avail, 125.67 pend union all
  select 'MM' prod_cd, '2004-10-28' open_date, '2004-10-28' last_date,
    9345.55 avail, 9845.55 pend union all
  select 'CD' prod_cd, '2004-06-30' open_date, '2004-06-30' last_date,
    1500.00 avail, 1500.00 pend) a
where c.fed_id = '999-99-9999';


insert ignore into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 10, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Salem' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2002-09-30' open_date, '2004-12-15' last_date,
    23575.12 avail, 23575.12 pend union all
  select 'BUS' prod_cd, '2002-10-01' open_date, '2004-08-28' last_date,
    0 avail, 0 pend) a
where c.fed_id = '04-1111111';
insert ignore into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 11, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Woburn' limit 1) e
  cross join
 (select 'BUS' prod_cd, '2004-03-22' open_date, '2004-11-14' last_date,
    9345.55 avail, 9345.55 pend) a
where c.fed_id = '04-2222222';
insert ignore into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 12, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Salem' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2003-07-30' open_date, '2004-12-15' last_date,
    38552.05 avail, 38552.05 pend) a
where c.fed_id = '04-3333333';
insert ignore into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 13, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Quincy' limit 1) e
  cross join
 (select 'SBL' prod_cd, '2004-02-22' open_date, '2004-12-17' last_date,
    50000.00 avail, 50000.00 pend) a
where c.fed_id = '04-4444444';
```

### 不能重复刷的部分<a id="orgheadline23"></a>

这种insert select语句有多行记录要刷进去，目前还找不到防止重复刷的办法，只好单独放在这里了。

```mysql
insert into transaction (txn_id, txn_date, account_id, txn_type_cd,
  amount, funds_avail_date)
select null, a.open_date, a.account_id, 'CDT', 100, a.open_date
from account a
where a.product_cd IN ('CHK','SAV','CD','MM');
```

---

# 别名<a id="orgheadline26"></a>

前面说了select字句是不仅可以运算列，还可以重新构建一个列，这些列mysql会自动为其创建默认名字，你也可以明确指定该名字，用如下 **as** 关键词，如下所示:

    select emp_id, 'ACTIVE' as status, emp_id * 3.1415926 as empid_x_pi, upper(lname) as last_name_upper from employee;

**as** 关键词可以省略，表达仍然有效，但还是推荐加上 **as** 关键词，这样SQL语句可读性更高。

# 去除重复的行<a id="orgheadline27"></a>

如下所示加入 **distinct** 关键词来让select字句过滤掉重复的行。

    select distinct cust_id from account;

# 附录<a id="orgheadline30"></a>

## 演示例子的补充信息<a id="orgheadline28"></a>

该演示数据，按照《SQL学习指南》一书所说，是为了某一银行建立的数据模型，不过我们看到，其中涉及的顾客，部门，产品等概念在很多领域都是适用的。

下面列出关于这些表格的含义说明:

-   **account:** 为特定顾客开放的特定产品
-   **branch:** 开展银行交易业务的场所，就可理解为某分公司分银行。
-   **business:** 公司顾客
-   **customer:** 与银行有业务往来的个人或公司
-   **department:** 就可理解为银行内某部门
-   **employee:** 银行工作人员
-   **individual:** 个人顾客，我们看到和business对应。
-   **officer:** 允许为公司顾客发起交易的人
-   **product:** 向顾客提供的银行服务
-   **product\_type:** 服务类型
-   **transaction:** 改变账户余额的操作

## 参考资料<a id="orgheadline29"></a>

1.  本网页主要参考了《SQL学习指南》一书，第二版，Alan Beaulieu著，张伟超，林青松译。

<div id="footnotes">
<h2 class="footnotes">Footnotes: </h2>
<div id="text-footnotes">

<div class="footdef"><sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> <div class="footpara">参考了[这个网页](http://www.w3schools.com/sql/sql_insert_into_select.asp)。</div></div>


</div>
</div>