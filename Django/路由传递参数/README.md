
在 `mysite/urls.py` 中写入：  
```py
urlpatterns = [
    path('', include('urlparams.urls')),
    path('admin/', admin.site.urls)
]
```

在 `urlparams/urls.py` 中写入：  
```py
from django.urls import path
from urlparams import views

urlpatterns = [
    path('args/', views.params_first),
    re_path(r'^params/(\w+)/(\d+)/$', views.params),
    path('params2/<username>/<password>/', views.params2)，
    path('params3/', views.params3, {'user': '李四', 'pwd': '123'}),
    re_path(r'^params4/(?P<username>\w+)/(?P<id>\d+)/$', views.params4),
]
```
在 `urlparams/views` 写入：  
```py
from django.http import HttpResponse


def params_first(request):
    #针对路由的第一种情况，直接从GET请求中获取参数。
    user_name=request.GET.get('user','')
    pass_word=request.GET.get('pwd','')
    result='账号:{},密码:{}'.format(user_name,pass_word)
    return HttpResponse(result)
    
def params(request, name, pwd):
    result = 'name={}, pwd={}'.format(name, pwd)
    return HttpResponse(result)
    
def params2(request, username, password):
    result = 'username={}, password={}'.format(username, password)
    return HttpResponse(result)
    
def params3(request, user, pwd):
    result = 'user={}, pwd={}'.format(user, pwd)
    return HttpResponse(result)
    
def params4(request, username, id):
    result = 'username={},id={}'.format(username, id)
    return HttpResponse(result)
```
在浏览器中输入  
```
127.0.0.1:8000/args/?user=张飒&pwd=123
127.0.0.1:8000/params/正则/234
127.0.0.1:8000/params2/不用正则/12345
127.0.0.1:8000/params3/
127.0.0.1:8000/params4/王五/123456
```

