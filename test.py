# from combat_analysis import CombatAnalysis
from config import *
# import cv2
# import numpy as np
from PIL import ImageGrab
# picture = 't5.jpg'
# card = CombatAnalysis(picture)
#
# # resistance = card.get_double_damage()
# # card.recognize_damage_multiplier([i[0] for i in resistance])
# card.get_card_area(f'{order_card}/buster.png',0.95)
# # card.recognize_OrderCard()
# print()

# img1=cv2.imread('test/quick2.png',0)
# img2 = cv2.imread('test/quick2.png',0)
# res = cv2.matchTemplate(img1,img2, cv2.TM_CCOEFF_NORMED)
# print()
# im =ImageGrab.grab()
# im.show()
# from home import Home
#
# home=Home('main.jpg')
# home.find_everyday_entrance()

import pytesseract
from PIL import Image

image = Image.open('2560x1440_home/AP.jpg')
code = pytesseract.image_to_string(image)
print(code)