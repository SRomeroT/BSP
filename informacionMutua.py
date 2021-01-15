from spike_detector import main as spikeDetector
import functools 
import numpy as np
import pickle



def posibleWords(lengthWord):
    posibleWords = 2**lengthWord
    numbers = range(0, posibleWords)
    binary = np.vectorize(np.binary_repr)
    return binary(numbers,width=lengthWord)
    
    
def main():
    spikeDetector()
    vd_directory = "./vdTrozoR_matrix.pickle"
    lp_directory = "./lpTrozoR_matrix.pickle"
    vd = pickle.load(open(vd_directory, "rb"))
    lp = pickle.load(open(lp_directory, "rb"))
    
def getWords(data,lengthWord):
     matrixWords =[]
     l = len(data)
     firstElement = 0
     for i in range(0,l):
         if i >= lengthWord -1:
             element = map(str, data[firstElement:i+1])
             matrixWords.append(functools.reduce(lambda a,b : a+b,element))
             if lengthWord ==1:
                 firstElement = i+1
             else:
                 firstElement=i
     return matrixWords
 
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
        
