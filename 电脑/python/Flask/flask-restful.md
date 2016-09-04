<nav id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. org模式入门</a></li>
</ul>
</div>
</nav>


# org模式入门<a id="orgheadline1"></a>

然后flask0.7版本之后新加入了 `MethodView` 类，如下所示:

    class UserAPI(MethodView):
    
        def get(self, user_id):
            if user_id is None:
                # return a list of users
                pass
            else:
                # expose a single user
                pass
    
        def post(self):
            # create a new user
            pass
    
        def delete(self, user_id):
            # delete a single user
            pass
    
        def put(self, user_id):
            # update a single user
            pass

这已经很方便就能编写出restful api接口了，但实际编写restfulapi推荐使用 flask-restful 这个插件。具体使用参看官方文档的这个例子:

    from flask import Flask
    from flask_restful import Resource, Api
    
    app = Flask(__name__)
    api = Api(app)
    
    class HelloWorld(Resource):
        def get(self):
            return {'hello': 'world'}
    
    api.add_resource(HelloWorld, '/')
    
    if __name__ == '__main__':
        app.run(debug=True)

注意一下几点:

1.  返回的是字典类型，该插件会自动jsonify处理的。
2.  `api.add_resource(ClassName,'/resname/<path:path>',endpoint='resname')` ，endpoint定义了这个restfulapi的视图函数的endpoint值，然后你可以用 `url_for` 来快速生成对应的URL。
3.  该类中的方法其实等同于之前谈及的flask的视图函数，所以request session等这些变量也是可以使用的（存疑？）。
4.  你可以这样:

    class FoldersAPI(Resource):
        def __init__(self):
            parser = reqparse.RequestParser()
            parser.add_argument('name')
            parser.add_argument('description')
            parser.add_argument('apikey')
            self.args = parser.parse_args()
            if self.args.get('apikey'):
                g.apikey = self.args.get('apikey')

来给你的restfulapi endpoint 刷入一些参数，如果没设置参数，则该 `self.args['name']` 就是默认值 None。这些参数在后面的视图函数 get post之类中都是可以使用的。这个 `reqparse` 来自:

    from flask_restful import reqparse

你可以看到其使用和 argparse 模块很接近。如果你熟悉python的argparse模块，那么可以毫不费力的来直接使用了。

如果你要刷入一个列表，则需要如下设置:

    parser.add_argument('name', action='append')

你还可以利用其从flask的request对象上刷值:

    parser.add_argument('name', type=int, location='form')

这个我还不太清楚，似乎我们应该这样把之前提及的request变量刷的值引入进来。这样这套api也是可以为视图层所使用了。

具体例子请参看我写的 [flask-examples](https://github.com/a358003542/flask-examples) 那里，具体是 restfulapi.py 。

更多内容请参看官方文档。这个插件的官方文档的中文翻译版本可以在这里 [阅读](http://flask-restful-cn.readthedocs.org/zh/latest/quickstart.html) 。