# 通过 Nginx 部署 Flask 项目和静态站点

<details>
<summary>Resources</summary>

- [uWSGI 官方中文文档](https://uwsgi-docs-zh.readthedocs.io/zh_CN/latest/index.html)  
- [Supervisor](http://www.supervisord.org/) — 进程管理系统。  
- [通过Nginx部署flask项目和静态站点 | 简书](https://www.jianshu.com/p/aed6b5204225)  
- [在 Ubuntu 上使用 Nginx 部署 Flask 应用 | oschina](https://www.oschina.net/translate/serving-flask-with-nginx-on-ubuntu)  
- [Flask+uwsgi+Nginx部署应用 | 简书](https://www.jianshu.com/p/84978157c785)  
- [Centos+Nginx+flask（单服务器多项目部署）| CSDN](https://blog.csdn.net/u014446012/article/details/109815776)  
</details>

<details>
<summary>Contents</summary>

- [环境准备](#一环境准备)
- [Nginx 配置](#二Nginx-配置)
- [静态 Web 服务器](#三静态-Web-服务器)
- [单个 Flask 项目](#四单个-Flask-项目)
- [多个 Flask 项目](#五多个-Flask-项目)
</details>

## 一、环境准备

>涉及内容：`nginx+html` & `nginx + supervisor + uwsgi + flask`  
>系统版本：Ubuntu 16.04 LTS

配置环境：  
```sh
# 安装 nginx
$ sudo apt-get install nginx

# 安装 supervisor
$ sudo apt-get install supervisor
# 或
$ pip3 install supervisor
# 只支持python 2.x, pip安装不会在/etc/supervisor自动生成默认配置文件，
# 但可以使用命令echo_supervisord_conf > /etc/supervisord.conf

# 安装 uwsgi
$ pip3 install uwsgi
```

启动服务：  
```sh
$ sudo service nginx start
$ sudo service supervisor start
# 或
$ sudo systemctl start nginx
$ sudo systemctl start supervisor
```

查看日志：  
```sh
# nginx 日志（默认）
$ cat /var/log/nginx/access.log
$ cat /var/log/nginx/error.log
# supervisor 日志（默认）
$ cat /var/log/supervisor/supervisord.log
```

supervisor 命令：  
```sh
# 指定配置启动
supervisord -c supervisord.conf

# 查看启动的进程
$ sudo supervisorctl status
# flask_hello                      RUNNING   pid 8950, uptime 0:39:18
# flask_world                      RUNNING   pid 8951, uptime 0:39:18

# 控制所有进程
$ sudo supervisorctl start all
$ sudo supervisorctl stop all
$ sudo supervisorctl restart all

# 控制目标进程
$ sudo supervisorctl stop httpRunnerLoan
$ sudo supervisorctl start httpRunnerLoan
$ sudo supervisorctl restart httpRunnerLoan
```

## 二、Nginx 配置

### 2.1 全局配置文件 `nginx.conf`

一般需要配置下面两项，其他保持默认  
```
user www-data
worker_processes auto
```

其他配置见下文······  

## 三、静态 Web 服务器

假设静态文件在 `/home/user/www/html` 下：  
```sh
$ ls /home/user/www/html
index.html static
```

**配置 nginx：**  
复制默认配置文件：  
```sh
cp /etc/nginx/sites-available/default /etc/nginx/sites-available/mysite
```
编辑 `mysite` 配置文件：  
```
server {
    listen 80;  # 监听端口
    server_name 192.168.1.4;  # 监听的host
    root  /home/moco/www/html;  # 站点的根目录
    charset utf-8;
    client_max_body_size 75M;
    # 路由位置
    location / {
        index  index.html index.htm;
    }
}
```
如果配置多个：  
```
server {
    listen 80;
    server_name 192.168.1.4;
    charset utf-8;
    client_max_body_size 75M;
    location / {
        root  /home/moco/www/html;
        index  index.html index.htm;
    }
    location /tool {
        root  /home/moco/other/;
        index  index.html index.htm;
    }
    location /tool2 {
        alias  /home/moco/www/tool/;
        index  index.html index.htm;
    }
}
```
>**root 和 alias 的区别：**  
>alias 指定的目录就是要访问的目录，root 是要访问目录的上级目录。  
>使用 root 时，静态文件的实际路径等于 root+location 的路径，如上面的第二个 location,站点文件必须在 /home/moco/other/tool/ 下。  
>而使用 alias，则静态文件的路径就是 alias 路径，即第三个 location 站点文件就在 home/moco/www/tool/ 下。  
>**使用 alias 时后面接的目录名一定要加 「/」**。  

## 四、单个 Flask 项目
项目路径：`/home/user/www/myflask/`:  
```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/moco")
def moco():
    return "Hello moco!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```
配置 uWSGI：  
```
[uwsgi]
# uwsgi 启动时所使用的地址与端口,也可以使用.sock文件的方式
socket = 127.0.0.1:5000
# 指向网站目录
chdir = /home/moco/www/myflask
# python 启动程序文件
wsgi-file = manage.py
# python 程序内用以启动的 application 变量名
callable = app
# 处理器数
processes = 1
# 线程数
threads = 1
#状态检测地址
stats = 127.0.0.1:5001
#项目flask日志文件
logto = /home/moco/www/myflask/log.log
```
启动 uWSGI：  
```sh
uwsgi uwsgi.ini
```
配置 nginx：  
```
server {
    listen 80;
    server_name 192.168.1.4;
    charset utf-8;
    client_max_body_size 75M;
    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:5000;
    }
}
```

## 五、多个 Flask 项目
uwsgi1.ini：  
```
[uwsgi]
# uwsgi 启动时所使用的地址与端口
socket = 127.0.0.1:5001

# 指向网站目录（这里nginx会传参过来，所以不需要了）
# chdir = /home/moco/www/flask_hello

# python 启动程序文件
# wsgi-file = app.py 

# python 程序内用以启动的 application 变量名
callable = app
# 处理器数
processes = 1
# 线程数
threads = 1
#状态检测地址
stats = 127.0.0.1:5002
#项目flask日志文件
logto = /home/moco/www/flask_hello/log.log

mount=/hello=manage.py
manage-script-name=true
```
uwsgi2.ini：  
```
[uwsgi]
# uwsgi 启动时所使用的地址与端口
socket = 127.0.0.1:6001

# 指向网站目录
# chdir = /home/moco/www/flask_world

# python 启动程序文件
# wsgi-file = app.py 

# python 程序内用以启动的 application 变量名
callable = app
# 处理器数
processes = 1
# 线程数
threads = 1
#状态检测地址
stats = 127.0.0.1:6002
#项目flask日志文件
logto = /home/moco/www/flask_world/log.log

mount=/world=manage.py
manage-script-name=true
```
因为要启动多个 uWSGI 配置文件，所以用 supervisor 统一管理  
在 `/etc/supervisor/conf.d/` 下，  
添加 `flask_hello.conf`：  
```
[program:flask_hello]
# 启动命令入口
command=/home/moco/.local/share/virtualenvs/myflask-XuRgNXhR/bin/uwsgi /home/moco/www/flask_hello/uwsgi_config.ini
# 命令程序所在目录
directory=/home/moco/www/flask_hello
#运行命令的用户名
user=moco
autostart=true
autorestart=true
#日志地址
stdout_logfile=/home/moco/www/flask_hello/uwsgi_supervisor.log
```
添加 `flask_world.conf`：  
```
[program:flask_world]
# 启动命令入口
command=/home/moco/.local/share/virtualenvs/myflask-XuRgNXhR/bin/uwsgi /home/moco/www/flask_world/uwsgi_config.ini

# 命令程序所在目录
directory=/home/moco/www/flask_world
#运行命令的用户名
user=moco

autostart=true
autorestart=true
#日志地址
stdout_logfile=/home/moco/www/flask_world/uwsgi_supervisor.log
```

启动 supervisor：  
```sh
sudo service supervisor start
```

配置 nginx：  
```
server {
    listen 80;
    server_name 192.168.1.4
    charset utf-8;
    client_max_body_size 75M;
    # 这里location 自定义，也可以是 /
    location /hello {
        include uwsgi_params;
        uwsgi_param SCRIPT_NAME /hello;
        uwsgi_pass 127.0.0.1:5001;
        uwsgi_param UWSGI_PYHONE /home/moco/.local/share/virtualenvs/myflask-XuRgNXhR;
        uwsgi_param UWSGI_CHDIR /home/moco/www/flask_hello;
        uwsgi_param UWSGI_SCRIPT manage:app;
    }
    location /world {
        include uwsgi_params;
        uwsgi_param SCRIPT_NAME /world;
        uwsgi_pass 127.0.0.1:6001;
        uwsgi_param UWSGI_PYHONE /home/moco/.local/share/virtualenvs/myflask-XuRgNXhR;
        uwsgi_param UWSGI_CHDIR /home/moco/www/flask_world;
        uwsgi_param UWSGI_SCRIPT manage:app;
    }
}
```

>这里 `uwsgi_param SCRIPT_NAME xxx` 要与 uwsgi 配置中的 `mount=xxx` 保持一致，且不能与flask中的路由节点相同。最终 nginx 会把这些参数传给uwsgi。  
>`nginx location /hello` 可以根据需要自定义，也可以是 `'/'`，最终访问 url = /hello + flask 中的路由。  
>如果启动 nginx 后无法访问，可以尝试吧 uwsgi 再重启下， `sudo service supervisor start`。  
