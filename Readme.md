# README

En este repositorio se encuentra el código utilizado para el análisis de señales asociadas a la sinapsis artificial. 

### Preprocesamiento

En primer lugar, los datos son preprocesados y transformados en objetos pickle a partir de los siguientes ficheros: 

  - leerDatos.py para las neuronas LP y VD de la etapa Control
  - leerDatosG.py para las neuronas LP y VD de la etapa GABA
  - leerDatosR.py para las neuronas LP y VD de la etapa Recuperación

### Análisis previo
Posteriormente, para realizar el análisis previo, se ha implementado una serie de funciones que se encuentra en el fichero analisis_previos.py , junto con el fichero spike_detector.py , en el cual se encuentra el código asociado a la detección de spikes.

### Información Mutua
Por otro lado, el cálculo de la información mutua se ha llevado a cabo a partir de la implementación que se localiza en el fichero informacionMutua.py , de la cual requiere los siguientes ficheros para computar este cálculo:

 - posibilitiesUtils.py para encontrar las diferentes posibilidades de palabra que puedan aparecer en una señal
 - transformToBinary.py para transformar la señal a binario
 - wordsUtils.py para identificar las diferentes palabras que se encuentran a lo largo de la señal

### Entropía de la Permutación

Para el cálculo de la entropía de la permutación se ha utilizado el código que se encuentra en el repositorio https://github.com/nikdon/pyEntropy.

### Transformada de Fourier
Finalmente, se han utilizado una serie de archivos para analizar la señal a partir de la transformada de Fourier:

 - fft_spectrum.py realiza un cálculo de fft a la señal neuronal
 - Crear pickles para FFT.ipynb es el notebook que se ha implementado para convertir las señales en objetos pickles para posteriormente analizarlas y procesarlas 
 - FTTs, Power Spectrum y Filtrar ruido de spikes.ipynb es el notebook que finalmente se ha utilizado para analizar estas señales neuronales mediante los cálculos mencionados anteriormente asociados al cálculo de la FFT

