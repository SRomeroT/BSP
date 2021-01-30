import numpy as np
import functools 

def posibleWords(lengthWord):
    posibleWords = 2**lengthWord
    numbers = range(0, posibleWords)
    binary = np.vectorize(np.binary_repr)
    return binary(numbers,width=lengthWord)

def getWords(data,lengthWord):
     matrixWords =[]
     l = len(data)
     firstElement = 0
     for i in range(l):
         if i >= lengthWord -1:
             element = map(str, data[firstElement:i+1])
             matrixWords.append(functools.reduce(lambda a,b : a+b,element))
             if lengthWord ==1:
                 firstElement = i+1
             else:
                 firstElement+=1
     return matrixWords   