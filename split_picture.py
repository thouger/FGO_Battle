from PIL import Image
im = Image.open(r"out.png")# 图片的宽度和高度
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
        region.save(f"five_image/{i}.png")

