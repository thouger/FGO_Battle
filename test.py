import cv2
import numpy as np

from compare_image.compare1 import image_similarity1
from compare_image.compare2 import compare_images
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

# from itertools import combinations
# for i in combinations(range(5), 2):
#     print(i)
#     similarity_bands_via_numpy, similarity_histogram_via_pil, similarity_vectors_via_numpy, similarity_greyscale_hash_code = \
#         image_similarity1(f'five_image/{i[0]}.png', f'five_image/{i[1]}.png')
#     print()

# img2= cv2.imread(f"five_image/1.png",0)
# x,y=img2.shape
# img2 = img2[y//2:y,0:x]
# cv2.imshow('1',img2)
# cv2.waitKey(0)

for i in range(5):
    print(i)
    img1= cv2.imread(f"five_image/{i}.jpg")
    y, x,z = img1.shape
    img1 = img1[y//2-10:y-70,0+80:x-350]
    # original =  cv2.cvtColor(img1 , cv2.COLOR_BGR2GRAY)
    # img2= cv2.imread(f"five_image/{i+1}.png",0)
    # img2 = img2[y//2-10:y-70,0+80:x-350]
    # shopped = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # compare_images(original, shopped, "Original vs. Photoshopped")
    # compare_images(img1, img2, "Original vs. Photoshopped")
    cv2.imwrite(f"five_image/{i}.jpg",img1)
    # cv2.imwrite(f"five_image/{i{1}}.png", img2)