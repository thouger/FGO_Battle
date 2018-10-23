# coding=gbk
from functools import reduce

from interval import Interval

from utils.compare_image import compare_images
from utils.config import *
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image


# TODO get_double_damage,get_half_damage的图片需要用ps裁剪
# TODO 识别从者那里有问题，mask_test.py开始修改

def find_area(img, sign, method):
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

def find_many_area(img, sign, method,threshold):
    img = cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2GRAY)
    sign = cv2.cvtColor(cv2.imread(sign), cv2.COLOR_BGR2GRAY)
    w, h = sign.shape[::-1]
    res = cv2.matchTemplate(img, sign, eval(method))
    points = np.where(res>threshold)
    return points

def mark(img, template, args):
    img = cv2.imread(img)
    img2 = img.copy()
    template = cv2.imread(template)
    cv2.rectangle(img2, args[0], args[1], 255, 2)

    plt.subplot(221), plt.imshow(img, cmap="gray")
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(template, cmap="gray")
    plt.title('template Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(212), plt.imshow(img2, cmap="gray")
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.show()


def marks(img, template, OrderCard_x, OrderCard_y_list):
    img = cv2.imread(img)
    template = cv2.imread(template)
    w, h,d = template.shape[::-1]
    for OrderCard_y in OrderCard_y_list:
        bottom_right = (OrderCard_y + w, OrderCard_x + h)
        cv2.rectangle(img, (OrderCard_y, OrderCard_x), bottom_right, 255, 2)
    plt.subplot(111)
    plt.imshow(img, cmap="gray")
    plt.show()

def judge(recognized,threshold):
    if (recognized >= threshold).any():
        return True
    else:
        return False
recognize = lambda img, template: cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
img_grey = lambda img:cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2GRAY)

def mark_point(img, point):
    # plt.imshow(cv2.imread(img))
    plt.imshow(Image.open(img))
    plt.annotate(f'{point[0], point[1]}', xy=point, xycoords='data',
                 xytext=(0.5, 0.5), textcoords='figure fraction',
                 arrowprops=dict(arrowstyle="->"))
    plt.show()


class CombatAnalysis:
    first_kill = ()

    def __init__(self, picture):
        self.threshold = 0.95
        self.methods = 'cv2.TM_CCOEFF'
        self.screenshot = f'{combat}{picture}'
        self.screen_img = cv2.imread(self.screenshot)
        self.screen_img_gray = img_grey(self.screenshot)

        self.split_area()

    def split_area(self):
        six_interval = self.screen_img_gray.shape[0]//6
        self.interval = [Interval(six_interval * (i - 1), six_interval * i) for i in range(1, 6)]

    def recognize_StartButton(self):

        start_button = img_grey(f'{combat}start_combat.png')
        recognized=recognize(self.screen_img_gray, start_button)
        if (recognized >= self.hreshold).any():
            return True
        else:
            return False

    def recognize_OrderCard(self):
        recognized_arts = recognize(self.screen_img_gray,img_grey(f'{OrderCard}/start_sign4.jpg'))
        a=np.where(recognized_arts > self.threshold)
        # marks(self.screen_img,f'{OrderCard}/start_sign4.jpg',a[0],a[1])
        arts=self.get_OrderCard_area(recognized_arts)
        # recognized_quick = recognize(self.screen_img_gray,img_grey(f'{OrderCard}/quick.jpg'))
        # quick=self.get_OrderCard_area(recognized_quick)
        # recognized_buster = recognize(self.screen_img_gray,img_grey(f'{OrderCard}/buster.jpg'))
        # buster=self.get_OrderCard_area(recognized_buster)

        all_cards = quick + arts + buster
        all_cards.sort()

        print("cards: ", all_cards)

    def get_double_damage(self):
        start_button = cv2.cvtColor(cv2.imread(f'{OrderCard}/restraint.png'), cv2.COLOR_BGR2GRAY)
        recognized=recognize(self.screen_img_gray, start_button)
        if judge(recognized,self.threshold):
            return True
        else:
            return False


    def get_half_damage(self):  # get the coordinates of the resistance mark
        threshold = 0.85
        resistance = find_area(f'{OrderCard}/resistance.png', threshold)
        return resistance

    #不知道什么东西
    def get_OrderCard_area(self, recognized):
        area = []
        resistance_x = np.where(recognized>self.threshold)[1]
        for x in resistance_x:
            for index,interval in enumerate(self.interval):
                if x in interval:
                    area.append(interval)
                    break
        return area

    def get_card_area(self, template, threshold):
        template_img = cv2.cvtColor(cv2.imread(template), cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(self.screen_img_gray, template_img, cv2.TM_CCOEFF_NORMED)

        loc = np.where(res >= threshold)
        OrderCard_x = np.mean(loc[0]).astype(np.int)
        OrderCard_y = loc[1]
        # mark(template, OrderCard_x, OrderCard_y)
        ary = {OrderCard_x: OrderCard_y}
        ary = [(i, list(ary.keys())[0]) for i in list(ary.values())[0]]
        for i in range(len(ary)):
            for p in range(1, len(ary) - i):
                for k in range(-5, 5):
                    for l in range(-5, 5):
                        if ((ary[i][0] + k) == ary[i + p][0]) and ((ary[i][1] + l) == ary[i + p][1]):
                            ary[i + p] = [0, 0]
        while ary.count([0, 0]) >= 1:
            ary.remove([0, 0])
        return ary

    def recognize_follower(self):
        for i in range(1, 6):
            img = cv2.imread(f'tmp/follow{i}.jpg')

    def get_follower(self):
        for i in range(1, 6):
            img = self.screen_img_gray[826:826 + 382 // 2,
                  105 + (300 + 213) * (i - 1):105 + (300 + 213) * (i - 1) + 300]
            cv2.imshow('1', img)
            cv2.imwrite(f'tmp/follow{i}.jpg', img)


if __name__ == '__main__':
    combat_analysis = CombatAnalysis('t1.jpg')
    # combat_analysis.get_follower()
    # print(combat_analysis.recognize_StartButton())
    # print(combat_analysis.get_double_damage())
    # print(combat_analysis.recognize_OrderCard())
    combat_analysis.get_card_area(f'{OrderCard}/quick.jpg',0.95)