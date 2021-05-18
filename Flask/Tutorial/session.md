# Session: 安全的 Cookie

Flask 用 session 对象加密 Cookie。数据存储在一个叫 session 的 cookie 中。  
不要在 session 中存敏感信息。

```py
# 获取 Cookie
session.get(attr)
# 设置 Cookie
session[attr] = value
# 删除 Cookie
session.pop(attr)

# 生命周期
# 默认关闭浏览器后删除
# session.permanent 设为 True，将有效期延长至 Flask.permanent_session_lifetime
```
