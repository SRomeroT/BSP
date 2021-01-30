import numpy as np
import matplotlib.pyplot as plt
import math
import locale
import pickle


def detect_event(signal, sample_freq,threshold = 0.3):
    num_spike = 0

    matrix = []

    signal_size = len(signal)

    for i in range(1, signal_size-1, sample_freq):
        prev_value = float(signal[i - 1].replace(",","."))
        current_value = float(signal[i].replace(",","."))
        next_value = float(signal[i + 1].replace(",","."))

        if prev_value<current_value and next_value < current_value and current_value > threshold:
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
    lp_directory = signal_name_lp + ".pickle"

    vd_directory = "./../pickles/" + vd_directory
    lp_directory = "./../pickles/" + lp_directory

    sample_freq = 1
    vd = pickle.load(open(vd_directory, "rb"))
    lp = pickle.load(open(lp_directory, "rb"))

    vd_matrix = detect_event(vd, sample_freq,0.33)
    lp_matrix = detect_event(lp, sample_freq,1.12)

    with open(signal_name_vd + "_matrix.pickle", 'wb') as handle:
        pickle.dump(vd_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open(signal_name_lp + "_matrix.pickle", 'wb') as handle:
        pickle.dump(lp_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    main()
