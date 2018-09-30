import cv2
from config import *
file = f'{combat}t1.jpg'
img = cv2.imread(file)
for i in range(1,6):
    img2 = img[1149:1465,222+i*511:395+i*511]
    cv2.imshow('test',img2)
    cv2.imwrite(f'start_sign{i}.jpg',img2)
    # cv2.waitKey(0)

# img2 = img[1140:1190,210+511:387+511]
# cv2.imshow('test',img2)
# cv2.imwrite(f'start_sign.jpg',img2)
# cv2.waitKey(0)