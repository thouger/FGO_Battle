# -*- coding:utf-8 -*-
from utils.positioning import find_area, mark

from utils.config import *

img = f"../{combat}t.jpg"
sign = f"../{combat}start_combat.jpg"
# 6 中匹配效果对比算法
methods = ['cv2.TM_CCOEFF']
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    left_top,right_bottom=find_area(img,sign,meth)
    mark(img,sign,[left_top,right_bottom])