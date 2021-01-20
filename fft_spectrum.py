
# coding: utf-8

# In[ ]:


import math
import numpy as np
import matplotlib.pyplot as plt
import pickle
from numpy.fft import fft, fftfreq

def powerSpectrum(signal_array,signal_spacing,nombre_señal):
    signal_freq = 1/signal_spacing
    n_signal = len(signal_array)

    freqs_signal = (signal_freq*1000)*np.arange(0,n_signal)/n_signal

    mask = fftfreq(n_signal) > 0

    fft_signal = fft(signal_array)

    fft_unilateral = (2.0 * np.abs(fft_signal/n_signal))

    ps_signal = 2.0 * np.square(np.abs(fft_signal/n_signal))

    plt.figure(figsize=(12, 6))
    plt.plot(freqs_signal[mask], fft_unilateral[mask])
    plt.title('FFT vs Frecuencia - ' + nombre_señal)
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('FFT (mV)')
    plt.show()

    plt.figure(figsize=(12, 6))
    plt.plot(freqs_signal[mask], ps_signal[mask])
    plt.title('Power Espectrum - ' + nombre_señal)
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Power ($mV^2/Hz$)')
    plt.xlim(0,2000)
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
    plt.show()

    return freqs_signal,fft_signal,fft_unilateral,ps_signal

def main():
    part = "C"

    signal_name_vd = "vdTrozo" + part
    signal_name_lp = "lpTrozo" + part

    vd_directory = signal_name_vd + ".pickle"
    lp_directory = signal_name_lp  + ".pickle"

    vd = pickle.load(open(vd_directory, "rb" ))
    lp = pickle.load(open(lp_directory , "rb" ))

    vd = np.array(np.char.replace(vd, ',', '.'),dtype='double')
    lp = np.array(np.char.replace(lp, ',', '.'),dtype='double')

    powerSpectrum(np.array(vd,dtype='double'),0.1,'Recuperacion - VD')

    powerSpectrum(np.array(lp,dtype='double'),0.1,'Recuperacion - LP')
    
    return

if __name__ == "__main__":
    main()

