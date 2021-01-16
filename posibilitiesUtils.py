import numpy as np

def getPosibilities(data,posibleResults):
    l = len(data)
    lP = len(posibleResults)
    posibilities = np.zeros(lP)
    for i in range(0,l):
        word = data[i]
        for j in range(0,lP):
            possibleWord = posibleResults[j]
            if word == possibleWord:
                posibilities[j]+=1
                break
    return posibilities/l

def getPosibilitiesRS(dataR,dataS,posibleResults):
    lR = len(dataR)
    l = len(dataS)
    if l>lR:
        dataS = dataS[0:lR]
        l = len(dataS)
    lP = len(posibleResults)
    posibilities = np.zeros((lP,lP))
    for i in range(0,l):
        wordS = dataS[i]
        for j in range(0,lP):
            possibleWordS = posibleResults[j]
            if wordS == possibleWordS:
                wordR = dataR[i]
                for k in range(0,lP):
                    possibleWordR = posibleResults[k]
                    if wordR == possibleWordR:
                        posibilities[j,k]+=1
                        break
                break
    return posibilities/l