#!/usr/bin/python
import numpy as np
import pylab as pl
from matplotlib.colors import ListedColormap
from sklearn.svm import SVC
from sklearn.svm import NuSVC
from sklearn.cross_validation import StratifiedKFold
from sklearn.grid_search import GridSearchCV
from sklearn.preprocessing import StandardScaler
from getData import loadBankData


dataHeader, dataTrain = loadBankData(fileName = 'bank-training.data')
dataHeaderTest, dataTest = loadBankData(fileName = 'bank-test.data')
X_train = StandardScaler().fit_transform(dataTrain[:,:-1])
y_train = dataTrain[:,-1]
X_test = StandardScaler().fit_transform(dataTest[:,:-1])
y_test = dataTest[:,-1]


names = ["Linear SVM", "Gaussian SVM", "Sigmoid SVM", "Poly2 SVM", "Poly3 SVM", \
"Error Tolerant SVM"]
classifiers = [\
    SVC(kernel='linear', C= 1),\
    SVC(kernel='rbf', gamma=2, C=1),\
    SVC(kernel='sigmoid', gamma=2, C=1),\
    SVC(kernel='poly', degree =2, C =1 ),\
    SVC(kernel='poly', degree =3, C =1),\
    NuSVC(gamma=2, nu =0.1)]
    # parameter nu denotes a lower bound of the fraction of support vectors


print "Classification Score for Bank Data:"
# iterate over classifiers
for name, clf in zip(names, classifiers):
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    print "Using "+str(name)+":"+str(score)
    

