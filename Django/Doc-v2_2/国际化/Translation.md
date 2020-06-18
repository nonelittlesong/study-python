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
