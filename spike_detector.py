import numpy as np
import matplotlib.pyplot as plt
import math
import locale
import pickle


def detect_spike(dic, threshold, v):
    spike = 0
    if dic["lv2"] <= dic["lv1"] and dic["lv1"] >= v and dic["lv1"] > threshold:
        spike = 1
    dic["lv2"] = dic["lv1"]
    dic["lv1"] = v
    return spike


def main():

    # locale.setlocale(locale.LC_ALL, 'es_ES')
    dic = {}
    dic["lv1"] = 0.0
    dic["lv2"] = 0.0
    threshold = 0.3
    sample_freq = 0.1
    total_spike = 0
    vd = pickle.load( open( "vdTrozoC.pickle", "rb" ) )
    lp = pickle.load( open( "lpTrozoC.pickle", "rb" ) )

    for elem in vd:
        sp = detect_spike(dic,threshold, float(elem.replace(",",".")))
        total_spike += sp


    print("total spikes: "+str(total_spike))





if __name__ == "__main__":
    main()
