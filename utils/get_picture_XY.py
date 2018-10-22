import matplotlib.pyplot as plt
from PIL import Image
from utils.config import *
x=[]
y=[]
def on_press(event):
    x.append(event.xdata)
    y.append(event.ydata)
    print("my position:" ,event.button,event.xdata, event.ydata)
def get_picture_XY(f):
    fig = plt.figure()
    img = Image.open(f)
    plt.imshow(img, animated= True)
    fig.canvas.mpl_connect('button_press_event', on_press)
    plt.show()

if __name__ == '__main__':
    # get_picture_XY(f'../{combat}/t1.jpg')
    get_picture_XY(f'../{combat}/t.jpg')
    # get_picture_XY(f'../{home}start.jpg')
    # get_picture_XY('../out.png')
    print()