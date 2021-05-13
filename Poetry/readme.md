
# [Poetry](https://python-poetry.org/)

依赖管理和打包。

>不支持 Python 3.5 以下版本。
>`poetry` 会检测是否在 virtualenv 中并安装相应的包。所以，可以全局地安装 poetry 并随处可用。

## 1. 安装

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

## 安装指定版本
python install-poetry.py --version 1.2.0
```

卸载：

```
python install-poetry.py --uninstall
```

更新：

```
poetry self update            # 最新的稳定版
poetry self update --preview  # preview 版
poetry self update 1.2.0      # 指定版本
```

## 2. 使用

查看：

```
## 查看依赖
$ poetry show --tree

## 查看最新版本的包
$ poetry show --latest

```

创建：

```
## 创建一个新的项目
$ poetry new poetry-demo

## 在现有项目中添加 poetry
$ poetry init
```

添加：

```
$ poetry add <package>            # 安装最新稳定版本的包
$ poetry add <package> --dev      # 安装开发环境下的包
$ poetry add <package>=<version>  # 安装指定版本的包
$ poetry install                  # 安装 pyproject.toml 下的所有包
$ poetry install --no-dev         # 安装 pyproject.toml 下的所有非 dev 包
```

更新：

```
$ poetry update            # 更新所有包
$ poetry update <package>  # 更新指定包
$ poetry show --outdate    # 查看可更新包
```

删除：

```
$ poetry remove <package>
```

## 3. 虚拟环境

>如果在配置文件中配置了 `virtualenvs.create=true`，执行 `poetry install` 时会检查是否有虚拟环境，否则会自动创建。

指定创建虚拟环境时的 Python 版本：

```
$ poetry env use python3.7
```

```
## 激活虚拟环境
$ poetry shell

## 查看虚拟环境的信息
$ poetry env info

## 显示虚拟环境列表
$ poetry env list

## 显示虚拟环境的路径
$ poetry env list --full-path

## 删除虚拟环境
$ poetry env remove python3.7

## 查看 python 版本
$ poetry run python -V
```

## 比较 Pipenv

pipenv 的依赖解析不稳定，例如：

```
pipenv install oslo.utils==1.4.0
# 结果
- Could not find a version that matches pbr!=0.7,!=2.1.0,<1.0,>=0.6,>=2.0.0
```

而 Poetry 能够给你正确的包：

```
poetry add oslo.utils=1.4.0
# 结果
  - Installing pytz (2018.3)
  - Installing netifaces (0.10.6)
  - Installing netaddr (0.7.19)
  - Installing oslo.i18n (2.1.0)
  - Installing iso8601 (0.1.12)
  - Installing six (1.11.0)
  - Installing babel (2.5.3)
  - Installing pbr (0.11.1)
  - Installing oslo.utils (1.4.0)
```