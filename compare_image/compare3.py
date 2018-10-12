from PIL import Image


def compare3(i1,i2):
    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1 - p2) for p1, p2 in pairs)
    else:
        dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

    ncomponents = i1.size[0] * i1.size[1] * 3
    print("Difference (percentage):", (dif / 255.0 * 100) / ncomponents)

if __name__ == '__main__':
    i1 = Image.open("test/img1.png")
    i2 = Image.open("test/img3.png")