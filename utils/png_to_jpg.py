from PIL import Image
from utils.config import *
im = Image.open(f"../{combat}start_combat.png")
rgb_im = im.convert('RGB')
rgb_im.save(f"../{combat}start_combat.jpg")