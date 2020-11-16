# Python2 转 Python3 引起的问题

## Dictionary view objects
由 dict.keys(), dict.values() 和 dict.items() 返回的 视图对象。  
提供一个字典实体的动态视图。这意味着字典改变时，这个视图会反映相应的变化。  

python2 返回的是列表。  

```diff
- TypeError: 'dict_values' object does not support indexing
- AttributeError: 'dict_keys' object has no attribute 'remove'

```
解决：  
```py
# py2
dict.values()
dict.keys()
# py3
valueList = list(dict.values())
keyList = list(dict)
```
