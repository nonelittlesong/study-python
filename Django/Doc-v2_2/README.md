# 新手指南

##  一、创建一个项目
```sh
$ django-admin startproject mysite
```

生成的文件：  
```
mysite/              # 名称无任何影响，可以重命名
    manage.py        # 命令行工具
    mysite/          # 视为一个纯 Python 包。它的名字就是当你引用它内部任何东西时需要用到的 Python 包名。 (比如 mysite.urls)
        __init__.py  # 空文件告知 Python 将该目录视为 Python 包
        settings.py  # 项目的配置文件
        urls.py      # URL 声明，就像网站的目录
        wsgi.py      # 作为你的项目的运行在 WSGI 兼容的Web服务器上的入口
```

>**注意：**  
>不要在生产模式中使用 Django 内置的 Server！！  

## 二、创建 Polls app
```sh
$ python3 manage.py startapp polls
```

生成 polls 目录，结构如下：  
```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

### 视图
编写 `poll/views.py`  
```py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
编写 `poll/urls.py`  
```py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
编辑 `mysite/urls.py`  
```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

>**注意：**  
>在包含其他 URL 时，始终使用 `include()`。只有 `admin.site.urls` 例外。  

### path()
参数：  
- route - URL 字符串。不会查询参数。  
- view - 当找到匹配的 URL 时，调用对应的视图函数，`HttpRequest` 作为第一个参数，任何从路由中捕获的值作为关键字参数。  
- kwargs  
- name - 为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。这个有用的特性允许你只改一个文件就能全局地修改某个 URL 模式。
