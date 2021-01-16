from spike_detector import main as spikeDetector
import pickle
import math

from wordsUtils import posibleWords,getWords
from posibilitiesUtils import getPosibilitiesRS,getPosibilities
    
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
      



