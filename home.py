#coding:utf-8
import os
import time

import cv2
# import pytesseract

from utils.config import *
from utils.compare_image import compare_images
from utils.positioning import find_area, mark

# TODO pytesseract的安装
# TODO 点击关闭按钮
# TODO 以后屏幕截图存放在tmp文件夹内
#TODO 进入界面后点击的过程
class Home:

    AP_pic = f'{home}/AP.jpg'
    start_img = cv2.imread(f'{home}/start.jpg', 0)
    StartSign_img = cv2.imread(f'{home}/StartSign.jpg', 0)

    def __init__(self, picture):

        self.screenshot = f'{home}/{picture}'
        self.screeen_img = cv2.imread(self.screenshot, 0)

    def find_everyday_entrance(self):
        everyday_pic = f'{home}/{everyday_entrance}'
        everyday_img = cv2.imread(everyday_pic,0)
        top_left, bottom_right=find_area(self.screeen_img,everyday_img,'cv2.TM_CCOEFF_NORMED')
        mark(self.screeen_img,everyday_img,top_left,bottom_right)

    def find_AP(self):
        AP_img = self.screeen_img[1329:1367,435:508]
        cv2.imwrite(self.AP_pic,AP_img)


    def find_StartSign(self):
        StartSign_img = self.start_img[24:120,1100:1455]
        cv2.imwrite(f'tmp/StartSign.jpg',StartSign_img)
        MSE,SSIM = compare_images(StartSign_img,self.StartSign_img)
        if SSIM>0.95:
            return True
        else:
            return False

    def recognize_AP(self):
        while not os.path.exists(self.AP_pic):
            time.sleep(0.5)
        else:
            AP = pytesseract.image_to_string(self.AP_pic, config='--psm 6')
        return AP

    def close_start(self):
        close_start_area = 2482,46

if __name__ == '__main__':
    home = Home(f'{home}main.jpg')
    print(home.find_StartSign())