# Flask

<details>
  <summary>参考：</summary>
  
</details>

## pipenv
1、 在当前用户下安装 pipenv
```sh
$ pip3 install --user pipenv
```

&nbsp;  
2、 创建虚拟环境
```sh
$ pipenv install
```
报错
```diff
- AttributeError: module 'os' has no attribute 'PathLike'
```
原因： python 3.6 开始支持 [PathLike](https://docs.python.org/zh-cn/3/library/os.html?highlight=pathlike#os.PathLike)。  
