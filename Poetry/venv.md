# [venv 创建虚拟环境](https://docs.python.org/zh-cn/3.9/library/venv.html#module-venv)

## 1. 创建虚拟环境

```
$ python3 -m venv /path/to/new/virtual/environment
```

```
environment/
├─ pyvenv.cfg
├─ bin/
├─ lib/
│  ├─ pythonX.Y/
│  │  ├─ site-packages/
```

## 2. 激活虚拟环境

linux：

```
$ source <venv>/bin/activate
```

windows:

```
environment\Scripts\activate.bat
```

## 3. 退出虚拟环境

```
$ deactivate
```
