# Click

- `flask --help` - 查看帮助

## 启动内嵌服务器

```sh
$ flask run
# --host=0.0.0.0 对外可见
# --port=xxxx    设置端口
```

规则：  
- 寻找 app.py 和 wsgi.py 模块，并从中寻找名为 app 或 application 的程序实例。  
- 从环境变量 FLASK_APP 对应的模块名/导入路径寻找名为 app 或 application 的程序实例。  
- 安装 `python-dotenv`，环境变量 > .env > .flaskenv。  

## flask shell

```sh
$ flask shell
>>>
```

## 自定义命令

- [click](https://click.palletsprojects.com)

```py
@app.cli.command() # 参数 指令名称，默认为函数名
def hello():
    """Just say hello.""" # 帮助文档
    click.echo('Hello, Human!')
```
