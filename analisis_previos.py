import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import signal
from scipy.signal import butter, lfilter, freqz
from scipy.fftpack import rfft, irfft, fftfreq

import pickle



def detect_spikes(dic,v,threshold=0.3):

    spike = 0


    if dic["lv2"] < dic["lv1"] and dic["lv1"] > v and dic["lv1"] > threshold and dic["lv3"]==0:
        spike = 1
        dic["lv3"]=1
    if dic["lv3"] ==1 and v<threshold:
        dic["lv3"] =0

    dic["lv2"] = dic["lv1"]
    dic["lv1"] = v

    return spike

def firing_rate(values, threshold):
    print("Calculando Firing rate\n")
    dic = {}
    dic["lv1"] = -100
    dic["lv2"] = -100
    total_spikes=0
    for val in values:
        total_spikes+=detect_spikes(dic,val,threshold)

    print("Numero total de spikes: "+str(total_spikes))
    
    fr = total_spikes

    return fr

def regularity_scatter(times,values,periodo,threshold,title):
    print("Generando scatter plot\n")
    fig, ax = plt.subplots(1, figsize=(10, 6))
    fig.suptitle(title)
    plt.xlabel("Time (cs)")
    plt.ylabel("# burst")



    last_spike_time = 0
    n_spikes_val = 0
    lens = []
    nspikes = []


    aux = 0

    burst_limit = 1000
    init_time = 0
    dic = {}
    dic["lv1"] = -100
    dic["lv2"] = -100
    dic["lv3"] = 0

    total_bursts=0
    burst_init = 30
    ISIs = []
    f_init=1
    s_len = []
    s_last_len = 0

    for time,value in zip(times,values):

        sp=detect_spikes(dic,value,threshold)
        if sp == 1:
            ISIs.append(aux)
            last_spike_time = time
            n_spikes_val+=1
            
            
            burst_init = 1
        if  burst_init==1:
            aux+=periodo
        if burst_init==1 and f_init==1:
            init_time = time
            f_init=0
            if s_last_len !=0:
                s_len.append(time-s_last_len)

        if (time-last_spike_time)>60 and burst_init ==1:
            burst_init = 0
            
            

            total_bursts+=1

            dic["lv1"] = -100
            dic["lv2"] = -100
            dic["lv3"] = 0

            # print(ISIs)
            ax.scatter(np.array(ISIs), np.full(len(ISIs), total_bursts),
                        color="green", 
                        s=10,          
                        alpha=0.5,       
                        linewidths=0.1)
            
            nspikes.append(n_spikes_val)
            
            if n_spikes_val >1:
                # print("L:"+str(last_spike_time))
                # print("I"+str(init_time))
                # print("result: "+str(last_spike_time-init_time))
                lens.append(last_spike_time-init_time)
                s_last_len = last_spike_time
            ISIs= []
            aux = 0
            n_spikes_val = 0
            last_spike_time =0
            f_init=1

            




        if total_bursts==burst_limit:
            break


    print(total_bursts)
    lens = np.array(lens)
    nspikes = np.array(nspikes)
    s_len = np.array(s_len)
    print("Longitud media rafaga: "+str(lens.mean()))
    print("Desviacion estandar: "+str(lens.std()))
    print("Nº spikes medio : "+str(nspikes.mean()))
    print("Desviacion estandar: "+str(nspikes.std()))
    print("Longitud media silencio : "+str(s_len.mean()))
    print("Desviacion estandar: "+str(s_len.std()))
    plt.xlim((0,200))
    plt.show()
