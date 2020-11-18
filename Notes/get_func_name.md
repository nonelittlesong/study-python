# 获取当前方法的名称

- [python3 获取当前运行函数名称和类方法名称](https://blog.csdn.net/a1007720052/article/details/107342733)  

## 函数名
```py
def create():
    print("hello word")
print(create.__name__)
# create

import sys
def create():
    print(f"当前方法名：{sys._getframe().f_code.co_name}")
create()
# 当前方法名：create
```

## 类名
```py
import sys

class Object():
    def filter(self,*args, **kwargs):
        return Filter(*args, **kwargs)

    def create(self):
        print(f'当前类名称：{self.__class__.__name__}')
        print(f"当前方法名：{sys._getframe().f_code.co_name}")

o=Object()
o.create()
# 当前类名称：Object
# 当前方法名：create
```
