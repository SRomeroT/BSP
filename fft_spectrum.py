import math
import numpy as np
import  matplotlib.pyplot as plt
import pickle

part = "R"

signal_name_vd = "vdTrozo" + part
signal_name_lp = "lpTrozo" + part
vd_directory = signal_name_vd + ".pickle"
lp_directory = signal_name_lp  + ".pickle"

vd_directory = "D:\\Sergio\\Master\\BSP\\" + vd_directory
lp_directory = "D:\\Sergio\\Master\\BSP\\" + lp_directory


vd = pickle.load(open(vd_directory, "rb" ))
lp = pickle.load(open(lp_directory , "rb" ))

signal_size = len(vd)
sample_freq = 0.01
sampling_rate = 1/sample_freq

x = vd

num_final = signal_size*sample_freq
time = np.arange(0,num_final,sample_freq)
plt.plot(time,x)
plt.show()
fft_data = np.fft.fft(x)

abs_fourier_transform = np.abs(fft_data)
power_spectrum = np.square(abs_fourier_transform)

frequency = np.linspace(0, sampling_rate/2, len(power_spectrum))

plt.plot(frequency, power_spectrum)
plt.show()