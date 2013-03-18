#!/usr/bin/python
import numpy as np
import pylab as pl
from matplotlib.colors import ListedColormap
from sklearn.svm import SVC
from sklearn.cross_validation import StratifiedKFold
from sklearn.grid_search import GridSearchCV
#from sklearn.preprocessing import StandardScaler
from getData import loadAbaloneData


dataHeader, dataTrain = loadAbaloneData(fileName = 'abalone-training.data')
dataHeaderTest, dataTest = loadAbaloneData(fileName = 'abalone-test.data')
X_train = dataTrain[:,:-1]
y_train = dataTrain[:,-1]
X_test = dataTest[:,:-1]
y_test = dataTest[:,-1]


names = ["Linear SVM", "Gaussian SVM","Sigmoid SVM", "Poly2 SVM", "Poly3 SVM"]
classifiers = [\
    SVC(kernel='linear', C= 0.025),\
    SVC(kernel='rbf', gamma=2, C=1),\
    SVC(kernel='sigmoid', degree = 5, C=0.025),\
    SVC(kernel='poly', degree =2, C =0.025 ),\
    SVC(kernel='poly', degree =3, C =1)]

print "Classification Score for Abalone Data:"
# iterate over classifiers
for name, clf in zip(names, classifiers):
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    print "Using "+str(name)+":"+str(score)

"""
#Calculate best params for RBF and Poly Kernels  using Grid Search
skf = StratifiedKFold(y_train, n_folds=10)
#svr = SVC(kernel = 'rbf')
#cRange = np.arange(-10, 10)
#gammaRange = 10**np.arange(-5,5)
#parameters = dict(C=cRange, gamma=gammaRange)
param_grid = {'C':np.arange(-10, 10), 'gamma': 10**np.arange(-5,5)}
clfGrid = GridSearchCV(SVC(), param_grid=param_grid, verbose =1)
clfGrid.fit(X_train, y_train, cv = 10)
print("The best classifier is: ", clfGrid.best_estimator_)
"""

