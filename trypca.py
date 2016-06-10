import numpy as np
from sklearn.decomposition import PCA
from sklearn.cross_validation import train_test_split

# create X1 data and label
X1 = np.loadtxt("slit.txt")
pca = PCA(n_components=1000)
pca.fit(X1)
a = np.size(X1)
X1_label = np.empty(a, 1)
for i in X1_label:
    X1_label[i] = 0

# create X2 data and label
X2 = np.loadtxt("impingement.txt")
pca = PCA(n_components=1000)
pca.fit(X2)
b = np.size(X2)
X2_label = np.empty(b, 1)
for i in X2_label:
    X2_label[i] = 1

# train and test (not finished)
