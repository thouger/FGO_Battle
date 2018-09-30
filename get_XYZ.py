import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from PIL import Image
from config import *
def on_press(event):
    print("my position:" ,event.button,event.xdata, event.ydata)

fig = plt.figure()
img = Image.open(f'{combat}/t1.jpg')
plt.imshow(img, animated= True)
fig.canvas.mpl_connect('button_press_event', on_press)
plt.show()
