methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
import cv2
from matplotlib import pyplot as plt
def find_area(img,sign,method):
    w, h = sign.shape[::-1]
    res = cv2.matchTemplate(img, sign, eval(method))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        left_top = min_loc
    else:
        left_top = max_loc
    right_bottom = (left_top[0] + w, left_top[1] + h)
    return left_top,right_bottom

def mark(img,sign,top_left,bottom_right,):
    img2 = img.copy()
    cv2.rectangle(img2, top_left, bottom_right, 255, 2)

    plt.subplot(221), plt.imshow(img, cmap="gray")
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(sign, cmap="gray")
    plt.title('template Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(212), plt.imshow(img2, cmap="gray")
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.show()