def spikes_reg(times,values,threshold):
    print("Calculando regularidad spikes\n")
    i =0
    aux_time = 0
    
    dic = {}
    dic["lv1"] = -100
    dic["lv2"] = -100
    dic["lv3"] = 0
    ISIs = []
    for time, value in zip(times,values):
        sp = detect_spikes(dic,value,threshold)
        if sp ==1:
            if aux_time == 0:
                aux_time = time
            else:
                if (time-aux_time)<2:
                    pass
                    # print(time)
                    # print(aux_time)
                    # print("c:"+str(values[i])+" time: "+str(times[i]))
                    # print("c-1:"+str(values[i-1])+" time: "+str(times[i-1]))
                    # print("c-2:"+str(values[i-2])+" time: "+str(times[i-2]))
                    # print("c-3:"+str(values[i-3])+" time: "+str(times[i-3]))
                    # print("c-4:"+str(values[i-4])+" time: "+str(times[i-4]))
                    # print("c-5:"+str(values[i-5])+" time: "+str(times[i-5]))
                    # plt.plot(values[i-50:i+50])
                    # plt.show()

                ISIs.append(time-aux_time)
                aux_time = time
        i+=1

    ISIs = np.array(ISIs)
    print("Media ISIs: " + str(ISIs.mean()))
    print("Desviacion estandar ISIs: " + str(ISIs.std()))
    # print(ISIs)
    return ISIs

def distribution_analisis(ISIs,title,period):

    print(np.max(ISIs))
    print(np.max(ISIs)+period)
    print((np.max(ISIs)+period)/period)
    print(np.round(np.max(ISIs)+period,1))
    # print(ISIs)
    axisx = np.arange(0,np.round(np.max(ISIs)+period,1),period)
    # tam = int(np.round((np.max(ISIs))/period)+1)
    # print(tam)
    axisy = np.zeros(len(axisx))
    for i in ISIs:
        # print(i)
        index = int(np.round(i,1)/period)
        # print(np.round(i,1))
        # print(index)
        axisy[index] +=1

    # axisx *=period
    # print(axisy[155])
    print(len(axisx))
    print(len(axisy))
    plt.bar(axisx,axisy)
    plt.xlim(0,100)
    plt.title(title)
    plt.xlabel("Tiempo (ms)")
    plt.ylabel("# ISIs")
    plt.show()

def analisis_previos():

    period = 0.1
    threshold_vd = 0.3
    threshold_lp = 0.5

    lp = pickle.load(open("BSP/lpTrozoC.pickle", "rb"))
    vd = pickle.load(open("BSP/vdTrozoC.pickle", "rb"))



    fvd = firing_rate(vd[0:100000],0.2)/10
    flp = firing_rate(lp[0:100000],0.28)/10
    # flp_nosubumbral = firing_rate(lp[0:10000],0.03)
    print("Tasa de disparo LP: "+str(flp)+"spikes/s")
    # print("Tasa de disparo LP no subumbral: "+str(flp_nosubumbral)+"spikes/s")
    print("Tasa de disparo VD: "+str(fvd)+"spikes/s")



    #ESTUDIO DE LA REGULARIDAD

    #suavizado de la señal
    # vd = signal.savgol_filter(vd, 1, 1) # window size 51, polynomial order 3
    # plt.plot(vd[0:20000])
    # plt.show()



    axisx = np.arange(0,len(vd)*period,0.1)
    ISIs = spikes_reg(axisx,vd,threshold_vd)
    distribution_analisis(ISIs,"Distribución IPIs VD etapa Control",period)
    regularity_scatter(axisx,vd,period,threshold_vd,'Scatterplot distribución de ISIs VD etapa C')



    axisx = np.arange(0,len(lp)*period,0.1)
    ISIs = spikes_reg(axisx,lp,threshold_vd)
    distribution_analisis(ISIs,"Distribución IPIs LP etapa Control",period)

    regularity_scatter(axisx,lp,period,threshold_lp,'Scatterplot distribución de ISIs LP etapa C')


    return



