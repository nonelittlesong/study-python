#!usr/bin/python3.5
# encoding=utf-8

import os, shutil, time
import  glob
from multiprocessing import Process

getbigimg = lambda x: x.split('fail_image/')[0]+x.split('fail_image/')[1][:6]+'.png'

dates = ['19mt_20201019_online_front-station']
for date in dates:
    side_failimgs = glob.glob(date+'/*/fail_image/Cam[1,2,3]_*.png')
    #side_failimgs = glob.glob(date+'/*/fail_image/Cam[4,6]_*.png')
    big_failimgs = list(set(map(getbigimg, side_failimgs)))
    side_failimgs.extend(big_failimgs)
    for side_failimg in side_failimgs:
        try:
            shutil.copy(side_failimg, side_failimg.replace(date, date+'_top'))
            #shutil.copy(side_failimg, side_failimg.replace(date, date+'_side'))
        except:
            newpng = side_failimg.replace(date, date+'_top')
            #newpng = side_failimg.replace(date, date+'_side')
            newpath = newpng.rstrip(newpng.split('/')[-1])
            os.makedirs(newpath)
            shutil.copy(side_failimg, newpng)
