import cv2
img=cv2.imread('../test/img2.png')
img2=cv2.resize(img,cv2.imread('../test/img1.png',0).shape[::-1])
cv2.imwrite('../test/img3.png',img2)