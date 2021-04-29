
## 标准过滤器

### tojson

将对象转为 json。

```html
<button onclick='doSomethingWith({{ user.username|tojson }})'>
    Click me
</button>

<script type=text/javascript>
    doSomethingWith({{ user.username|tojson }});
</script>
```
