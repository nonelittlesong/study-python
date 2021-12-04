# 映射类型
<details>
<summary>参考：</summary>

- [为什么Python 3.6以后字典有序并且效率更高？](https://zhuanlan.zhihu.com/p/73426505)  
</details>

在 3.5(含) 之前，字典是无序的。从 3.6 开始，字典有序。  

构造字典：  
- 使用花括号内以逗号分隔 `键: 值` 对的方式: `{'jack': 4098, 'sjoerd': 4127}` or `{4098: 'jack', 4127: 'sjoerd'}`  
- 使用字典推导式: `{}`, `{x: x ** 2 for x in range(10)}`  
- 使用类型构造器: `dict()`, `dict([('foo', 100), ('bar', 200)])`, `dict(foo=100, bar=200)`

