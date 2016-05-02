import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from PIL import Image

address = './pipe_as_gif/'
damage_type = ['dent','slit','impi','squiz','nd']
label = [1,2,3,4,5]
damage_sample_size = 100
H = 640
W = 480
L = 200

X = np.empty((0, H*W))
y = np.empty((0))
for tid, t in enumerate(damage_type):
    for i in range(1,damage_sample_size+1):
        file = address + t + str(i) + '.gif'
        im = Image.open(file).convert('L')
        im = np.asarray(im.getdata(), dtype=np.uint8).reshape((im.size[1],im.size[0]))
        w=Image.fromarray(im,mode='L')
        plt.imshow(w)

        plt.show()
        # for l in range(L):
        #     X = X.concat(im)
        #     y = y.concat(label[tid]*np.ones(L))


