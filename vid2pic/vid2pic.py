
# coding: utf-8

import cv2
from pathlib import Path
import numpy as np
import os

#res = (512, 512)
res = (1080, 1080)
img_dir = Path('./data/dancegirl_img')
img_dir.mkdir(exist_ok=True)
video_path = './data/dancegirl.mkv'

cap = cv2.VideoCapture(video_path)

width_resized = 480  #columns = 480
height_resized = 480 #rows = 480
idx = 0
i = -1
while(cap.isOpened()):
    flag, img = cap.read()
    i += 1
    if flag is False:
        break
    
    shape_dst = np.min(img.shape[:2])
    oh = (img.shape[0] - shape_dst) // 2
    ow = (img.shape[1] - shape_dst) // 2

    img = img[oh:oh+shape_dst, ow:ow+shape_dst]
    img = cv2.resize(img, (width_resized,height_resized))
    #img = cv2.resize(img, res)
    cv2.imwrite(str(img_dir.joinpath(f'img_{idx:04d}.png')), img)
    idx += 1
cap.release()

