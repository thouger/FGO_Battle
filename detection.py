# -*- coding:utf-8 -*-
from positioning import find_area, mark

from config import *
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(f"{combat}t5.jpg")
sign = cv2.imread(f"{OrderCard}quick.jpg")
# 6 中匹配效果对比算法
methods = ['cv2.TM_CCOEFF']
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    left_top,right_bottom=find_area(img,sign,meth)
    mark(img,sign,left_top,right_bottom)