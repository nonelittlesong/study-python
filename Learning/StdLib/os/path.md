
## [os.path](https://docs.python.org/zh-cn/3.7/library/os.path.html#module-os.path)

### [os.path.join(path, \*paths)](https://docs.python.org/zh-cn/3.7/library/os.path.html#os.path.join)
合理地拼接一个或多个路径部分。  

返回值是 `path` 和 `*paths` 所有值的连接，每个非空部分后面都紧跟一个目录分隔符 (`os.sep`)，除了最后一部分。这意味着如果最后一部分为空，则结果将以分隔符结尾。  

如果参数中某个部分是绝对路径，则绝对路径前的路径都将被丢弃，并从绝对路径部分开始连接。  

### os.path.isdir(path)
如果 _path_ 指向的现有的目录，则返回 True。  
如果符号链接指向一个目录，也会返回 True。所以，对于一个路径，可能 `islink()` 和 `isdir()` 都为 True。  