def analisis_previos_r():

    period = 0.1
    threshold_vd = 0.25
    threshold_lp = 0.8

    lp = pickle.load(open("BSP/lpTrozoR.pickle", "rb"))

    vd = pickle.load(open("BSP/vdTrozoR.pickle", "rb"))




    fvd = firing_rate(vd[0:100000],0.2)/10
    flp = firing_rate(lp[0:100000],0.28)/10
    # flp_nosubumbral = firing_rate(lp[0:10000],0.03)
    print("Tasa de disparo LP: "+str(flp)+"spikes/s")
    # print("Tasa de disparo LP no subumbral: "+str(flp_nosubumbral)+"spikes/s")
    print("Tasa de disparo VD: "+str(fvd)+"spikes/s")


    print("analisis vd")


    #ESTUDIO DE LA REGULARIDAD

    #suavizado de la señal
    # vd = signal.savgol_filter(vd, 1, 1) # window size 51, polynomial order 3


    

    # DEL 6000 AL 17500 COMPROBAR ISIs 175000-6000= 11500
    # axisx = np.arange(0,11500/10,0.1)
    # print(len(vd))
    # ISIs = spikes_reg(axisx,vd[6000:17500],threshold_vd)
    # ISIs = spikes_reg(axisx,vd[0:11500],threshold_vd)
    # print(ISIs)
    # plt.plot(vd[0:2000])
    # plt.show()
    # maxIsi = ISIs+100

    # print("max: "+str(np.max(vd)))
    # axisx = np.arange(0,len(vd)/10,0.1)
    # print(axisx[0:10])
    # ISIs = spikes_reg(axisx,vd,threshold_vd)
    # print(ISIs[0:1000])
    # plt.hist(ISIs)
    # plt.show()



    
    axisx = np.arange(0,len(vd)*period,0.1)
    ISIs = spikes_reg(axisx,vd,threshold_vd)
    distribution_analisis(ISIs,"Distribución IPIs VD etapa Recuperación",period)
    regularity_scatter(axisx,vd,period,threshold_vd,'Scatterplot distribución de ISIs VD etapa R')



    axisx = np.arange(0,len(lp)*period,0.1)
    ISIs = spikes_reg(axisx,lp,threshold_lp)
    distribution_analisis(ISIs,"Distribución IPIs LP etapa Recuperación",period)
    regularity_scatter(axisx,lp,period,threshold_lp,'Scatterplot distribución de ISIs LP etapa R')


    return
def analisis_previos_G():

    period = 0.1
    threshold_vd = 0.3
    threshold_lp = 0.3

    lp = pickle.load(open("BSP/lpTrozoR.pickle", "rb"))
    vd = pickle.load(open("BSP/vdTrozoR.pickle", "rb"))





    fvd = firing_rate(vd[0:100000],0.2)/10
    flp = firing_rate(lp[0:100000],0.28)/10
    # flp_nosubumbral = firing_rate(lp[0:10000],0.03)
    print("Tasa de disparo LP: "+str(flp)+"spikes/s")
    # print("Tasa de disparo LP no subumbral: "+str(flp_nosubumbral)+"spikes/s")
    print("Tasa de disparo VD: "+str(fvd)+"spikes/s")



    #ESTUDIO DE LA REGULARIDAD

    #suavizado de la señal
    # vd = signal.savgol_filter(vd, 1, 1) # window size 51, polynomial order 3



    

    # DEL 6000 AL 17500 COMPROBAR ISIs 175000-6000= 11500
    # axisx = np.arange(0,11500/10,0.1)
    # print(len(vd))
    # ISIs = spikes_reg(axisx,vd[6000:17500],threshold_vd)
    # ISIs = spikes_reg(axisx,vd[0:11500],threshold_vd)
    # print(ISIs)
    # plt.plot(vd[0:2000])
    # plt.show()
    # maxIsi = ISIs+100

    # print("max: "+str(np.max(vd)))
    # axisx = np.arange(0,len(vd)/10,0.1)
    # print(axisx[0:10])
    # ISIs = spikes_reg(axisx,vd,threshold_vd)
    # print(ISIs[0:1000])
    # plt.hist(ISIs)
    # plt.show()





    axisx = np.arange(0,len(vd)*period,0.1)
    ISIs = spikes_reg(axisx,vd,threshold_vd)

    distribution_analisis(ISIs,"Distribución IPIs VD etapa GABA",period)
    regularity_scatter(axisx,vd,period,threshold_vd,'Scatterplot distribución de ISIs VD etapa G')

    axisx = np.arange(0,len(lp)*period,0.1)
    ISIs = spikes_reg(axisx,lp,threshold_lp)
    distribution_analisis(ISIs,"Distribución IPIs LP etapa GABA",period)

    regularity_scatter(axisx,lp,period,threshold_lp,'Scatterplot distribución de ISIs LP etapa G')


    return
def main():
    analisis_previos()
    analisis_previos_r()
    analisis_previos_G()
    
if __name__ == "__main__":
    main()