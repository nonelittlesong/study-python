# [访问 Request 数据](https://flask.palletsprojects.com/en/2.0.x/quickstart/#accessing-request-data)

Flask 通过全局的 `request` 对象访问客户端发送到服务端的数据。使用 `context locals`(`thread local`) 确保线程安全。

## 1. 单元测试

```py
from flask import request

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'

# 传递整个 WSGI 环境给 request_context() 方法
with app.request_context(environ):
    assert request.method == 'POST'
```

## 2. [Request](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request) 对象

为了访问 POST 和 PUT 传来的数据，可以访问 [form] (https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request.form) 属性。

```py
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
```

如果访问 form 属性中不存在的 key，会报 [KeyError](https://docs.python.org/3/library/exceptions.html#KeyError) 异常。如果不捕获它，会返回 HTTP 400 错误页面。

访问 URL 中的参数（?key=value)，可以使用 [args](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request.args) 属性：

```py
searchword = request.args.get('key', '')
```
