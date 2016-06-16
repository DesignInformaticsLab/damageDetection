import numpy as np
from sklearn.decomposition import PCA
from sklearn.cross_validation import train_test_split

damage = np.loadtxt('damage.txt')  # size (500,307200)

print(np.shape(damage))

pca = PCA(n_components=500)  # it seems that the maximum number of components is 500
damage_new = pca.fit_transform(damage, y=None) # damage_new is (500,500)

Y = np.empty(500, 1)

for i in range(100):
    Y[i] = 0
    Y[i + 100] = 1
    Y[i + 200] = 2
    Y[i + 300] = 3
    Y[i + 400] = 4

X_train, X_test, y_train, y_test = train_test_split(damage_new,Y, test_size=0.25, random_state=42)
