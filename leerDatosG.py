# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 19:39:31 2020

@author: I_Jara
"""

# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import pickle
import os

print(os.getcwd())

f = open('DatosSinapsisArtificial/TrozoG.txt','r')

interval = 0
channels = 0
samples = 0

vd = []
lp = []
tyd = []

for i,line in enumerate(f.readlines()):
	print("Line: ", i)
	if i == 0 :
		interval = line.split(" ")[-1]
	elif i == 1 :
		channel = line.split(" ")[-1]
	elif i == 2 :
		samples = line.split(" ")[-1]
	else:
		lp.append(line.split("\t")[0])
		vd.append(line.split("\t")[1])
		tyd.append(line.split("\t")[2])

with open('vdTrozoG.pickle', 'wb') as handle:
	pickle.dump(vd, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('lpTrozoG.pickle', 'wb') as handle:
	pickle.dump(lp, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('tydTrozoG.pickle', 'wb') as handle:
	pickle.dump(tyd, handle, protocol=pickle.HIGHEST_PROTOCOL)


