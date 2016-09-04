<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 简介</a></li>
<li><a href="#orgheadline5">2. 第一个例子</a>
<ul>
<li><a href="#orgheadline2">2.1. 模型层</a></li>
<li><a href="#orgheadline3">2.2. 网页模板</a></li>
<li><a href="#orgheadline4">2.3. 视图层</a></li>
</ul>
</li>
</ul>
</div>
</nav>


# 简介<a id="orgheadline1"></a>

官方文档在 [这里](https://flask-wtf.readthedocs.org/en/latest/) ，简单的安装就是:

    bash>>> sudo pip3 install flask-wtf

其是对python的另外一个模块 `wtforms` 和flask的对接，方便快速创建表单，管理表单等等其他相关事情。我之前并没有接触过 `wtforms` 这个模块，不管怎么说，后面慢慢接触吧。

# 第一个例子<a id="orgheadline5"></a>

比如我们要创建登录输入email和密码的表单，在flask框架的forms.py那里写上:

```python
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class EmailPasswordForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
```

然后在相应的模块文件那里有如下代码:

```html
&lt;form action="{{url_for('signin')}}" method="post" class="form-signin"&gt;
      &lt;h2 class="form-signin-heading"&gt;Please sign in&lt;/h2&gt;
    &lt;div class="form-group"&gt;
            {{ form.email(class_="form-control",placeholder="Email") }}
    &lt;/div&gt;
    &lt;div class="form-group"&gt;
        {{ form.password(class_="form-control",placeholder="Password") }}
    &lt;/div&gt;
    &lt;button type="submit" class="btn btn-default btn-halfblock"&gt;Sign in&lt;/button&gt;
    &lt;button type="submit" formaction="/register" class="btn btn-default btn-halfblock"&gt;Register&lt;/button&gt;

    {{ form.csrf_token }}
&lt;/form&gt;
```

然后在flask框架的视图层那边有:

```python
@app.route('/register', methods=['GET','POST'])
def register():
    form = EmailPasswordForm()
    if form.validate_on_submit():
        ### do some register sucessed thing
        user = User(
            email = form.email.data,
            password = form.password.data
        )
        email = user.email
        target = db.session.query(User).filter(User.email == email).first()
        if target:
            flash('alredy register under this email')
        else:
            ## update database
            ##send confirm email
    return redirect(url_for('index'))
```

当然更加成熟的处理用户注册登录之类事宜的推荐使用 `flask-user` 模块，这里主要是利用这个例子来理解 `flask-wtf` 的一些基本的东西。

## 模型层<a id="orgheadline2"></a>

模型层那边就是定义一些你想要该form表单存储那些value。定义的时候像 `StringField` 这个是很影响后面在网页模板那边具体的显示结果的，比如 `PasswordField` 在输出 input 标签的时候 type 类型应该是 password 。当然实际操作我们根据情景选择使用的类即可，不用想那么多了。

`validators` 这个选项很重要，比如 `validators=[DataRequired(), Email()])` 则要求该输入框你必须输入值而且是有效的email格式，否则该表单不能提交。你还可以定义自己的验证器等，还有自己的提示信息等，这些后面再说。

## 网页模板<a id="orgheadline3"></a>

这里参看了 [这个网页](http://stackoverflow.com/questions/22084886/add-a-css-class-to-a-field-in-wtform) ，当我们在网页模板上写上:

    {{ form.email }}

其会输出:

    <input id="email" name="email" type="text" value="">

然后如果我们如下写上:

    {{ form.email(class_="form-control",placeholder="Email") }}

其输出（我这里还不大确切，不过大体是这样）:

    <input id="email" name="email" type="text" value="" class="form-control" placeholder="Email">

其他相关html知识这里就不多说了，然后再看到这一行:

    {{ form.csrf_token }}

使用是处理表单CSRF的唯一性验证的，然后app的config需要加上:

    WTF_CSRF_ENABLED = False

然后其他的flask-wtf会自动帮我们处理好，当然这一块还有其他一些内容，先暂时略过。

## 视图层<a id="orgheadline4"></a>

在视图层的视图函数那边，首先我们需要定义你这里想使用的表单对象:

    form = EmailPasswordForm()

然后后面的基本结构是:

    if form.validate_on_submit():
        ### do some register sucessed thing
    return redirect(url_for('index'))

这里的 `form.validate_on_submit()` 就是在接受POST请求的时候验证表单有效性，如果有效则具体做何种动作，比如数据库操作啊，发送确认email动作啊等等。最后那个就是网页返回操作了，这个根据实际情况需要会有所不同。

大体整个流程就是这样的，然后接下来就是其他一些具体细节问题了。