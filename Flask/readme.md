# Flask

轻量的 [WSGI](https://wsgi.readthedocs.io/en/latest/) 网页应用框架，基于 [Werkzeug](https://palletsprojects.com/p/werkzeug/)（综合的 WSGI 库） 和 [Jinja](https://palletsprojects.com/p/jinja/)（Python 模板引擎）。

参考：

- [thread-local](http://www.threadlocal.cn/) — 线程局部变量

## 1. 依赖

以下软件在安装 Flask 后会自动安装：

- [Werkzeug](https://palletsprojects.com/p/werkzeug/)
- [Jinja](https://palletsprojects.com/p/jinja/)
- [MarkupSafe](https://palletsprojects.com/p/markupsafe/) — 转义用户的输入
- [ItsDangerous](https://palletsprojects.com/p/itsdangerous/) — 安全地标记数据，保护 session 和 cookie。
- [Click](https://palletsprojects.com/p/click/) — 命令行应用框架。

可选依赖（不会自动安装，Flask 会在你安装了它们时使用）：

- [Blinker](https://pythonhosted.org/blinker/) 为 [Signals](https://flask.palletsprojects.com/en/1.1.x/signals/#signals) 提供支持
- [SimpleJSON](https://simplejson.readthedocs.io/en/latest/) — JSON 编码和解码
- [python-dotenv](https://github.com/theskumar/python-dotenv#readme) - 环境配置工具
- [watchdog](https://pythonhosted.org/watchdog/) - 重载器

## 2. 虚拟环境

- venv — python3 自带 venv，不如 [virtualenv](https://virtualenv.pypa.io/en/latest/)。
- pipenv — 推荐，相当于 virtualenv 和 pip 的合体。

### 2.1. 创建虚拟环境

创建项目文件夹和 venv 文件夹：

```
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv

## python2
$ python2 -m virtualenv venv
```

开发项目前，激活相应的环境：

```
$ . venv/bin/activate
```

安装 Flask：

```
$ pip install Flask
```

## 3. Pipenv

在当前用户下安装 pipenv：

```sh
$ pip3 install --user pipenv
```

创建虚拟环境：

```sh
$ pipenv install
```

报错

```diff
- AttributeError: module 'os' has no attribute 'PathLike'
```

原因： python 3.6 才开始支持 [PathLike](https://docs.python.org/zh-cn/3/library/os.html?highlight=pathlike#os.PathLike)。  
