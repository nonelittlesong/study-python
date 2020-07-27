# Django 应用 Dwebsocket
参考:  
- [dwebsocket 学习 - 掘金](https://juejin.im/post/5d9f6d66e51d4578034d2db3)  
- [dwebsocket - PyPI](https://pypi.org/project/dwebsocket/)  
- [dwebsocket - github](https://github.com/duanhongyi/dwebsocket)  

## 安装 dwebsocket
```sh
# [] 中是可选项
pip3 install dwebsocket[==x.x.xx]
```

## 使用 dwebsocket
两种使用方式:  
- **单个**视图添加 websocket 功能：  
  - 利用 `accept_websocket` 修饰器，同时接收 HTTP 请求。  
  - 利用 `require_websocket` 修饰器，拒绝 HTTP 请求。  
- **所有**视图添加 websocket 功能：  
  - 在设置 `MIDDLEWARE_CLASSES` 中添加 `dwebsocket.middleware.WebSocketMiddleware` 中间件。同时，在视图中设置 `accept_websocket`，才能接收 websockets。  
  - 要使所有视图接收 websocket，设置 `WEBSOCKET_ACCEPT_ALL` 为 `true`。  

## 属性和方法

### 属性

### 方法
