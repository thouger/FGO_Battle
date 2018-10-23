#coding:utf-8
# from itertools import combinations
#
# from compare_image.compare1 import image_similarity1
#
# if __name__ == '__main__':
#     for i in combinations(range(1,6), 2):
#         print(i)
#         # img1,img2=f'tmp/{i[0]}.jpg',f'tmp/{i[1]}.jpg'
#         img1, img2 = f'tmp/follow{i[0]}.jpg', f'tmp/follow{i[1]}.jpg'
#         # similarity_bands_via_numpy, similarity_histogram_via_pil, similarity_vectors_via_numpy, similarity_greyscale_hash_code = \
#         #     image_similarity1(img1,img2)
#         image_similarity1(img1, img2)
#
#         # compare_images(cv2.cvtColor(cv2.imread(f"five_image/{i[0]}.jpg"), cv2.COLOR_BGR2GRAY), cv2.cvtColor(cv2.imread(f"five_image/{i[1]}.jpg"), cv2.COLOR_BGR2GRAY), "Original vs. Photoshopped")
#
#         # i1 = Image.open(f'../five_image/{i[0]}.jpg')
#         # i2 = Image.open(f'../five_image/{i[1]}.jpg')
#         # compare3(i1,i2)
#         # print()



# -*- coding:utf-8 -*-
__author__ = 'Microcosm'

import cv2
import numpy as np
from matplotlib import pyplot as plt
img,sign ='2160x1080_CardFace/t1.jpeg','2160x1080_OrderCard/quick.png'
img = cv2.imread(img, 0)
img2 = img.copy()
template = cv2.imread(sign, 0)
w, h = template.shape[::-1]

# 6 中匹配效果对比算法
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()

    method = eval(meth)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    print(meth)
    plt.subplot(221), plt.imshow(img2, cmap="gray")
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(template, cmap="gray")
    plt.title('template Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(res, cmap="gray")
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(img, cmap="gray")
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.show()