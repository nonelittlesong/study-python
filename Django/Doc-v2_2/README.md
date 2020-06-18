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


## 四、编写更多的视图
向 `polls/views.py` 里添加更多的视图  
```py
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```
把新视图添加进 `polls.urls` 模块里  
```py
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

## 五、[使用模板](https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial03/#write-views-that-actually-do-something)
1. 在 `polls` 目录下创建 `templates` 目录。  
2. 在 `templates` 目录下再创建 `polls` 目录。  
3. 在 `polls/templates/polls` 新建一个模板 `index.html`。  

编辑 `polls/templates/polls/index.html`  
```py
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```
编辑 `polls/views.py`  
```py
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 载入模板
    template = loader.get_template('polls/index.html')
    # 将模板内的变量映射为 Python 对象
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

### render()
「载入模板，填充上下文，再返回由它生成的 HttpResponse 对象」是一个非常常用的操作流程。于是 Django 提供了一个快捷函数，我们用它来重写 `index()` 视图：  
```py
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```
