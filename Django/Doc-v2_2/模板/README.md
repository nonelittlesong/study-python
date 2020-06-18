## 变量
语法： `{{ variable }}`  

>如果 variable 不存在，默认赋予 `''` 空字符串。  
>
>注意：如果 `bar` 在模板表达式中（如 `{{ foo.bar }}`），会被翻译成字符串，而不是变量 `bar` 的值。  
>
>以下划线开头的变量属性被视为私有的，不能访问。  

## 标签和过滤器
- [内建标签和过滤器](https://docs.djangoproject.com/zh-hans/2.2/ref/templates/builtins)  
- [自定义标签和过滤器](https://docs.djangoproject.com/zh-hans/2.2/howto/custom-template-tags/)

## 注释
语法： `{# #}`  
多行注释使用 `comment` 标签。  

## 模板继承

**注意：**  
- `{% extends %}` 必须位于模板最开始，否则不生效。  
- 在 `{% block %} 外通过 `as` 创建的变量，不能在 block 里用。  

## 自动 HTML 转义
避免 XSS 攻击！！  

### 如何关闭
- 对于单个变量，使用 `safe` 过滤器。  
- 对于文本块，使用 `autoescape` 标签。  

## 访问方法调用
由于Django有意限制了模板中语言逻辑的处理, 所以不能在模板内调用方法时传递参数. 数据应当在视图中计算, 然后再传递给模板.  

