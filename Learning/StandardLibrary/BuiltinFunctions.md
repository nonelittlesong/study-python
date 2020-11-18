# 内置函数

## filter(function, iterable)
function 为 None 时， iterable 中为假的元素会被删除。  

## sorted(iterable, \*, key=None, reverse=False)
对 iterable **稳定**排序。  

参数：  
- key - 带有单个参数的函数，提取用于比较的键。  
- reverse - 是否按反向顺序排序。  

返回：  
**列表**!!  

## sum(iterable, /, start=0)
```py
# 数字相加
sum([0, 1, 2, 3], 2)   # 8

# 列表相加
sum([[1], [1, 2]], []) # [1, 1, 2]
```
