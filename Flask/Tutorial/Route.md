
# Routing

使用 [route()](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.route) 装饰器绑定方法和 URL。

```py
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```

## 1. 变量

```py
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
```

Converter 类型：

| Converter 类型 | 描述 |
| --- | --- |
| string | (default) 接受不含 `/` 的文字 |
| int | 接受正整数 |
| float | 接受正浮点值 |
| path | 和 `string` 相似，但接受 `/` |
| uuid | UUID 字符串 |

## 2. Unique URLs / Redirection Behavior

```py
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```

- 使用 `/projects` 访问 `/projects/` 会重定向。
- 使用 `/about/` 访问 `/about`，返回 404。
