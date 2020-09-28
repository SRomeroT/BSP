# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 19:39:31 2020

@author: I_Jara
"""

# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplost as plt
import pickle

f = open('/DatosSinapsisArtificial/TrozoC.txt','r')

interval = 0
channels = 0
samples = 0

vd = []
lp = []

for i,line in enumerate(f.readlines):
    if i == 0 :
        interval = line.split(" ")[-1]
    elif i == 1 :
        channel = line.split(" ")[-1]
    elif i == 2 :
        samples = line.split(" ")[-1]
    else:
        vd.append(line.split("\t")[0])
        lp.append(line.split("\t")[1])




