# combine some common used function from cv2
from matplotlib import pyplot as plt
import cv2
import numpy as np


def location(sh, tmp, thd):
    img = cv2.imread(sh, 0)
    template = cv2.imread(tmp, 0)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = thd

    loc = np.where(res >= threshold)
    #刚好三个点就不用这个了
    OrderCard_x = np.mean(loc[0]).astype(np.int)
    OrderCard_y = loc[1]
    # mark(img,template,OrderCard_x,OrderCard_y)
    return {OrderCard_x:OrderCard_y}


def check(sh, tmp, thd):
    img = cv2.imread(sh, 0)
    template = cv2.imread(tmp, 0)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = thd

    if (res >= threshold).any():
        return 1


def mark(img, template, OrderCard_x, OrderCard_y_list):
    w, h = template.shape[::-1]
    for OrderCard_y in OrderCard_y_list:
        bottom_right = (OrderCard_y+ w, OrderCard_x + h)
        cv2.rectangle(img, (OrderCard_y,OrderCard_x), bottom_right, 255, 2)
    plt.subplot(111), plt.imshow(img, cmap="gray")
    plt.show()