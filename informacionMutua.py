from spike_detector import main as spikeDetector
import pickle
import math
from matplotlib import pyplot as plt

from wordsUtils import posibleWords,getWords
from posibilitiesUtils import getPosibilitiesRS,getPosibilities
from transformToBinary import transformToBinary
    
def mutualInformation(ritmA,ritmB,wordLength):
    r = getWords(ritmA,wordLength)
    s = getWords(ritmB,wordLength)
    words = posibleWords(wordLength)
    posibleR = getPosibilities(r,words)
    posibleS = getPosibilities(s,words)
    posibleRS = getPosibilitiesRS(r,s,words)
   
    result = 0
    
    for i in range(0,len(words)):
        py = posibleS[i]
        for j in range(0,len(words)):
            if posibleRS[i,j] > 0 and posibleR[j] > 0 and posibleS[i] >0:
                px = posibleR[j]
                pxy = posibleRS[i,j]
                I = math.log2(pxy / (px * py))
                result += pxy * I
    return result
    
    

def main():
    spikeDetector()
    vd_directory = "./vdTrozoR_matrix.pickle"
    lp_directory = "./lpTrozoR_matrix.pickle"
    vd = pickle.load(open(vd_directory, "rb"))
    lp = pickle.load(open(lp_directory, "rb"))
    
    wordsLength = range(1,8)
    dT = range(1,100,10)
    
    matrix = []
    for i in range(0,len(wordsLength)):
        for j in range(0,len(dT)):
            rA = transformToBinary(vd,dT[j])
            rB = transformToBinary(lp,dT[j])
            matrix.append(mutualInformation(rA,rB,wordsLength[i]))
        plt.plot(dT,matrix)
        plt.title("Informacion Mutua palabras de "+str(wordsLength[i])+" bit")    
        plt.ylabel('IM')    
        plt.xlabel('dT')    
        plt.show()    
        matrix = []
      

if __name__ == "__main__":
    main()

