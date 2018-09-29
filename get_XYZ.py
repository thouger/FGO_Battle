import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from PIL import Image
def on_press(event):
    print("my position:" ,event.button,event.xdata, event.ydata)

fig = plt.figure()
img = Image.open('test/t1.jpeg')
#updata = True

plt.imshow(img, animated= True)

fig.canvas.mpl_connect('button_press_event', on_press)
plt.show()
