# etree 模块读取 xml 示例
#
# test.xml 文件结构：
# <annotation>
#   <path>/home/song/Pictures/test.png</path>
#   <object>
#     <name>1</name>
#     <bndbox>
#       <xmin>67</xmin>
#       <ymin>203</ymin>
#       <xmax>561</xmax>
#       <ymax>367</ymax>
#     </bndbox>
#   </object>
#   <object>
#     <name>3</name>
#     <bndbox>
#       <xmin>565</xmin>
#       <ymin>370</ymin>
#       <xmax>757</xmax>
#       <ymax>1079</ymax>
#     </bndbox>
#   </object>
#   <object>
#     <name>2</name>
#     <bndbox>
#       <xmin>755</xmin>
#       <ymin>69</ymin>
#       <xmax>1532</xmax>
#       <ymax>365</ymax>
#     </bndbox>
#   </object>
# </annotation>

import xml.etree.ElementTree as ET

xmlPath = 'AnalyseXML/test.xml'
tree = ET.parse(xmlPath)

annotation = tree.getroot()
print(annotation)      # <Element 'annotation' at 0x7fc264c43c28>
print(annotation.text) # 空字符串

path = annotation.find('path')
print(path)      # <Element 'path' at 0x7fc263551548>
print(path.text) # /home/song/Pictures/test.png

objects = annotation.findall('object')  # 返回 Element 列表
print(objects)
# [<Element 'object' at 0x7f130299ae08>,
#  <Element 'object' at 0x7f13029a1098>,
#  <Element 'object' at 0x7f13029a12c8>]

######### 修改 XML #########

# 删除元素
annotation.remove(path)
print(path)                    # <Element 'path' at 0x7fc263551548>
print(path.text)               # /home/song/Pictures/test.png
print(annotation.find('path')) # None

# 添加元素
# annotation.append('path')    # 报错，参数类型必须是 Element
annotation.append(ET.Element('path'))
path2 = annotation.find('path')
print(path2)                   #<Element 'path' at 0x7f36590a9548>
ET.dump(annotation) # <path />
path2.text = ''
ET.dump(annotation) # <path />

# 修改文本字段
path2.text = '修改后的文本字段'
print(annotation.find('path').text) # 修改后的文本字段

# 添加和修改属性
objects[0].set('objectName', '测试添加和修改属性')
print(objects[0].get('objectName')) # 测试添加和修改属性

# 将结果写入 xml 文档
ET.dump(annotation)
tree.write('AnalyseXML/test2.xml', 'utf-8')

######### 创建 XML #########

# 处理缩进
def indent(elem, level=0):
    i = '\n' + level * '  '
    if (len(elem)):
        if not elem.text or not elem.text.strip():
            elem.text = i + '  '
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

# 创建 Element
a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
indent(a)
ET.dump(a)
# <a>
#   <b />
#   <c>
#     <d />
#   </c>
# </a>
print(ET.tostring(a))
# b'<a>\n  <b />\n  <c>\n    <d />\n  </c>\n</a>\n'

# with open('test3.xml', 'w') as fp:
#     fp.write(ET.tostring(a, 'utf-8', 'text')) # 报错，参数必须是字符串，而不是字节

with open('AnalyseXML/noDir/test3.xml', 'wb') as fp:  # 不能创建目录
    fp.write(ET.tostring(a, 'utf-8'))
