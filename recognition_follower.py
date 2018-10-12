from itertools import combinations
from PIL import Image
import cv2

from compare_image.compare3 import compare3
from compare_image.compare1 import image_similarity1
from compare_image.compare2 import compare_images

img = '2560x1440_combat/t1.jpg'
im = Image.open(img)# 图片的宽度和高度
img_size = im.size
print("图片宽度和高度分别是{}".format(img_size))
xx = 5
yy = 1
x = img_size[0] // xx
y = img_size[1] // yy
for j in range(yy):
    for i in range(xx):
        left = i*x
        up = y*j
        right = left + x
        low = up + y
        region = im.crop((left,up,right,low))
        print((left,up,right,low))
        temp = str(i)+str(j)
        region.save(f"five_image/{i}.jpg")
for i in range(5):
    print(i)
    img1= cv2.imread(f"five_image/{i}.jpg")
    y,x,z = img1.shape
    img1 = img1[y//2+110:y-400,0+105:x-40]
    # original =  cv2.cvtColor(img1 , cv2.COLOR_BGR2GRAY)
    # img2= cv2.imread(f"five_image/{i+1}.png",0)
    # img2 = img2[y//2-10:y-70,0+80:x-350]
    # shopped = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # compare_images(original, shopped, "Original vs. Photoshopped")
    # compare_images(img1, img2, "Original vs. Photoshopped")
    cv2.imwrite(f"five_image/{i}.jpg",img1)

for i in combinations(range(5), 2):
    print(i)
    # similarity_bands_via_numpy, similarity_histogram_via_pil, similarity_vectors_via_numpy, similarity_greyscale_hash_code = \
    #     image_similarity1(f'five_image/{i[0]}.jpg', f'five_image/{i[1]}.jpg')


    # compare_images(cv2.cvtColor(cv2.imread(f"five_image/{i[0]}.jpg"), cv2.COLOR_BGR2GRAY), cv2.cvtColor(cv2.imread(f"five_image/{i[1]}.jpg"), cv2.COLOR_BGR2GRAY), "Original vs. Photoshopped")

    i1 = Image.open(f'five_image/{i[0]}.jpg')
    i2 = Image.open(f'five_image/{i[1]}.jpg')
    compare3(i1,i2)
    print()