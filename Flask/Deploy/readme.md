# 通过 Nginx 部署 Flask 项目和静态站点

<details>
<summary>Resources</summary>

- [uWSGI 官方中文文档](https://uwsgi-docs-zh.readthedocs.io/zh_CN/latest/index.html)  
- [Supervisor](http://www.supervisord.org/) — 进程管理系统。  
- [通过Nginx部署flask项目和静态站点 | 简书](https://www.jianshu.com/p/aed6b5204225)  
- [在 Ubuntu 上使用 Nginx 部署 Flask 应用 | oschina](https://www.oschina.net/translate/serving-flask-with-nginx-on-ubuntu)  
- [Flask+uwsgi+Nginx部署应用 | 简书](https://www.jianshu.com/p/84978157c785)  
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
$ sudo service nginx supervisor
# 或
$ systemctl start nginx
$ systemctl start supervisor
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

## 三、静态 Web 服务器

假设静态文件在 `/home/user/www/html` 下：  
```sh
$ ls /home/user/www/html
index.html static
```

## 四、单个 Flask 项目

## 五、多个 Flask 项目
