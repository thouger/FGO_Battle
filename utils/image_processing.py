# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 16:39
# @Author  : thouger
# @Email   : 1030490158@qq.com
# @File    : image_processing.py
# @Software: PyCharm

from functools import reduce

from tensorflow.python.ops.image_ops_impl import ssim

from utils.config import *
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

# TODO get_double_damage,get_half_damage的图片需要用ps裁剪

"""
识别图像位置函数

输入一处从大图像中的一小片段图像，以及一整幅图像，找到识别需要图像的位置并返回

:parameter
----------
img:完整图像，string
sign:需要识别的图像，string
method:cv2采用识别的方法，string

:returns
---------
left_top:左上角坐标
right_bottom:右下角坐标
center:中心坐标

"""


def find_area(img, sign, method='cv2.TM_CCOEFF'):
    img = cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2GRAY)
    sign = cv2.cvtColor(cv2.imread(sign), cv2.COLOR_BGR2GRAY)
    w, h = sign.shape[::-1]
    res = cv2.matchTemplate(img, sign, eval(method))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        left_top = min_loc
    else:
        left_top = max_loc
    right_bottom = (left_top[0] + w, left_top[1] + h)
    center = [reduce(lambda x, y: (x + y) / 2, i) for i in zip(left_top, right_bottom)]
    return left_top, right_bottom, center


# todo:注释
def find_many_area(img, sign, method, threshold):
    img = cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2GRAY)
    sign = cv2.cvtColor(cv2.imread(sign), cv2.COLOR_BGR2GRAY)
    w, h = sign.shape[::-1]
    res = cv2.matchTemplate(img, sign, eval(method))
    points = np.where(res > threshold)
    return points


"""
标记出一个片段图像在整副图像的位置

输入一处从大图像中的一小片段图像，一整幅图像，左上角坐标、右下角坐标，标记处该图像处于整副图像的位置

:parameter
----------
img:完整图像，string
sign:需要识别的图像，string
args:左上角坐标、右下角坐标，list

"""


def mark(img, sign, args):
    img = cv2.imread(img)
    img2 = img.copy()
    sign = cv2.imread(sign)
    cv2.rectangle(img2, args[0], args[1], 255, 2)

    plt.subplot(221), plt.imshow(img, cmap="gray")
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(sign, cmap="gray")
    plt.title('sign Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(212), plt.imshow(img2, cmap="gray")
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.show()


"""
标记出片段图像在整副图像的位置

输入N处从大图像中的一小片段图像，一整幅图像，阈值，标记处该图像处于整副图像的位置

:parameter
----------
img:完整图像，string
sign:需要识别的图像，string
threshold:阈值，num
"""


def marks(img, template, threshold=0.9):
    img = img_grey(img)
    template = img_grey(template)
    w, h = template.shape[::-1]
    res = recognize(img, template)
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):  # *号表示可选参数
        right_bottom = (pt[0] + w, pt[1] + h)
        cv2.rectangle(img, pt, right_bottom, (0, 0, 255), 2)
    plt.subplot(111)
    plt.imshow(img)
    plt.show()


"""
标记坐标在图像的位置

:parameter
----------
img:被标记的图像，string
point:坐标，list
"""
def mark_point(img, point):
    plt.imshow(Image.open(img))
    plt.annotate(f'{point[0], point[1]}', xy=point, xycoords='data',
                 xytext=(0.5, 0.5), textcoords='figure fraction',
                 arrowprops=dict(arrowstyle="->"))
    plt.show()

"""
显示图像坐标

显示用鼠标点击的图像坐标
"""
def get_picture_XY(img):
    x,y=[],[]
    def on_press(event):
        x.append(event.xdata)
        y.append(event.ydata)
        print("my position:", event.button, event.xdata, event.ydata)
    fig = plt.figure()
    img = Image.open(img)
    plt.imshow(img, animated= True)
    fig.canvas.mpl_connect('button_press_event', on_press)
    plt.show()
# 模板匹配函数的包装
recognize = lambda img, template: cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
# 图像灰度
img_grey = lambda img: cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2GRAY)


def compare_images(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    SSIM = ssim(imageA, imageB)
    return err,SSIM

#-----------------------------------------------------------------------------------
#以下都是没有经过测试的代码
def FeaturePoint_detection(img):
    img = cv2.imread(img)

    # 检测
    # akaze = cv2.AKAZE_create()
    # akaze = cv2.BRISK_create()
    akaze = cv2.FastFeatureDetector_create()
    # akaze = cv2.KAZE_create()
    # akaze = cv2.ORB_create()
    keypoints = akaze.detect(img, None)

    # 显示
    # 必须要先初始化img2
    img2 = img.copy()
    img2 = cv2.drawKeypoints(img, keypoints, img2, color=(0, 255, 0))
    cv2.imshow('Detected AKAZE keypoints', img2)
    cv2.waitKey(0)

def crop_image(img):
    file = f'../{combat}t1.jpg'
    img = cv2.imread(file)
    for i in range(1, 6):
        img2 = img[826:826 + 382 // 2, 105 + (300 + 213) * (i - 1):105 + (300 + 213) * (i - 1) + 300]
        # img2=img[826:826 + 382, 105 * i:105 * (i + 1)]
        cv2.imshow('1', img2)
        # cv2.imshow('test',img2)
        cv2.imwrite(f'start_sign{i}.jpg', img2)

def resize_picture(img):
    img = cv2.imread('../test/img2.png')
    img2 = cv2.resize(img, cv2.imread('../test/img1.png', 0).shape[::-1])
    cv2.imwrite('../test/img3.png', img2)

def png_to_jpg():
    im = Image.open(f"../{combat}start_combat.png")
    rgb_im = im.convert('RGB')
    rgb_im.save(f"../{combat}start_combat.jpg")
if __name__ == '__main__':
    # get_picture_XY(f'../{combat}/t1.jpg')
    get_picture_XY(f'../{combat}/t.jpg')
    # get_picture_XY(f'../{home}start.jpg')
    # get_picture_XY('../out.png')
    print()