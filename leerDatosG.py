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

directory = "DatosSinapsisArtificial/TrozoG.txt"
# directory = "D:\\Sergio\\Master\\BSP\\DatosSinapsisArtificial/TrozoG.txt"
f = open(directory,'r')

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
		split = line.split("\t")
		vd_value = split[1]
		lp_value = split[0]
		tyd_value = split[2]

		vd.append(float(vd_value.replace(",", ".")))
		lp.append(float(lp_value.replace(",", ".")))
		tyd.append(float(tyd_value.replace(",", ".")))

with open('vdTrozoG.pickle', 'wb') as handle:
	pickle.dump(vd, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('lpTrozoG.pickle', 'wb') as handle:
	pickle.dump(lp, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('tydTrozoG.pickle', 'wb') as handle:
	pickle.dump(tyd, handle, protocol=pickle.HIGHEST_PROTOCOL)


