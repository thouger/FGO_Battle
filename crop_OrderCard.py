import cv2
from config import *
file = f'{combat}t1.jpg'
img = cv2.imread(file)
for i in range(5):
    img2 = img[1140:1190,210+511*i:387+511*i]
    cv2.imshow('test',img2)
    cv2.imwrite(f'{OrderCard}start_sign{i}.jpg',img2)

# img2 = img[1145:1185,210+511*4:387+511*4]
# cv2.imshow('test',img2)
# cv2.imwrite(f'start_sign.jpg',img2)
# cv2.waitKey(0)