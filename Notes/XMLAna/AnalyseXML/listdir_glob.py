import os, glob

# --------- listdir ---------
# 报错 Not a directory
# listdir_array = os.listdir('/home/song/Pictures/cat.jpg')
# print(listdir_array)

# 报错 无法解析~
# listdir_array = os.listdir('~/Pictures')
# print(listdir_array)
listdir_array = os.listdir('/home/song/Pictures')
print(listdir_array)

# --------- glob ---------
# 可获取文件和文件夹
glob_array = glob.glob('/home/song/Pict*')
print(glob_array) # ['/home/song/Pictures']

glob_array = glob.glob('/home/song/Pictures/*.png')
print(glob_array)

glob_array = glob.glob('~/Pictures/*.png')
print(glob_array) # 不能识别~

# listdir 得到的不是完整的路径
# glob    得到的是完整的路径