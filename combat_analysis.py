from interval import Interval

from config import *
import numpy as np
import pandas as pd
import cv2
from matplotlib import pyplot as plt

class CombatAnalysis:
    def __init__(self, picture):

        self.screenshot = f'{card_face}/{picture}'
        self.screeen_img = cv2.imread(self.screenshot, 0)

        self.split_area()

    def split_area(self):
        width = self.screeen_img.shape
        self.interval = [Interval(width * (i - 1), width * i) for i in range(1, 6)]

    def get_card_area(self, sign_pic, threshold):  # get the coordinates of cards/marks
        sign_img = cv2.imread(sign_pic, 0)

        res = cv2.matchTemplate(self.screeen_img, sign_img, cv2.TM_CCOEFF_NORMED)

        loc = np.where(res >= threshold)
        OrderCard_x = np.mean(loc[0]).astype(np.int)
        OrderCard_y = loc[1]
        self.mark(sign_img,OrderCard_x,OrderCard_y)
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

    # This part is used to set the status of the cards
    def get_double_damage(self, ):  # get the coordinates of the restraint mark
        threshold = 0.85
        restraint = self.get_card_area(f'{order_card}/restraint.png', threshold)
        return restraint

    def get_half_damage(self):  # get the coordinates of the resistance mark
        threshold = 0.85
        resistance = self.get_card_area(f'{order_card}/resistance.png', threshold)
        return resistance

    def recognize_damage_multiplier(self, resistance_x):
        area = []
        width = self.screeen_img.shape[1]
        for x in resistance_x:
            for i in self.interval:
                if x in i:
                    area.append(i)
                    break
        return area

    def recognize_OrderCard(self):
        threshold = 0.98
        quick = self.get_card_area(f'{order_card}/quick.png', threshold)
        arts = self.get_card_area(f'{order_card}/arts.png', threshold)
        buster = self.get_card_area(f'{order_card}/buster.png', threshold)

        all_cards = quick + arts + buster
        all_cards.sort()

        print("cards: ", all_cards)

    def mark(self, template, OrderCard_x, OrderCard_y_list):
        w, h = template.shape[::-1]
        for OrderCard_y in OrderCard_y_list:
            bottom_right = (OrderCard_y + w, OrderCard_x + h)
            cv2.rectangle(self.screeen_img, (OrderCard_y, OrderCard_x), bottom_right, 255, 2)
        plt.subplot(111)
        plt.imshow(self.screeen_img, cmap="gray")
        plt.show()