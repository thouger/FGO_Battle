import cv2
from config import *
from positioning import find_area, mark


class Home:
    def __init__(self, picture):

        self.screenshot = f'{home}/{picture}'
        self.screeen_img = cv2.imread(self.screenshot, 0)


    def find_everyday_entrance(self):
        everyday_pic = f'{home}/{everyday_entrance}'
        everyday_img = cv2.imread(everyday_pic,0)
        top_left, bottom_right=find_area(self.screeen_img,everyday_img,'cv2.TM_CCOEFF_NORMED')
        mark(self.screeen_img,everyday_img,top_left,bottom_right)