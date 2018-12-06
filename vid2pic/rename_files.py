#rename all files in a folder
import os

idx = 0
dir = r'./data/dancegirl_img/'
for file in os.listdir(dir):    #os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
    new_name = f'img_{idx:04d}.png'
    os.rename(os.path.join(dir,file), os.path.join(dir,new_name))
    idx += 1