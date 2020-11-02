# 统计瑕疵
#
# 源目录结构例子：
# originPath
# ├─20201020-103703
# │ ├─Cam4_4.png
# │ ├─Cam1_3.png
# │ └─Cam4_4.xml
# └─20201020-103702
#

import argparse
import os, glob, shutil
import xml.etree.ElementTree as ET

# --------- 设置命令行参数 ---------
argParser = argparse.ArgumentParser(description='作用：统计瑕疵光学采样的结果')
argParser.add_argument('originPath', help='样品所在的根目录')
argParser.add_argument('-o', '--output', help='保存分析结果的文件')
argParser.add_argument('-d', '--details', help='是否保存详细的结果', action='store_true')
args = argParser.parse_args()
# 判断参数 originPath 是否是个目录，不是则终止程序
if (not os.path.exists(args.originPath)):
    argParser.error('文件夹 ' + args.originPath + ' 不存在')
if (not os.path.isdir(args.originPath)):
    argParser.error(args.originPath + ' 不是一个文件夹')
# 读取保存结果的文件名，默认 'originPath/result.txt'
resultFile = args.output if args.output else os.path.join(args.originPath, 'result.txt')
# 是否保存详细信息
isDetails = True if args.details else False

# --------- 分析数据 ---------
# 定义
originPath = args.originPath # 源路径 会解析 ~ 字符
results = {} # 保存分析结果的字典

dateList = glob.glob(originPath + '/2*') # 例 /home/song/originpath/20201010-143333
print(dateList)
for date in dateList:
    xmlList = glob.glob(date + '/*.xml')
    for xmlfile in xmlList:
        # 解析 xml 文档
        tree = ET.parse(xmlfile)
        annotation = tree.getroot()

        objects = annotation.findall('object')
        print(objects[0].text)

# 放弃了，特殊情况太多了，不好搞