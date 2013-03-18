#!/usr/bin/python
import numpy as np


def loadAbaloneData (pathToData = '../data', fileName = 'abalone-training.data', \
                verbose = False):
    """
    Loads data from the data folder
    """
#    fileHandle = open(pathToData + '/' + fileName)
    if verbose: print "Loading "+str(fileName)+"..."
    from path import path
    pathToData = path(pathToData) 
    openFile = path(pathToData + '/' + fileName)
    listOfLines = openFile.lines(retain=False)
    numData = len(listOfLines)-1 #because first line is labels
    dataHeader = listOfLines[0].split(',')
    for i, item in enumerate(dataHeader):
        if item[0]=='"': dataHeader[i] = item[1:-1]
        
    data = np.zeros((numData, len(dataHeader)))
    
    for i in range(numData):
        temp= np.array(map(str, listOfLines[i+1].split(',') ))
        for j, item in enumerate(temp):
            if item[0]=='"': temp[j] = item[1:-1]
        # for attribute sex
        if temp[0] == 'M': temp[0] =1  #Male
        elif temp[0] == 'F': temp[0] = 2 #Female
        elif temp[0] == 'I': temp[0] = 3 #Infant
        #For data labels
        if temp[-1] == 'TRUE': temp[-1] =1
        elif temp[-1] == 'FALSE':temp[-1] = 0
        
        data[i,:] = temp

    return dataHeader, data

def loadBankData (pathToData = '../data', fileName = 'bank-training.data', \
                verbose = False):
    """
    Loads data from the data folder
    """
#    fileHandle = open(pathToData + '/' + fileName)
    print "Loading "+str(fileName)+"..."
    from path import path
    pathToData = path(pathToData) 
    openFile = path(pathToData + '/' + fileName)
    listOfLines = openFile.lines(retain=False)
    numData = len(listOfLines)-1 #because first line is labels
    dataHeader = listOfLines[0].split(',')
    numHeader = len(dataHeader)
    for i, item in enumerate(dataHeader):
        if item[0]=='"': dataHeader[i] = item[1:-1]
        
    data = np.zeros((numData, numHeader))
    dataTemp = np.zeros((numData, numHeader), dtype = '|S16')
    
    for i in range(numData):
        temp= np.array(map(str, listOfLines[i+1].split(',') ))
        for j, item in enumerate(temp):
            if item[0]=='"': temp[j] = item[1:-1]
        dataTemp[i,:] = temp
    
    #define which values are numerical and which are not
    dataHeaderValues = [0,1,1,1,1,0,1,1,1,0,1,0,0,0,0,1,1]

#    attrList = np.array((numHeader,))
    attrList = [[] for x in dataHeader]
    for j in range (numHeader):
        attrList[j] = list(set(dataTemp[:,j]))
        if verbose:
            if dataHeaderValues[j] == 1: print str(attrList[j])
    for i in range(numData):
        for j in range(numHeader):
            if dataHeaderValues[j] == 1:
                data[i,j] = attrList[j].index(dataTemp[i,j])
            else:
                data[i,j] = dataTemp[i,j] 

    return dataHeader, data


