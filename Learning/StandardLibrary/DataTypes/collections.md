# 容器
提供内建容器 `dict`, `list`, `set`, 和 `tuple` 的替代选择。  

| 类名 | 描述 |
| --- | --- |
| Counter | 字典的子类，提供了可哈希对象的计数功能 |

## Counter 计数器
计数可以是 0 和负数。  

初始化：  
```py
c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)             # a new counter from keyword args
```

和 `dict` 的区别：  
如果引用不存在的键，返回 0，而不是 KeyError。  
```py
c = Counter(['eggs', 'ham'])
c['bacon']                              # count of a missing element is zero
# 返回 0
```

设计一个计数器为 0，不能删除元素。使用 `del` 删除它：  
```py
c['sausage'] = 0                        # counter entry with a zero count
del c['sausage']                        # del actually removes the entry
```

