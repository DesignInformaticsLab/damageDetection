import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from PIL import Image

im = Image.open('image.gif')
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((1, 1))
