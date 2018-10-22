from itertools import combinations

from compare_image.compare1 import image_similarity1

if __name__ == '__main__':
    for i in combinations(range(1,6), 2):
        print(i)
        # img1,img2=f'tmp/{i[0]}.jpg',f'tmp/{i[1]}.jpg'
        img1, img2 = f'tmp/follow{i[0]}.jpg', f'tmp/follow{i[1]}.jpg'
        # similarity_bands_via_numpy, similarity_histogram_via_pil, similarity_vectors_via_numpy, similarity_greyscale_hash_code = \
        #     image_similarity1(img1,img2)
        image_similarity1(img1, img2)

        # compare_images(cv2.cvtColor(cv2.imread(f"five_image/{i[0]}.jpg"), cv2.COLOR_BGR2GRAY), cv2.cvtColor(cv2.imread(f"five_image/{i[1]}.jpg"), cv2.COLOR_BGR2GRAY), "Original vs. Photoshopped")

        # i1 = Image.open(f'../five_image/{i[0]}.jpg')
        # i2 = Image.open(f'../five_image/{i[1]}.jpg')
        # compare3(i1,i2)
        # print()