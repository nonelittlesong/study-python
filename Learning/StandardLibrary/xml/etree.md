# [etree API](https://docs.python.org/zh-cn/3.8/library/xml.etree.elementtree.html?highlight=etree)

## 解析 XML

xml 文件：  
```xml
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
```

解析 XML：  
```py
# 方法一 读取文件
import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

# 方法二 读取字符串
root = ET.fromstring(country_data_as_string)
```

`root` 具有标签和属性字典：  
```
>>> root.tag
'data'
>>> root.attrib
{}
```

`root` 迭代子节点：  
```
>>> for child in root：  
...    print(child.tag, child.attrib)
...
country {'name': 'Liechtenstein'}
country {'name': 'Singapore'}
country {'name': 'Panama'}
```

访问子节点：  
```
>>> root[0][1].text
'2008'
```


## 查找元素

### Element.iter()
递归遍历所有子节点（包括子级，子级的子级）：  
```
>>> for neighbor in root.iter('neighbor'):
...     print(neighbor.attrib)
...
{'name': 'Austria', 'direction': 'E'}
{'name': 'Switzerland', 'direction': 'W'}
{'name': 'Malaysia', 'direction': 'N'}
{'name': 'Costa Rica', 'direction': 'W'}
{'name': 'Colombia', 'direction': 'E'}
```

### Element.findall()
查找当前元素的直接子元素中所有带有指定标签的元素。  

### Element.find()
找带特定标签的 *第一个* 子级。  

### Element.text
访问元素的文本内容。  

### Element.get()
访问元素的属性。  

```
>>> for country in root.findall('country'):
...     rank = country.find('rank').text
...     name = country.get('name')
...     print(name, rank)
...
Liechtenstein 1
Singapore 4
Panama 68
```


## 修改 XML 文件
- Element.remove() - 删除元素
- Element.text - 修改文本字段
- Element.set() - 添加和修改属性
- Element.append() - 添加新的子元素
- ElementTree.write() - 写入修改后的 xml

```
>>> for rank in root.iter('rank'):
...     new_rank = int(rank.text) + 1
...     rank.text = str(new_rank)
...     rank.set('updated', 'yes')
...
>>> tree.write('output.xml')

>>> for country in root.findall('country'):
...     # using root.findall() to avoid removal during traversal
...     rank = int(country.find('rank').text)
...     if rank > 50:
...         root.remove(country)
...
>>> tree.write('output.xml')
```


## 构建 XML 文档
SubElement() 函数还提供了一种便捷方法来为给定元素创建新的子元素:  
```
>>> a = ET.Element('a')
>>> b = ET.SubElement(a, 'b')
>>> c = ET.SubElement(a, 'c')
>>> d = ET.SubElement(c, 'd')
>>> ET.dump(a)
<a><b /><c><d /></c></a>
```

## 命名空间

## [XPath 支持](https://docs.python.org/zh-cn/3.8/library/xml.etree.elementtree.html#xpath-support)
