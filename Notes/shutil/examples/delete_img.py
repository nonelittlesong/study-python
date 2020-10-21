#!usr/bin/python3.5
# encoding=utf-8

import os, shutil, time
import  glob

# 获取大图片
getbigimg = lambda x: x.split('fail_image/')[0]+x.split('fail_image/')[1][:6]+'.png'
# 获取目录
getDirname = lambda x: x.split('/')[1]

rootDirs = ['test']
for rootDir in rootDirs:
    # 获取瑕疵图片
    failimgs = glob.glob(rootDir+'/*/fail_image/Cam[1-7]_*.png')

    # 获取瑕疵对应的大图
    bigFailimgs = list(set(map(getbigimg, failimgs)))
    for bigFailimg in bigFailimgs[:]:
        bigFailimg += '_'
        bigFailimgs.append(bigFailimg)
    
    # 获取所有大图
    bigImgs = glob.glob(rootDir+'/*/*.png*')

    # 获取没有瑕疵的大图
    bigPassimgs = list(set(bigImgs) - set(bigFailimg))

    # 删除没有瑕疵的大图
    for bigPassimg in bigFailimgs:
        if os.path.exists(bigPassimg):
            os.remove(bigPassimg)
