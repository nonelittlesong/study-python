#!usr/bin/python3.5
# encoding=utf-8

import os, shutil, time
import  glob
from multiprocessing import Process

# 获取大图片
getbigimg = lambda x: x.split('fail_image/')[0]+x.split('fail_image/')[1][:6]+'.png'
# 获取目录
getDirname = lambda x: x.split('/')[1]

dates = ['20mt_20201013_labled_product_82pcs_front-station']
for date in dates:
    top_failimgs = glob.glob(date+'/*/fail_image/Cam[1,2,3]_*.png')
    side_failimgs = glob.glob(date+'/*/fail_image/Cam[4,6]_*.png')

    # 获取同时包含正侧面瑕疵的目录
    top_dirnames = set(map(getDirname, top_failimgs))
    side_dirnames = set(map(getDirname, side_failimgs))
    both_dirnames = top_dirnames & side_dirnames

    top_big_failimgs = list(set(map(getbigimg, top_failimgs)))
    for top_big_failimg in top_big_failimgs[:]:
        print(top_big_failimg)
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
                shutil.copy(top_failimg, top_failimg.replace(date, date+'_both'))
            except:
                newpng = top_failimg.replace(date, date+'_both')
                newpath = newpng.rstrip(newpng.split('/')[-1])
                os.makedirs(newpath)
                shutil.copy(top_failimg, newpng)
        else:
            try:
                shutil.copy(top_failimg, top_failimg.replace(date, date+'_top'))
            except:
                newpng = top_failimg.replace(date, date+'_top')
                newpath = newpng.rstrip(newpng.split('/')[-1])
                os.makedirs(newpath)
                shutil.copy(top_failimg, newpng)

    for side_failimg in side_failimgs:
        side_dirname = side_failimg.split('/')[1]
        if side_dirname in both_dirnames:
            try:
                shutil.copy(side_failimg, side_failimg.replace(date, date+'_both'))
            except:
                newpng = side_failimg.replace(date, date+'_both')
                newpath = newpng.rstrip(newpng.split('/')[-1])
                os.makedirs(newpath)
                shutil.copy(side_failimg, newpng)
        else:
            try:
                shutil.copy(side_failimg, side_failimg.replace(date, date+'_side'))
            except:
                newpng = side_failimg.replace(date, date+'_side')
                newpath = newpng.rstrip(newpng.split('/')[-1])
                os.makedirs(newpath)
                shutil.copy(side_failimg, newpng)

