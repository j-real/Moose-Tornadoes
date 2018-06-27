import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from matplotlib import style
style.use("ggplot")

x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]

plot.scatter(x,y)
plt.show()

# convert to numpy array
# list of features and then label

# first make the list
# inside, corresponding values of x and y
X = np.array([[1,2],
            [5,8],
            [1.5,1.8],
            [8,8],
            [1,0.6],
            [9,11]])

# lable the pairs? idk how he got these numbers. 5:16 in video
y = [0,1,0,1,0,1]

# create classifier
clf = svm.SVC(kernal='linear', C-1.0)

# fit features to their labels
clf.fit(X,y)

print(clf.predict([0.58,0.76]))