## [国际化 JavaScript 代码](https://docs.djangoproject.com/en/3.0/topics/i18n/translation/#internationalization-in-javascript-code)  
问题：  
- JS 无法访问 `gettext` 实现。  
- JS 无法访问 `.po .mo` 文件；需要通过服务器传递。  
- `translation catalog` 需要尽可能小。  

Django 通过 `JavaScriptCatalog` 视图解决问题。  



## 国际化 Python 代码

## 国际化模板
在所有需要翻译的模板开头加上 `{% load i18n %}` 标签，即使它继承的模板已经有了。  

### trans 模板标签
可以翻译字符串常量和变量：  
```django
<title>{% trans "This is the title." %}</title>
<title>{% trans myvar %}</title>
<!-- noop 选项禁止翻译 -->
<title>{% trans "myvar" noop %}</title>
<!-- 上下文标记 -->
{% trans "May" context "month name" %}
```

只翻译、不显示：  
```django
{% trans "This is a title" as the_title %}

<title>{{ the_title }}</title>
<meta name="description" content="{{ the_title }}">
```

### blocktrans 模板标签
翻译字符串和变量的组合形式：  
```django
{% blocktrans %}This string will have {{ value }} inside.{% endblocktrans %}
```
为了访问对象属性或使用模板过滤器，需要在标签中绑定：  
```django
{% blocktrans with amount=article.price %}
That will cost $ {{ amount }}.
{% endblocktrans %}

{% blocktrans with myvar=value|filter %}
This will have {{ myvar }} inside.
{% endblocktrans %}

<!-- 可以在一个标签中使用多个表达式 -->
{% blocktrans with book_t=book|title author_t=author|title %}
This is {{ book_t }} by {{ author_t }}
{% endblocktrans %}

<!-- 其他格式 -->
{% blocktrans with book|title as book_t and author|title as author_t %}
```

不能在 `blocktrans` 标签中使用其他的块标签（例如： `{% for %}` 和 `{% if %}`）。  

复数形式：  
```django
{% blocktrans count counter=list|length %}
There is only one {{ name }} object.
{% plural %}
There are {{ counter }} {{ name }} objects.
{% endblocktrans %}

{% blocktrans with amount=article.price count years=i.length %}
That will cost $ {{ amount }} per year.
{% plural %}
That will cost $ {{ amount }} per {{ years }} years.
{% endblocktrans %}
```

Reverse URL lookups cannot be carried out within the blocktrans and should be retrieved (and stored) beforehand:  
```django
{% url 'path.to.view' arg arg2 as the_url %}
{% blocktrans %}
This is a URL: {{ the_url }}
{% endblocktrans %}
```

`asvar` 只翻译、 不显示：  
```django
{% blocktrans asvar the_title %}The title is {{ title }}.{% endblocktrans %}
<title>{{ the_title }}</title>
<meta name="description" content="{{ the_title }}">
```

## 创建语言文件


## 笔记
### [django 如何确定语言偏好](https://docs.djangoproject.com/en/2.2/topics/i18n/translation/#how-django-discovers-language-preference)
如果没有用 `LocaleMiddleware` 中间件，根据系统的 `LANGUAGE_CODE` 确定用户语言。  
如果使用了 `LocaleMiddleware` 中间件，则遵循如下的算法：  
1. 首先，如果用了 [i18n_patterns](https://docs.djangoproject.com/en/2.2/topics/i18n/translation/#module-django.conf.urls.i18n)，查看 URL 中的 语言前缀。  
2. 其次，查看 `LANGUAGE_SESSION_KEY`。  
3. 其次，查看 cookie。  
4. 其次，查看 HTTP 的 `Accept-Language` 头，由浏览器设定。  
5. 最后，查看 `LANGUAGE_CODE`。  
