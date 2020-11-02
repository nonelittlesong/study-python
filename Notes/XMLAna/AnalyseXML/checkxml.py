#!usr/bin/python3.5
# encoding=utf-8
# ------------检查标注后xml位置------------
# 1. 被标注文件夹添加到folders文件夹，以ok_20190817_all等级文件夹为单位
# 2. 子文件夹下只有大图片和对应xml

import os, glob, shutil
from xml.etree import ElementTree

def strip_voidspace(string):
    new_string = string.replace('\n', '').strip()
    return new_string

path = os.getcwd()
dates = ['Public']
for date in dates:
    xmls = glob.glob(date+'/*/*.xml')
    for xml in xmls:
        tree = ElementTree.parse(xml)
        root = tree.getroot()
        target_path = strip_voidspace(root.find('path').text).replace('.png', '.xml')
        actual_path = os.path.join(path, xml)
        if target_path != actual_path:
            print(u'***********xml位置错误***********')
            print(u'原始路径： ', actual_path)
            print(u'目标路径： ', target_path)
            if os.path.exists(target_path):
                print(target_path, u' 已存在，非法移动导致文件覆盖，禁止移动')
            else:
                shutil.move(actual_path, target_path)
                print(u'移动完成')
        for object_attribute in root.findall('object'):
            try:
                classify = int(object_attribute.find('name').text)
            except:
                print(u'***********瑕疵名缺失***********')
                print(u'xml位置： ', target_path)
