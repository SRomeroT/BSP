import numpy as np
import matplotlib.pyplot as plt
import math
import locale
import pickle


def detect_event(signal, sample_freq):
    num_spike = 0

    matrix = []

    threshold = 0.3

    signal_size = len(signal)

    for i in range(0, signal_size-1, sample_freq):
        current_value = signal[i]
        next_value = signal[i + 1]

        if next_value <= current_value and current_value > threshold:
            num_spike += 1
            matrix.append(1)
        else:
            matrix.append(0)


    print("Total Spikes: " + str(num_spike))

    return matrix


def main():

    # locale.setlocale(locale.LC_ALL, 'es_ES')
    potential = {}

    part = "R"

    signal_name_vd = "vdTrozo" + part
    signal_name_lp = "lpTrozo" + part
    vd_directory = signal_name_vd + ".pickle"
    lp_directory = signal_name_lp  + ".pickle"

    vd_directory = "D:\\Sergio\\Master\\BSP\\" + vd_directory
    lp_directory = "D:\\Sergio\\Master\\BSP\\" + lp_directory

    sample_freq = 1
    vd = pickle.load(open(vd_directory, "rb" ))
    lp = pickle.load(open(lp_directory , "rb" ))

    vd_matrix = detect_event(vd, sample_freq)
    lp_matrix = detect_event(lp, sample_freq)

    with open(signal_name_vd + "_matrix.pickle", 'wb') as handle:
        pickle.dump(vd_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open(signal_name_lp + "_matrix.pickle", 'wb') as handle:
        pickle.dump(lp_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)



if __name__ == "__main__":
    main()
