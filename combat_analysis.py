# coding=gbk
from interval import Interval
from utils.config import *
import numpy as np
import cv2

from utils.image_processing import img_grey, recognize, find_area, mark_point


def judge(recognized,threshold):
    if (recognized >= threshold).any():
        return True
    else:
        return False

"""
ս����������Ҫ�����У�
1.����ͼ��5�ȷ����䣬������Ϊ��
2.ʶ��ʼս����ťλ�ò�����
3.ʶ������ָ�λ��
4.ʶ����ߵֿ������״̬
5.��ս��״̬��ͼ��ֳ�5��
"""

#todo ʶ������ָ�λ��
#todo ʶ����ߵֿ������״̬
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
        six_interval = self.screen_img_gray.shape[1]//5
        self.interval = [Interval(six_interval * (i - 1), six_interval * i) for i in range(1, 6)]

    def recognize_StartButton(self):
        _, _, center = find_area(self.screenshot, f'{combat}start_combat.png')
        # mark_point(self.screenshot, center)
        return center

    def recognize_OrderCard(self):
        recognized_arts = recognize(self.screen_img_gray,img_grey(f'{OrderCard}/arts.jpg'))
        # marks(self.screen_img,f'{OrderCard}/start_sign4.jpg',a[0],a[1])
        arts=self.get_OrderCard_area(recognized_arts)
        recognized_quick = recognize(self.screen_img_gray,img_grey(f'{OrderCard}/quick.jpg'))
        quick=self.get_OrderCard_area(recognized_quick)
        recognized_buster = recognize(self.screen_img_gray,img_grey(f'{OrderCard}/buster.jpg'))
        buster=self.get_OrderCard_area(recognized_buster)

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

    def get_OrderCard_area(self, recognized):
        area = set()
        resistance_x = np.where(recognized>self.threshold)[1]
        for x in resistance_x:
            for index,interval in enumerate(self.interval):
                if x in interval:
                    area.add(index)
                    break
        return area

    def recognize_follower(self):
        for i in range(1, 6):
            img = cv2.imread(f'tmp/follow{i}.jpg')

if __name__ == '__main__':
    combat_analysis = CombatAnalysis('t0.jpg')
    # combat_analysis.get_follower()
    # print(combat_analysis.recognize_StartButton())
    # print(combat_analysis.get_double_damage())
    # print(combat_analysis.recognize_OrderCard())
    combat_analysis.recognize_StartButton()