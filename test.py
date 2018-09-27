from card import get_restraint, recognize_area

sh = '2160x1080_CardFace/t2.jpeg'
resistance = get_restraint(sh)
recognize_area(sh,[i[0] for i in resistance])
print()