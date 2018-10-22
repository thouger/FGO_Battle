import cv2
from utils.config import *
file = f'../{combat}t1.jpg'
img = cv2.imread(file)
for i in range(1,6):
    img2 = img[826:826+382//2,105+(300+213)*(i-1):105+(300+213)*(i-1)+300]
    # img2=img[826:826 + 382, 105 * i:105 * (i + 1)]
    cv2.imshow('1', img2)
    # cv2.imshow('test',img2)
    cv2.imwrite(f'start_sign{i}.jpg',img2)
    # cv2.waitKey(0)

# img2 = img[1140:1190,210+511:387+511]
# cv2.imshow('test',img)
# cv2.waitKey(0)
# cv2.imwrite(f'start_sign.jpg',img2)
# cv2.waitKey(0)
