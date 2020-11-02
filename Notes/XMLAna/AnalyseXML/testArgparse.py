# argparse 模块示例

import argparse
import os, sys

argParser = argparse.ArgumentParser(description='作用： 统计瑕疵光学采样的结果')
argParser.add_argument('originPath', help='样品所在的根目录名')
argParser.add_argument('-o', '--output', help='保存分析结果的文件名')

args = argParser.parse_args()
print(args)
print(args.originPath, args.output)

# 判断 originPath 是否是个目录
if (not os.path.exists(args.originPath)):
    argParser.error('文件夹 ' + args.originPath + ' 不存在')
if (not os.path.isdir(args.originPath)):
    argParser.error(args.originPath + ' 不是一个文件夹')

resultFile = args.output if args.output else os.path.join(args.originPath, 'result.txt')
print(resultFile)

# 创建、读取、写入文件
with open(resultFile, 'w') as fp: # 如果文件不存在，会自动创建
    print(fp.write('result'))     # 返回输入的字符数
    input('按任意按键继续：')
# 传统文件写入的方式
fp2 = open('result2.txt', 'w')
try:
    fp2.write('line1')
    fp2.write('line2')
    input('调用 close() 方法后，文本内容才会写入！')
finally:
    fp2.close()
