import cv2


def main():
    # img = cv2.imread("out.png")
    img = cv2.imread("five_image/1.jpg")
    # cv2.imshow('Input Image', img)
    # cv2.waitKey(0)

    # 检测
    # akaze = cv2.AKAZE_create()
    # akaze = cv2.BRISK_create()
    akaze = cv2.FastFeatureDetector_create()
    # akaze = cv2.KAZE_create()
    # akaze = cv2.ORB_create()
    keypoints = akaze.detect(img, None)

    # 显示
    # 必须要先初始化img2
    img2 = img.copy()
    img2 = cv2.drawKeypoints(img, keypoints, img2, color=(0, 255, 0))
    cv2.imshow('Detected AKAZE keypoints', img2)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
