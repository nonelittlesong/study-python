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
