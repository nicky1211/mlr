from math import log
# import operator

def createDataSet():
    dataSet = [         ['Sunny', 'Hot',  'High',  'Weak',  'no'],
                        ['Sunny', 'Hot',  'High',  'Strong',  'no'],
                        ['Overcast', 'Hot',  'High',  'Weak',  'yes'],
                        ['Rain', 'Mild',  'High',  'Weak',  'yes'],
                        ['Rain', 'Cool',  'Normal',  'Weak',  'yes'],
                        ['Rain', 'Cool',  'Normal',  'Strong',  'no'],
                        ['Overcast', 'Cool',  'Normal',  'Strong',  'yes'],
                        ['Sunny', 'Mild',  'High',  'Weak',  'no'],
                        ['Sunny', 'Cool',  'Normal',  'Weak',  'yes'],
                        ['Rain', 'Mild',  'Normal',  'Weak',  'yes'],
                        ['Sunny', 'Mild',  'Normal',  'Strong',  'yes'],
                        ['Overcast', 'Mild',  'High',  'Strong',  'yes'],
                        ['Overcast', 'Hot',  'Normal',  'Weak',  'yes'],
                        ['Rain', 'Mild',  'High',  'Strong',  'no']]

    labels = ['OutLook', 'Temp', 'Humidity', 'Wind']
    return dataSet, labels

def calcEntropy(dataSet):
    numEntries = len(dataSet)
    # print numEntries
    labelCounts = {}
    for featList in dataSet:  
    	# print featList
        currentLabel = featList[-1]
        if currentLabel not in labelCounts.keys():labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
        # print labelCounts
    entropy = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        entropy -= prob * log(prob, 2)  # log base 2
    return entropy


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featList in dataSet:
        if featList[axis] == value:
            reducedFeatList = featList[:axis]  
            reducedFeatList.extend(featList[axis + 1:])
            retDataSet.append(reducedFeatList)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1  
    baseEntropy = calcEntropy(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures): 
        featList = [example[i] for example in dataSet]  
        # print featList
        uniqueVals = set(featList) 
        # print uniqueVals
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcEntropy(subDataSet)


        infoGain = baseEntropy - newEntropy  

        # print("feature : " + str(i))
        # print("baseEntropy : "+str(baseEntropy))
        # print("newEntropy : " + str(newEntropy))
        # print("infoGain : " + str(infoGain))

        if (infoGain > bestInfoGain):  
            bestInfoGain = infoGain 
            bestFeature = i
    return bestFeature  


def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]

    if classList.count(classList[0]) == len(classList):
        # stop splitting when all of the classes are equal
        return classList[0]  

    # use Information Gain
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]

    myTree = {bestFeatLabel: {}}
    # print("myTree : "+labels[bestFeat])
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    # print("featValues: "+str(featValues))
    uniqueVals = set(featValues)
    # print("uniqueVals: " + str(uniqueVals))
    for value in uniqueVals:
        subLabels = labels[:]  
        # print("subLabels"+str(subLabels))
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
        # print("myTree : " + str(myTree))
    return myTree


myDat, labels = createDataSet()
mytree = createTree(myDat, labels)
print(mytree)
