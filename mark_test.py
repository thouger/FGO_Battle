# -*- coding:utf-8 -*-
from combat_analysis import find_area, mark, marks, img_grey
from utils.config import *
import cv2
import numpy as np
# img,sign = f"../{combat}t1.jpg",f"../{OrderCard}arts.jpg"
img,template ='2160x1080_CardFace/t1.jpeg','2160x1080_OrderCard/quick.png'
# 6 中匹配效果对比算法
# methods = ['cv2.TM_CCOEFF']
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
threshold=0.95
for meth in methods:
    # left_top,right_bottom,center=find_area(img,sign,meth)
    template_img = cv2.cvtColor(cv2.imread(template), cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_grey(img), template_img, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= threshold)
    OrderCard_x = np.mean(loc[0]).astype(np.int)
    OrderCard_y = loc[1]
    marks(img,template,OrderCard_x,OrderCard_y)