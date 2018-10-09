import cv2
import numpy as np
from rolling_window import rolling_window
from PIL import Image
from config import *
# img1 = cv2.imread('2560x1440_combat/t1.jpg',0)
# img2 = cv2.imread('2560x1440_OrderCard/arts.jpg',0)
# shape = img2.shape
# array = rolling_window(img1,shape)
# for i in array:
#     for j in array:
#         if np.array_equal(img2,j):
#             print(1)
# a=np.array([[0, 1, 2],
#        [3, 4, 5],
#        [6, 7, 8]])
# b = rolling_window(a, (2,2))

# im = Image.open(f"2160x1080_CardFace/t1.jpeg")
im = Image.open(f"2560x1440_combat/t1.jpg")
# img2_size = im2.size
# # print("width & height: {}".format(img2_size))
# gap = (img2_size[0] - 1920) / 2
# left = gap
# right = img2_size[0] - gap
# top = (img2_size[1] / 2) - 100
# bottom = img2_size[1]
# # print((left, top, right, bottom))
# region = im2.crop((left, top, right, bottom))
# region.save("out.png")
# im = Image.open("out.png")
img_size = im.size
xx = 5
yy = 1
x = img_size[0] // xx
y = img_size[1] // yy
for j in range(yy):
    for i in range(xx):
        left = i * x
        up = y * j
        right = left + x
        low = up + y
        region = im.crop((left, up, right, low))
        # print((left, up, right, low))
        region.save(f"utt{i}.png")