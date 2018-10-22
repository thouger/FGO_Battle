from PIL import Image

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
import cv2
from matplotlib import pyplot as plt
def find_area(img,sign,method):
    img = cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2GRAY)
    sign = cv2.cvtColor(cv2.imread(sign), cv2.COLOR_BGR2GRAY)
    # img = cv2.imread(img,0)
    # sign = cv2.imread(sign,0)
    w, h = sign.shape[::-1]
    res = cv2.matchTemplate(img, sign, eval(method))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        left_top = min_loc
    else:
        left_top = max_loc
    right_bottom = (left_top[0] + w, left_top[1] + h)
    return left_top,right_bottom

def mark(img, template, args):
    img = cv2.imread(img)
    img2 = img.copy()
    template = cv2.imread(template)
    cv2.rectangle(img2, args[0],args[1], 255, 2)

    plt.subplot(221), plt.imshow(img, cmap="gray")
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(template, cmap="gray")
    plt.title('template Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(212), plt.imshow(img2, cmap="gray")
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.show()

def marks(img,template, OrderCard_x, OrderCard_y_list):
    w, h = template.shape[::-1]
    for OrderCard_y in OrderCard_y_list:
        bottom_right = (OrderCard_y + w, OrderCard_x + h)
        cv2.rectangle(img, (OrderCard_y, OrderCard_x), bottom_right, 255, 2)
    plt.subplot(111)
    plt.imshow(img, cmap="gray")
    plt.show()

def mark_point(img,point):
    # plt.imshow(cv2.imread(img))
    plt.imshow(Image.open(img))
    plt.annotate(f'{point[0], point[1]}', xy=point, xycoords='data',
                 xytext=(0.5, 0.5), textcoords='figure fraction',
                 arrowprops=dict(arrowstyle="->"))
    plt.show()
recognize = lambda img,template:cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
