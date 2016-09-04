<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. 简介</a></li>
<li><a href="#orgheadline5">2. 第一个例子</a>
<ul>
<li><a href="#orgheadline2">2.1. 事件</a></li>
<li><a href="#orgheadline3">2.2. namespace</a></li>
<li><a href="#orgheadline4">2.3. emit函数</a></li>
</ul>
</li>
</ul>
</div>
</nav>


# 简介<a id="orgheadline1"></a>

推荐使用 `flask-socketio` 这个模块:

    pip install flask-socketio

其入门tutorial在 [这里](http://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent) ，其github地址在 [这里](https://github.com/miguelgrinberg/Flask-SocketIO) ，其官方文档地址在 [这里](https://github.com/miguelgrinberg/Flask-SocketIO) 。

# 第一个例子<a id="orgheadline5"></a>

test.py

```python
from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app,debug=True)
```

然后在templates文件夹下建立的 `index.html` :

```html
&lt;!DOCTYPE HTML&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Flask-SocketIO Test&lt;/title&gt;
    &lt;script type="text/javascript" src="//code.jquery.com/jquery-1.4.2.min.js"&gt;&lt;/script&gt;
    &lt;script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.5/socket.io.min.js"&gt;&lt;/script&gt;

&lt;script&gt;
$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    socket.on('my response', function(msg) {
        $('#log').append('&lt;p&gt;Received: ' + msg.data + '&lt;/p&gt;');
    });
    $('form#emit').submit(function(event) {
        socket.emit('my event', {data: $('#emit_data').val()});
        return false;
    });
    $('form#broadcast').submit(function(event) {
        socket.emit('my broadcast event', {data: $('#broadcast_data').val()});
        return false;
    });
});
&lt;/script&gt;

&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;Flask-SocketIO Test&lt;/h1&gt;
    &lt;h2&gt;Send:&lt;/h2&gt;
    &lt;table&gt;
        &lt;tr&gt;
            &lt;td&gt;
                &lt;form id="emit" method='POST' action='#'&gt;
                    &lt;textarea name="emit_data" id="emit_data"&gt;&lt;/textarea&gt;
                    &lt;div&gt;&lt;input type="submit" value="Emit"&gt;&lt;/div&gt;
                &lt;/form&gt;
            &lt;/td&gt;
            &lt;td&gt;
                &lt;form id="broadcast" method='POST' action='#'&gt;
                    &lt;textarea name="broadcast_data" id="broadcast_data"&gt;&lt;/textarea&gt;
                    &lt;div&gt;&lt;input type="submit" value="Broadcast"&gt;&lt;/div&gt;
                &lt;/form&gt;
            &lt;/td&gt;
        &lt;/tr&gt;
    &lt;/table&gt;
    &lt;h2&gt;Receive:&lt;/h2&gt;
    &lt;div id="log"&gt;&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
```

推荐在额外安装个 `eventlet` :

    pip3 install eventlet

来支持更好的websocket并发，但在这里不是重点。首先我们看到代码，很是简洁明了，我想需要就以下细节说明以下即可:

## 事件<a id="orgheadline2"></a>

遇到何种事件做何种事情，默认的内置事件有: `connect` , `disconnect` , `message` , `json` 。后面再详细讨论之。

## namespace<a id="orgheadline3"></a>

含义类似于flask蓝图的 `url_prefix` 。

## emit函数<a id="orgheadline4"></a>

具体发送某个事件和该事件下的信息。然后我们看到 `broadcast=True` ，这样本次信号发送相当于一次广播，所有打开的网页都可以接受到这个广播信号，而不加的话，只有某一个web client能够看到。

再来看到网页那边，需要加载 `jquery` 和 `socket.io` 这两个js库。

    <script type="text/javascript" src="//code.jquery.com/jquery-1.4.2.min.js"></script>
    <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.5/socket.io.min.js"></script>

然后是下面这段代码，因为我js也是个新手，读者可以和我一起慢慢看一下。

```js
&lt;script&gt;
$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    socket.on('my response', function(msg) {
        $('#log').append('&lt;p&gt;Received: ' + msg.data + '&lt;/p&gt;');
    });
    $('form#emit').submit(function(event) {
        socket.emit('my event', {data: $('#emit_data').val()});
        return false;
    });
    $('form#broadcast').submit(function(event) {
        socket.emit('my broadcast event', {data: $('#broadcast_data').val()});
        return false;
    });
});
&lt;/script&gt;
```

首先是在文档加载完之后执行这个函数，然后建立了一个socket变量，然后当接受到 `my response` 事件的时候，则执行该函数，具体就是在log那边表现在添加某个文字内容。

然后下面两个是表单的emit那个标签，也就是html代码的emit那个按钮，如果点击submit了则执行这个函数，大体是发送 `my event` 事件，后面跟着某个data。

整个过程大体就是如此，读者可以简单的事件看一下效果。