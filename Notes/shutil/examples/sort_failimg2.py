#!usr/bin/python3.5
# encoding=utf-8

import os, shutil, time
import glob

# 需处理的目录列表
rootDirs = ['testing']

# 获取路径
getPath = lambda x: os.path.dirname(x)
# 获取大图片
getbigimg = lambda x: x.split('fail_image/')[0]+x.split('fail_image/')[1][:6]+'.png'
# 获取目录
getDirname = lambda x: x.split('/')[1]

for rootDir in rootDirs:
    
    # Step1 处理未完成的文件夹
    incompleteImgs = glob.glob(rootDir + '/*/AN_INCOMPLETE_CYCLE.png')
    incompleteDirs = list(map(getPath, incompleteImgs))
    for incompleteDir in incompleteDirs:
        shutil.copytree(incompleteDir, rootDir + '/incomplete/' + os.path.basename(incompleteDir))

    # Step2 删除无瑕疵的文件夹
    all2ndDirs = glob.glob(rootDir + '/[!i]*') # 获取 rootDir 下的所有子文件夹，去掉 incomplete
    for all2ndDir in all2ndDirs:
        if not glob.glob(all2ndDir + '/fail_image') or not os.listdir(all2ndDir + '/fail_image'):
            if all2ndDir not in incompleteDirs:
                print(all2ndDir)
                shutil.rmtree(all2ndDir)

    top_failimgs = glob.glob(rootDir+'/*/fail_image/Cam[1,2,3]_*.png')
    side_failimgs = glob.glob(rootDir+'/*/fail_image/Cam[4,6]_*.png')

    # Step3 分离正、侧面瑕疵
    # 获取同时包含正侧面瑕疵的目录
    top_dirnames = set(map(getDirname, top_failimgs))
    side_dirnames = set(map(getDirname, side_failimgs))
    both_dirnames = top_dirnames & side_dirnames

    top_big_failimgs = list(set(map(getbigimg, top_failimgs)))
    for top_big_failimg in top_big_failimgs[:]:
        top_big_failimg_ = top_big_failimg+'_'
        if os.path.exists(top_big_failimg_):
            top_big_failimgs.append(top_big_failimg_)
    side_big_failimgs = list(set(map(getbigimg, side_failimgs)))
    for side_big_failimg in side_big_failimgs[:]:
        side_big_failimg_ = side_big_failimg + '_'
        if os.path.exists(side_big_failimg_):
            side_big_failimgs.append(side_big_failimg_)
    top_failimgs.extend(top_big_failimgs)
    side_failimgs.extend(side_big_failimgs)

    for top_failimg in top_failimgs:
        top_dirname = top_failimg.split('/')[1]
        if top_dirname in both_dirnames:
            try:
                shutil.copy(top_failimg, top_failimg.replace(rootDir, rootDir+'_both'))
            except:
                newpng = top_failimg.replace(rootDir, rootDir+'_both')
                newpath = newpng.rstrip(newpng.split('/')[-1])
                os.makedirs(newpath)
                shutil.copy(top_failimg, newpng)
        else:
            try:
                shutil.copy(top_failimg, top_failimg.replace(rootDir, rootDir+'_top'))
            except:
                newpng = top_failimg.replace(rootDir, rootDir+'_top')
                newpath = newpng.rstrip(newpng.split('/')[-1])
                os.makedirs(newpath)
                shutil.copy(top_failimg, newpng)

    for side_failimg in side_failimgs:
        side_dirname = side_failimg.split('/')[1]
        if side_dirname in both_dirnames:
            try:
                shutil.copy(side_failimg, side_failimg.replace(rootDir, rootDir+'_both'))
            except:
                newpng = side_failimg.replace(rootDir, rootDir+'_both')
                newpath = newpng.rstrip(newpng.split('/')[-1])
                os.makedirs(newpath)
                shutil.copy(side_failimg, newpng)
        else:
            try:
                shutil.copy(side_failimg, side_failimg.replace(rootDir, rootDir+'_side'))
            except:
                newpng = side_failimg.replace(rootDir, rootDir+'_side')
                newpath = newpng.rstrip(newpng.split('/')[-1])
                os.makedirs(newpath)
                shutil.copy(side_failimg, newpng)
