# coding=gbk
from interval import Interval

from utils.compare_image import compare_images
from utils.config import *
import numpy as np
import cv2

# TODO 识别开始按钮
from utils.positioning import mark


class CombatAnalysis:
    first_kill = ()

    def __init__(self, picture):

        self.screenshot = f'{combat}{picture}'
        self.screen_img = cv2.imread(self.screenshot)
        self.screen_img_gray = cv2.cvtColor(cv2.imread(self.screenshot), cv2.COLOR_BGR2GRAY)
        self.split_area()

    def recognize_StartButton(self):
        threshold = 0.85
        resistance = self.get_card_area(f'{combat}start_combat.png', threshold)
        return resistance

    def split_area(self):
        width = self.screen_img.shape
        self.interval = [Interval(width * (i - 1), width * i) for i in range(1, 6)]

    def get_current_OrderCard(self):
        current_OrderCard = {}
        fgo_OrderCard = ['arts', 'buster', 'quick']
        for i in range(5):
            unkown_OrderCard = self.screen_img[1145:1185, 210 + 511 * i:387 + 511 * i]
            for OrderCard_name in fgo_OrderCard:
                err, SSIM = compare_images(unkown_OrderCard, cv2.imread(f'{OrderCard}{OrderCard_name}.jpg', 0))
                if SSIM > 0.9:
                    current_OrderCard[i] = OrderCard_name
                    break
        return current_OrderCard

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
        width = self.screen_img.shape[1]
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
    combat_analysis = CombatAnalysis('t.jpg')
    # combat_analysis.get_follower()
    print(combat_analysis.recognize_StartButton())
