# from combat_analysis import CombatAnalysis
# from config import *
# picture = 't5.jpg'
# card = CombatAnalysis(picture)
#
# # resistance = card.get_double_damage()
# # card.recognize_damage_multiplier([i[0] for i in resistance])
# card.get_card_area(f'{order_card}/buster.png',0.95)
# # card.recognize_OrderCard()
# print()
import cv2
import numpy as np
img1=cv2.imread('test/quick2.png',0)
img2 = cv2.imread('test/quick2.png',0)
res = cv2.matchTemplate(img1,img2, cv2.TM_CCOEFF_NORMED)
print()