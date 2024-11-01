---
title: "README"
author: "Andrea Valiente,Juliana Hernandez"
date: "2024-11-01"
editor_options: 
  markdown: 
    wrap: 60
---

------------------------------------------------------------------------


## ***LABORATORIO 4: Variabilidad de la Frecuencia Cardiaca usando la Transformada Wavelet***

------------------------------------------------------------------------

```         
                                       Procesamiento digiatal de señales
                                             Carolina Corredor
                                                  BMED B  
                                                   UMNG 
```

------------------------------------------------------------------------

> **Objetivo:** `Analizar la variabilidad de la frecuencia cardíaca (HRV) utilizando la transformada wavelet para identificar cambios en las frecuencias características y analizar la dinámica temporal de la señal cardíaca`

------------------------------------------------------------------------

**Descripción:** Para el desarrollo del laboratorio, se realizará primero una investigación teórica que abarque los conceptos necesarios para garantizar un adecuado desempeño de la práctica. Esta investigación incluirá:

-   Actividad simpática y parasimpática del sistema nervioso autónomo.

-   Efectos de la actividad simpática y parasimpática en la frecuencia cardíaca.

-   Variabilidad de la frecuencia cardíaca (HRV), medida a través de las fluctuaciones en el intervalo R-R y las frecuencias relevantes en este análisis.

-   Transformada Wavelet: definición, aplicaciones y tipos de wavelets utilizados en el análisis de señales biológicas.

| CONCEPTO | DESCRIPCIÓN |
| --- | --- |
| `Actividad Simpática del sistema nervioso autónomo` |La actividad simpática está dirigida para colocar al individuo en una situación de defensa ante circunstanciasde peligro, real o potencial. La estimulación simpática conduce a variaciones de las funciones viscerales destinadas a proteger la integridad del organismo como un todo y a garantizar la supervivencia.La activación masiva del sistema simpático produce un conjunto de reacciones que se definen como respuesta de alarma(fight or flight). |
|       | **FUENTE:**  Navarro, X. (2002). Fisiología del sistema nervioso autónomo. Revista Neurológica, 35(6), 553-562.|
| `Actividad Parasimpática del sistema nervioso autónomo` |La actividad del parasimpático está relacionada con funciones protectoras y de conservación, que favorecen el correcto funcionamiento particular de los diferentes órganos viscerales. Los componentes funcionales del sistema parasimpático no actúan simultáneamente en condiciones normales, sino que participan en reflejos específicos o en reacciones integradas para promover una función visceral concreta.|
|       | **FUENTE:**  Navarro, X. (2002). Fisiología del sistema nervioso autónomo. Revista Neurológica, 35(6), 553-562.|
| `Efecto de la actividad simpática en la frecuencia cardiaca` | La activación del sistema simpático aumenta la frecuencia cardíaca al liberar catecolaminas, como la adrenalina y la noradrenalina. Estas hormonas actúan sobre los receptores beta-adrenérgicos del corazón, incrementando tanto la frecuencia como la fuerza de las contracciones cardíacas.Este efecto es importante en situaciones de estrés, ejercicio físico, o cualquier circunstancia que requiera una rápida respuesta de energía y oxígeno en los tejidos |
|       | **FUENTE:**  Fernández, V. A., Vargas, S. C., Rodríguez, S. L. M., Umaña, D. R., & Ramírez, A. F. (2017). Variabilidad de la frecuencia cardíaca como indicador de la actividad del sistema nervioso autónomo: implicaciones en el ejercicio y patologías. Revista médica de la universidad de Costa Rica, 11(1).|
| `Efecto de la actividad Parasimpatica en la frecuencia cardiaca` | El sistema parasimpático actúa reduciendo la frecuencia cardíaca. Esto ocurre a través de la liberación de acetilcolina, que estimula los receptores muscarínicos en el nodo sinoauricular del corazón (el marcapasos natural), disminuyendo el ritmo de descarga. La actividad parasimpática es predominante durante el descanso, la digestión y situaciones de calma, favoreciendo la recuperación y conservación de energía |
|       | **FUENTE:**  Fernández, V. A., Vargas, S. C., Rodríguez, S. L. M., Umaña, D. R., & Ramírez, A. F. (2017). Variabilidad de la frecuencia cardíaca como indicador de la actividad del sistema nervioso autónomo: implicaciones en el ejercicio y patologías. Revista médica de la universidad de Costa Rica, 11(1)|
| `Variabilidad de la frecuencia cardiaca (HRV)medida como flutuaciones en el intervalo R-R` | El estudio de la HRV se puede realizar utilizando diferentes métodos de medidas. Entre ellos encontramos medida estáticas (análisis del tiempo dominante), métodos geométricos y análisis espectral (análisis de la frecuencia dominante).e la HRV es un indicador que provee datos importantes a la hora de determinar la condición aeróbica de las personas;pero que de igual forma requiere de muchos más estudios investigativos para llegar a procedimientos claros y precisos que permitan la correcta utilización de los resultados obtenidos De igual forma, provee datos importantes sobre el estado de salud a nivel cardiaco de las personas, puesto que su estudio permite analizar la influencia del Sistema Nervioso Autónomo a nivel cardiaco, estas fluctuaciones cardiacas, están condicionadas por los procesos respiratorios de inspiración y expiración y mediada por la actividad de los sistemas nerviosos simpático y parasimpático Las fluctuaciones de la frecuencia cardiaca son comúnmente valoradas por las mediciones del intervalo R-R |
|       | **FUENTE:** Guzmán, J. E. O., & Romero, D. M. (2008). Variabilidad de la frecuencia cardiaca, una herramienta útil. Rev. Digital., BuenosAires, 121|
| `frecuencias de interés en este análisis` | **Muy baja frecuencia (VLF):** está alimentado por frecuencias menores a 0.04 Hz. Algunos autores consideran que la VLF está influenciada por el ritmo circadiano, el perímetro vasomotor y la termorregulación. |
|       |**Baja frecuencia (LF):** son componentes que están alrededor de 0.1 Hz. El poder de producción en la LF epende del tono simpático a causa de la actividad de los varo-receptores.|
|       | **Alta frecuencia (HF):** componente sincronizado con la frecuencia de respiración. Está sobre un rango de 0.2 a 0.5 Hz dependiendo de la frecuencia respiratoria y es considerado un indicador de la actividad vagal|
|       | **FUENTE:** Guzmán, J. E. O., & Romero, D. M. (2008). Variabilidad de la frecuencia cardiaca, una herramienta útil. Rev. Digital., BuenosAires, 121|


| Transformada Wavelet | Caracteristicas |
| --- | --- |
| `DEFINICIÓN` | es una rama de la matemática relativamente nueva, la cual ha encontrado aplicaciones muy rápidamente en un gran número de disciplinas incluyendo la Física, Análisis Numérico, Procesamiento de Señal, Probabilidad y Estadística. |
|  `USOS`      | Puede ser usada para aproximar funciones/señales de acuerdo a escala resolución usando un conjunto de funciones base llamadas wavelets.|
| | Permiten representaciones de funciones en las cual se retiene tanto la escala como la información espacial. Muchas funciones pueden ser aproximadas con gran exactitud usando sólo un pequeño número de coeficientes wavelet. |
|       | Puede ser usada para representar económicamente características de interés localizadas en una señal, lo cual la convierte en un candidato idea para la extracción de características en contextos de clasificación|
|       | Puede ser usado como una técnica de filtrado para la remoción de los componentes de alta frecuencia incluidas en los datos, o usado como un método para representar la información de manera sucinta. Alternativamente, tiene excelentes propiedades para la compresión de datos |
|   `CALCULO`     | Cada coeficiente wavelet se calcula tomando el producto escalar del vector de datos por una de las funciones base. El conjunto de las funciones base se deriva a partir de una única función (frecuentemente llamada **"Wavelet Madre"**) por una serie de dilataciones y tralaciones.|
| `TIPOS` | **Wavelets de Haar:** Es la wavelet más simple, con forma de escalón,ácil de implementar, pero ofrece una resolución limitada en comparación con otras wavelets |
|       |**Wavelets de Daubechies (db):** Muy utilizadas en análisis de señales y procesamiento de imágenes debido a su capacidad para captar detalles en alta resolución,Las versiones db2, db4, db8, etc., representan diferentes órdenes y niveles de suavidad|
|       | **Wavelets de Symlet (sym):** Variantes simétricas de las wavelets Daubechies, con una forma menos distorsionada.Usadas en aplicaciones donde se requiere evitar efectos de asimetría, como en procesamiento de imágenes y de señales de audio|
|       | **Wavelets de Coiflet (coif):**  Desarrolladas para tener tanto la wavelet madre como su primera derivada en valores cercanos a cero.Tienen buena localización en frecuencia y tiempo, adecuadas para aplicaciones de análisis en finanzas y en señales de ECG.|
|       | **Wavelets B-Spline (bior)::** Basadas en splines, proporcionan una buena localización en el dominio del tiempo.Muy utilizadas en análisis de imágenes médicas y procesamiento de señales, ya que permiten obtener una buena precisión en bordes|
|       | **Wavelets Morlet::** Basadas en una función senoidal modulada por una gaussiana, proporcionan una alta resolución en frecuencia.Amplias aplicaciones en análisis de EEG, ECG y otras señales biomédicas, ya que son efectivas para identificar frecuencias en señales continuas.|
|       | **Wavelets Mexican Hat (Sombrero Mexicano):**  Basadas en la segunda derivada de una función gaussiana, tienen una forma de pico similar a un sombrero.Muy utilizadas en detección de bordes y en análisis de señales de imágenes donde se desea identificar picos.|
|       | **Wavelets Meyer:**  Son wavelets ortogonales de tiempo continuo, diseñadas para tener una buena localización en frecuencia y decaimiento suave.Utilizadas en aplicaciones de análisis de señales y procesamiento de imágenes donde se necesita preservar detalles específicos.|
|       | **FUENTE:**  Montoya, J. R. A. (2001). La transformada wavelet. Revista de la Universidad de Mendoza.|




### *INSTRUCCIONES*

1.Al realizar este analisis para mejor compresión del desarrollo de la guia se plantea el siguiente diagrama de flujo donde se ecuentra una breve descripción de cada paso para obtener los resultados que se esperan .

![DIAGRAMA DE FLUJO](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/parte1.png) 
![DIAGRAMA DE FLUJO](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/parte2.png)
![DIAGRAMA DE FLUJO](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/parte3.png)
![DIAGRAMA DE FLUJO](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/parte4.png) 
![DIAGRAMA DE FLUJO](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/parte5.png)

2.Se investiga en la literatura la manera correcta de la ubicación de los electrodos para poder capturar la señal ECG para ello se diseña el circuito utilizando el sensor AD8232,arduino,cables de electrodos ,electrodos,jumpers como se muestra a continuacion ![CIRCUITO](https://github.com/SeebastianOchoa/IMAGENESLAB3/blob/4efcb0c3f74646ea466c312043812b58b5261d38/CIRCUITO.jpeg)

3.Se programa el arduino para enviar los datos captados por el sensor y asi poder ser graficados,para obtener estos datos se colocaron los electrodos uno en el brazo derecho (RA): Coloca un electrodo en el brazo derecho, justo debajo de la clavícula en el lado derecho del pecho. el otro en el brazo izquierdo (LA): Coloca otro electrodo en el brazo izquierdo, debajo de la clavícula en el lado izquierdo del pecho y por ultimo la tierra o referencia: Coloca el tercer electrodo en un punto neutro, como en la parte baja del abdomen o cerca de la cadera derecha o izquierda

4.Se sube este text a spyder para poder empezar con el analisis correspondiente, lo primero que se realiza es graficar la señal y se busca la frecuencia de muestreo adecuada utilizando el teorema de muestreo de Nyquist donde se establece que la frecuencia de muestreo debe ser al menos el doble de la frecuencia maxima de la señal,La frecuencia de muestreo ideal para una señal ECG suele ser entre 250 y 500 Hz, aunque puede variar dependiendo de la precisión que se requiera para el análisis de las características de la señal. Para aplicaciones médicas avanzadas o investigación, es común usar frecuencias más altas, incluso de 1000 Hz, para capturar con detalle los cambios rápidos en la señal siendo asi con el teorema mencionado anteriormente podemos decir que la frecuencia de muestreo escogida seraa de 1000 Hz. Se observa a continuación la gráfica de la señal ECG original con todas sus características, incluyendo frecuencia de muestreo, tiempo de muestreo, niveles de cuantificación, y estadísticos principales.

![SEÑAL ORIGINAL](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/Se%C3%B1al%20original.png)

> > A partir de la gráfica de la señal ECG obtenida durante una toma de datos de 5 minutos, se observan varios aspectos importantes. La señal muestra oscilaciones en amplitud alrededor de un nivel medio, con picos pronunciados que probablemente corresponden a los complejos QRS de cada latido, aunque también se aprecia bastante ruido o variabilidad, posiblemente causado por movimientos, artefactos, o ruido del ambiente. Las oscilaciones regulares reflejan la actividad del corazón, y su frecuencia podría analizarse para calcular la frecuencia cardíaca en cada instante y estudiar su variabilidad. Además, algunos puntos presentan valores atípicos o picos negativos que podrían deberse a ruido en la adquisición o movimientos del paciente durante la toma.En cuanto a la calidad general de la señal, visualmente parece estar afectada por ruido

![DATOS ESTADISTICOS](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/datos%20estadisticos.png)

> > **Número de muestras:** 30,000 muestras en total, lo cual tiene sentido ya que se tiene una duración de 300 segundos y una frecuencia de muestreo de 1000 Hz (300 \* 1000 = 30,000). Esto indica que se tienen suficientes datos para realizar el análisis.
> >
> > **Frecuencia de muestreo (fs):** se escogió de 1000 Hz ya que es una frecuencia de muestreo adecuada para la mayoría de los análisis de ECG, ya que permite capturar con precisión los detalles de la señal.
> >
> > **Tiempo de muestreo (ts):** Calculado como 0.001 segundos, que es consistente con 1 / fs y corresponde a un intervalo de muestreo muy fino, lo cual es adecuado para señales de ECG.
> >
> > **Datos estadísticos principales:**
> >
> > -   Promedio: Cerca de cero (aunque con un ligero redondeo), lo cual es común en señales de ECG que han sido procesadas para estar centradas en cero.
> >
> > -   Desviación estándar: 15.64, lo cual indica una variabilidad moderada en la señal, esperable en señales fisiológicas como el ECG.
> >
> > -   Valor mínimo: -101.88 y valor máximo: 106.61. Estos valores sugieren que la señal tiene una buena amplitud y parece contener tanto picos positivos como negativos, lo cual es característico de un ECG (picos P y complejos QRS)

Se muestra el código que se implemento para el paso 4

```         
# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import find_peaks

# Ruta completa donde se encuentra el archivo
file_path =  r'C:\users\andrea\downloads\lab4 procesamiento\ecg_signal.txt'  # Cambia esto por la ruta de tu archivo

# Cargamos el archivo de datos de ECG
ecg_data = np.loadtxt(file_path, delimiter=',')  # Lee los datos en un array de numpy

# Extraemos la señal ECG (suponiendo que está en la segunda columna)
ecg_signal = ecg_data[:, 1]  # Selecciona la segunda columna de datos
num_muestras = len(ecg_signal)  # Calcula el número de muestras

# Definimos la duración de la señal y la frecuencia de muestreo
duracion = 300  # Duración de la señal en segundos (ajusta según tu archivo)
fs = 1000  # Frecuencia de muestreo en Hz (ajusta según tu señal)
ts = 1 / fs  # Tiempo de muestreo (inverso de fs)

# Cálculo de estadísticas básicas de la señal
mean_val = np.mean(ecg_signal)  # Promedio de la señal
std_dev = np.std(ecg_signal)  # Desviación estándar de la señal
min_val = np.min(ecg_signal)  # Valor mínimo
max_val = np.max(ecg_signal)  # Valor máximo

# Mostramos los estadísticos y parámetros calculados
print(f"Número de muestras: {num_muestras}")
print(f"Frecuencia de muestreo: {fs} Hz")
print(f"Tiempo de muestreo: {ts} segundos")
print(f"Estadísticos principales:")
print(f"  Promedio: {mean_val:.2f}")
print(f"  Desviación estándar: {std_dev:.2f}")
print(f"  Valor mínimo: {min_val:.2f}")
print(f"  Valor máximo: {max_val:.2f}")

# Gráfica de la señal original 
plt.figure(figsize=(18, 12))
plt.subplot(4, 1, 1)  # Subgráfico para la señal original
plt.plot(ecg_signal, label='Señal original', color='blue')
plt.title('Señal ECG original en reposo')
plt.xlabel('Muestras')
plt.ylabel('Amplitud (mV)')
plt.grid(True)
plt.legend()
```

5.En este análisis de señales ECG, se implementaron tres filtros: un filtro pasa alto, un filtro pasa bajo y un filtro pasa banda, con el objetivo de limpiar la señal de ruido y artefactos no deseados que podrían afectar la interpretación de los componentes esenciales de la señal. Las frecuencias de corte de 0.5 Hz y 50 Hz se seleccionaron cuidadosamente para abordar distintas fuentes de ruido y preservar solo las frecuencias relevantes del ECG.

-   **FILTRO PASA ALTO** ![SEÑAL FILTRO PASA ALTO](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/pasa%20alto%20.png)

> La gráfica muestra una señal ECG filtrada con un filtro pasa alto de 0.5 Hz, cuyo propósito es eliminar las componentes de baja frecuencia, como el ruido de movimiento y las fluctuaciones de la línea base, que pueden interferir en el análisis de la señal. Con este filtrado, se observa una reducción en las variaciones lentas de la señal, lo que permite resaltar mejor las características cardíacas importantes, como los picos R. La señal filtrada oscila entre aproximadamente -100 mV y 100 mV, y aunque el filtro atenúa ciertas frecuencias bajas, aún se percibe bastante ruido en frecuencias más altas, que no son afectadas por este tipo de filtro. Además, se observan algunas variaciones bruscas, como picos pronunciados alrededor de las posiciones 15000 y 28000, que podrían ser artefactos o eventos específicos de la señal

-   **FILTRO PASA BAJO** ![SEÑAL FILTRO PASA BAJO](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/pasa%20bajo.png)

> la gráfica representa una señal de ECG filtrada utilizando un filtro pasa bajo con una frecuencia de corte de 50 Hz. El objetivo de aplicar este filtro es eliminar el ruido de alta frecuencia, como el generado por la red eléctrica, y mantener las frecuencias que contienen información relevante del ECG, generalmente situadas por debajo de los 50 Hz. La señal presenta un patrón relativamente constante con fluctuaciones en la amplitud, características de los ciclos cardíacos, donde las variaciones corresponden a los latidos. Sin embargo, en algunos puntos se destacan picos más altos que el resto, lo cual puede indicar la presencia de artefactos o interferencias externas. Estos picos aislados podrían estar relacionados con movimientos involuntarios o ruido residual

-   **FILTRO PASABANDA** ![SEÑAL FILTRO PASA BAJO](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/pasa%20banda.png)

> la gráfica muestra la señal de ECG procesada con un filtro pasa banda entre 0.5 y 50 Hz, diseñado para eliminar tanto las frecuencias bajas asociadas a movimientos lentos o ruido de base, como las frecuencias altas, como el ruido de la red eléctrica. Como resultado, la señal se centra en el rango de frecuencias clave del ECG, lo que permite observar mejor las variaciones correspondientes a los latidos cardíacos. A lo largo de la gráfica, se distinguen los picos regulares de la señal cardíaca, que muestran un ritmo constante en su mayoría, lo cual es característico de los ciclos cardíacos en el ECG. Estos picos regulares, que probablemente corresponden a las ondas R, representan la actividad eléctrica del corazón en cada latido. La amplitud de la señal, que varía entre aproximadamente -75 mV y 75 mV, sugiere una señal más detallada y libre de ruido

Se muestra el codigo que se implemento para los filtros

```         
##################### FILTROS ##########################
# Definimos las frecuencias de corte para los filtros
lowcut = 0.5  # Frecuencia de corte baja en Hz (filtro pasa alto)
highcut = 50  # Frecuencia de corte alta en Hz (filtro pasa bajo)

# Eliminamos la media de la señal para centrarla en cero
ecg_signal = ecg_signal - np.mean(ecg_signal)

# Aplicamos un filtro pasa alto para eliminar frecuencias muy bajas
sos_high = signal.butter(2, lowcut, btype='highpass', fs=fs, output='sos')  # Filtro de Butterworth de orden 2
ecg_filtered_highpass = signal.sosfilt(sos_high, ecg_signal)  # Aplicamos el filtro a la señal

# Aplicamos un filtro pasa bajo para eliminar frecuencias muy altas
sos_low = signal.butter(2, highcut, btype='lowpass', fs=fs, output='sos')  # Filtro de Butterworth de orden 2
ecg_filtered_lowpass = signal.sosfilt(sos_low, ecg_signal)  # Aplicamos el filtro a la señal

# Aplicamos un filtro pasa banda para conservar solo el rango de 0.5 a 50 Hz
sos_band = signal.butter(2, [lowcut, highcut], btype='bandpass', fs=fs, output='sos')  # Filtro de Butterworth de orden 2
ecg_filtered_bandpass = signal.sosfilt(sos_band, ecg_signal)  # Aplicamos el filtro a la señal


# Gráfica de la señal filtrada con el filtro pasa alto
plt.figure(figsize=(18, 12))
plt.subplot(4, 1, 2)
plt.plot(ecg_filtered_highpass, label='Señal filtrada - Pasa alto (0.5 Hz)', color='green')
plt.title('Señal ECG filtrada - Pasa alto (corte: 0.5 Hz)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud (mV)')
plt.grid(True)
plt.legend()

# Gráfica de la señal filtrada con el filtro pasa bajo
plt.figure(figsize=(18, 12))
plt.subplot(4, 1, 3)
plt.plot(ecg_filtered_lowpass, label='Señal filtrada - Pasa bajo (50 Hz)', color='purple')
plt.title('Señal ECG filtrada - Pasa bajo (corte: 50 Hz)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud (mV)')
plt.grid(True)
plt.legend()

# Gráfica de la señal filtrada con el filtro pasa banda
plt.figure(figsize=(18, 12))
plt.subplot(4, 1, 4)
plt.plot(ecg_filtered_bandpass, label='Señal filtrada - Pasa banda (0.5 - 50 Hz)', color='red')
plt.title('Señal ECG filtrada - Pasa banda (0.5 - 50 Hz)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud (mV)')
plt.grid(True)
plt.legend()

plt.tight_layout()  # Ajusta el espacio entre las gráficas
plt.show()  # Muestra todas las gráficas

# Aplanamos el array de la señal filtrada con pasa banda
ecg_filtered_bandpass = np.ravel(ecg_filtered_bandpass)
```

## ***Picos R***

6.La identificación de los picos R en una señal de ECG es un paso fundamental para analizar la actividad cardíaca, ya que estos representan el punto de máxima amplitud en cada ciclo del corazón y corresponden a la despolarización de los ventrículos. Al localizar los picos R en una señal de ECG filtrada, es posible calcular los intervalos R-R, que son los periodos de tiempo entre latidos consecutivos. Estos intervalos son claves para evaluar la frecuencia cardíaca y analizar la variabilidad del ritmo, factores importantes para diagnosticar y monitorear diversas condiciones cardíacas. En este laboratorio, se propone identificar automáticamente los picos R y calcular los intervalos R-R mediante la función find_peaks para obtener una representación precisa de la dinámica del ritmo cardíaco.

![GRAFICA PICOS R](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/se%C3%B1al%20picos.png)

La gráfica presenta una señal ECG filtrada en azul y los picos R identificados como puntos rojos. Estos picos R son los puntos de máxima amplitud de cada ciclo cardíaco y representan la despolarización ventricular. La identificación de estos picos es clave para medir los intervalos RR, que son los tiempos entre latidos consecutivos y permiten calcular la frecuencia.

La distribución y consistencia de estos picos proporciona información importante sobre el ritmo cardíaco del individuo. En una señal ECG normal y estable, los picos R deben aparecer de forma regular y espaciada uniformemente, lo que indicaría un ritmo cardíaco constante y sin irregularidades. En la gráfica observada, los picos R parecen estar distribuidos de manera bastante uniforme, lo que sugiere un ritmo cardíaco relativomen

Además, algunos picos R en la gráfica presentan amplitudes mayores o menores, lo que podría ser indicativo de variaciones naturales en el latido cardíaco o, en algunos casos, de artefactos o ruido en la señal

Se calcularon los intervalos R-R mediante la funcion find_peaks

![CALCULO DE LOS INTERVALOS R-R](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/intervalor-r.png)

Los intervalos R-R representan el tiempo entre dos picos R consecutivos en un ECG, medido en milisegundos (ms). Este tiempo es esencial para calcular la frecuencia cardíaca, ya que el intervalo inversamente corresponde al ritmo del corazón en latidos por minuto (bpm). Valores de intervalo R-R en reposo típicamente oscilan entre 600 y 1200 ms, lo que corresponde a una frecuencia cardíaca de 50 a 100 bpm.

los intervalos R-R encontrados varían entre aproximadamente 150 ms y 300 ms, valores significativamente más bajos que los esperados para una señal en reposo. Este rango sugiere que podrían existir artefactos o que aún hay picos falsos detectados como picos R, posiblemente debido a ruido residual en la señal.

-   El codigo que se utilizo fue el siguiente

```         
############################# DETECCIÓN DE PICOS R ########################

# Detectamos los picos R en la señal filtrada usando find_peaks
picos_R, _ = find_peaks(ecg_filtered_bandpass, height=0.02, distance=150)  # Ajustar height y distance según la señal

# Gráfica de la señal con los picos R identificados
plt.figure(figsize=(28, 4))
plt.plot(ecg_filtered_bandpass, label='Señal ECG Filtrada')
plt.plot(picos_R, ecg_filtered_bandpass[picos_R], 'ro', label='Picos R')
plt.title('Detección de Picos R en la Señal ECG')
plt.xlabel('Muestras')
plt.ylabel('Amplitud (mV)')
plt.grid(True)
plt.legend()
plt.show()

# Calculamos los intervalos R-R en milisegundos
intervalos_RR = np.diff(picos_R) / fs * 1000  # Intervalos R-R en milisegundos

# Mostramos los intervalos R-R calculados
print("Intervalos R-R (en ms):", intervalos_RR)
```

#### **7Análisis de la HRV en el dominio del tiempo**

-   En el análisis de señales de electrocardiografía (ECG), la visualización de los datos puede resultar extensa y compleja debido a la continuidad de la señal en el tiempo. Para mejorar la interpretación y hacer más manejable la visualización, se ha implementado un esquema de ventaneamiento en el cual la gráfica se divide en seis ventanas. Esta división permite observar segmentos específicos de la señal ECG en intervalos definidos, facilitando la identificación de patrones cardíacos y minimizando la superposición visual que podría complicar el análisis. Este método de segmentación es particularmente útil para un estudio detallado de los ciclos cardíacos, preservando la continuidad de la señal mientras permite un enfoque en secciones clave para una interpretación más precisa.

    Se ha escogido un ventaneamiento rectangular para dividir la señal, ya que es el método más simple y directo, permitiendo analizar cada sección de la señal tal como fue capturada. Al no aplicar ninguna ponderación, este tipo de ventana mantiene la forma y amplitud original de las ondas características del ECG, sin introducir efectos de suavizado o distorsión que podrían alterar la percepción de las contracciones y relajaciones cardíacas. Esto hace que el ventaneamiento rectangular sea ideal para estudiar patrones específicos en la señal.

![GRAFICA CON VENTANEAMIENTO RECTANGULAR](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/PICOS%20R.png)

En este análisis, se calculan los parámetros básicos de la variabilidad de la frecuencia cardíaca (HRV) y se examinan críticamente utilizando técnicas estadísticas adecuadas para interpretar las fluctuaciones en el ritmo cardíaco. La HRV es un indicador importante de la actividad del sistema nervioso autónomo y ofrece información sobre el equilibrio entre el sistema simpático y el parasimpático. Para mejorar la claridad y precisión en la visualización de la señal ECG, se aplica un ventaneo rectangular en seis ventanas de duración específica, lo cual permite segmentar la señal y observar las características de la HRV en intervalos discretos. Este enfoque facilita la detección de patrones y la reducción de ruido, permitiendo un análisis más detallado de la señal en cada segmento. Al aplicar técnicas estadísticas a cada ventana, se puede evaluar la variabilidad de la HRV en distintos intervalos, proporcionando una perspectiva más completa sobre la estabilidad del ritmo cardíaco y su comportamiento en el tiempo.

> > #### ***VENTANA 1***
> >
> > La gráfica de la ventana 1 muestra una porción de la señal ECG con los picos R marcados en rojo, indicando los puntos donde se detectaron latidos cardíacos. Visualmente, los picos R parecen estar distribuidos de manera regular, lo que es un buen indicador de estabilidad en el ritmo cardíaco durante esta ventana específica. La amplitud de la señal oscila entre aproximadamente -20 mV y 40 mV, con picos claros que ayudan en la detección de los intervalos R-R.

![VENTANA 1](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/ventana1.png)

![PARAMETROS BASICOS VENTANA 1]((https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/parametros%20basicos1.png))

> > 1.  ***Media RR:***  el valor del RR media es de 734,09 ms corresponde a una frecuencia cardiaca de aproximadamente 82 latidos por minuto, es valor es más típico en un estado de reposo o actividad ligera
> >
> > 2.  ***SDNN (desviación estándar RR)***: esta variable nos indica la variabilidad total de la frecuencia cardiaca, un valor de 184,15 ms, es bastante alto, lo cual es positivo y generalmente se asocia con una buena salud cardiovascular y una alta capacidad de adaptación del sistema nervioso autónomo.
> >
> > 3.  ***RMSSD***: mide las variaciones en intervalos RR consecutivos y es un indicador de la actividad parasimpática a corto plazo, el valor de 258, 04 ms es considerablemente alto, lo que sugiere una fuerte influencia parasimpática y una alta capacidad de relajación y recuperación del organismo; lo que también nos indica un tono vagal saludable y una capacidad de adaptación rápida del sistema cardíaco.
> >
> > 4.  ***NN50 y pNN50:***  el NN50 cuanta el numero de intervalos consecutivos de RR que difieren en más de 50 ms, mientras que pNN50 es el porcentaje de esos intervalos respecto al total. Un pNN50 de 72.73% indica que más del 70% de los intervalos RR tienen variaciones significativas de al menos 50 ms. Esto es muy alto y es un buen indicador de alta variabilidad cardíaca. Los valores altos de pNN50 sugieren una fuerte influencia parasimpática, lo cual es favorable para la salud cardiovascular y sugiere una gran capacidad del cuerpo para responder a cambios en el entorno.
> >
> > 5.  ***SDSD :*** mide la desviación estándar de las diferencias entre intervalos RR sucesivos, y al igual que RMSSD, es un indicador de la actividad parasimpática a corto plazo. Un valor de 257,95 ms es alto, lo cual confirma el análisis del RMSSD y sugiere una actividad vagal significativa (parasimpática), que contribuye a la recuperación y relajación del sistema cardiovascular .

> > #### ***VENTANA 2***

> > En la gráfica de la ventana 2 de la señal ECG, se observan los picos R marcados en rojo sobre la señal, que tiene una amplitud oscilando entre -10 mV y aproximadamente 25 mV. La regularidad de los picos R sugiere estabilidad en el ritmo cardíaco, aunque se pueden apreciar ciertas variaciones en las amplitudes y en la distancia entre los picos, lo que refleja la variabilidad de la frecuencia cardíaca

![VENTANA 2](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/ventana2.png
)

![PARAMETROS BASICOS VENTANA 2](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/parametros%20basicos2.png
)

> > 1.  ***MEDIA RR :*** La Media RR representa el intervalo promedio entre picos R, y un valor de 624,74 ms corresponde a una frecuencia cardíaca aproximada de 96 rpm (latidos por minuto). Esto es un poco elevado para una persona en reposo, pero puede ser normal en situaciones de actividad ligera o bajo un nivel de estrés. Esta frecuencia cardíaca es común y no es indicativa de problemas, aunque está en el rango superior de reposo.
> >
> > 2.  ***SDNN:***  es una medida de la variabilidad total de la frecuencia cardíaca y refleja tanto la actividad simpática como la parasimpática. Un valor de 127,30 ms es bastante alto, lo que generalmente es positivo e indica una alta variabilidad en la frecuencia cardíaca. Esto sugiere una buena capacidad de adaptación del sistema autónomo. Los valores altos de SDNN suelen estar asociados con una buena salud cardiovascular, reflejando una capacidad adecuada para responder a cambios en el entorno.
> >
> > 3.  ***RMSSD:*** mide las variaciones en intervalos RR sucesivos, y es un indicador de la actividad parasimpática a corto plazo. Un valor de 194,72 ms es elevado y sugiere una fuerte influencia parasimpática en la frecuencia cardíaca, lo que indica que el sistema nervioso autónomo está en un estado de relajación o recuperación. Este valor es muy positivo y sugiere una buena capacidad de recuperación y respuesta vagal (parasimpática).
> >
> > 4.  ***NN50 y pNN50:***  el NN50 cuenta el número de intervalos consecutivos de RR que difieren en más de 50 ms, y pNN50 es el porcentaje correspondiente. Un pNN50 de 69.23% indica que aproximadamente el 70% de los intervalos RR tienen una variación significativa entre ellos, lo cual es un signo de alta variabilidad cardíaca.
> >
> > 5.  ***SDSD:*** el SDSD mide la desviación estándar de las diferencias entre intervalos RR sucesivos, y al igual que RMSSD, es un indicador de la actividad parasimpática. Un valor de 194,16 ms confirma la alta variabilidad a corto plazo y la fuerte actividad parasimpática observada con RMSSD, lo cual sugiere que el sistema cardiovascular tiene una buena capacidad de adaptación y recuperación

> > ***VENTANA 3***

> > En la gráfica de la ventana 3 de la señal ECG, se observa un trazado de la señal con picos R marcados en rojo, que permiten identificar las contracciones cardíacas. A diferencia de las ventanas anteriores, esta gráfica muestra algunas irregularidades, como picos más altos y profundos alrededor de las muestras 1000 y 4000, que podrían ser artefactos o interferencias en la señal. La amplitud de la señal varía entre aproximadamente -60 mV y 60 mV, lo cual es inusual y sugiere que podría haber algún ruido o alteración que no fue completamente eliminado en el filtrado

![VENTANA 3](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/ventana3.png)

![PARAMETROS BASICOS VENTANA 3](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/parametros%20basicos3.png
)

> > 1.  ***MEDIA RR:*** Un intervalo RR de 642,67 ms equivale a una frecuencia cardíaca de aproximadamente 93 rpm (latidos por minuto). Esta frecuencia cardíaca es algo elevada lo que sugiere que la persona tuvo alguna preocupación, pero en términos generales, es una frecuencia cardíaca aceptable.
> >
> > 2.  ***SDNN:*** Un valor de 127,72 ms indica una variabilidad moderada a alta, lo cual generalmente se asocia con una buena capacidad de adaptación del sistema nervioso autónomo. Los valores altos de SDNN son positivos y suelen estar relacionados con una buena salud cardiovascular, ya que reflejan la capacidad del sistema autónomo para responder a cambios internos y externos.
> >
> > 3.  ***RMSSD:*** Un valor de 209,39 ms es elevado y sugiere una fuerte influencia parasimpática. Esto indica una buena capacidad de recuperación y respuesta vagal. En un contexto de reposo o relajación, un RMSSD alto refleja un tono parasimpático saludable.
> >
> > 4.  ***NN50 y Pnn50:*** Un pNN50 de 64% indica que el 64% de los intervalos RR tienen variaciones significativas entre ellos, lo cual es un signo de alta variabilidad en la frecuencia cardíaca.
> >
> > 5.  ***SDSD:*** mide la desviación estándar de las diferencias entre intervalos RR sucesivos, y al igual que RMSSD, es un indicador de la variabilidad a corto plazo y de la actividad parasimpática. Un valor de 209,38 ms confirma el alto RMSSD.

> > #### ***VENTANA 4***

> > En la gráfica de la ventana 4 de la señal ECG, se observa la señal cardíaca con picos R marcados en rojo, indicando los momentos de contracción ventricular. La señal oscila entre aproximadamente -20 mV y 30 mV, lo cual parece estar dentro de un rango más estable en comparación con otras ventanas. Los picos R están claramente identificados, aunque se notan ciertas variaciones en la amplitud, posiblemente debido a la respiración u otros factores fisiológicos

![VENTANA 4](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/ventana4.png
)

![PARAMETROS BASICOS VENTANA 4](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/parametros%20basicos4.png)

> > 1.  ***MEDIA RR :*** La Media RR de 640 ms corresponde a una frecuencia cardíaca de aproximadamente 93,75 rpm. Este valor es muy similar a los de las ventanas anteriores (aproximadamente entre 90 y 96 rpm), lo cual sugiere una frecuencia cardíaca estable a lo largo del período analizado. Una frecuencia cardíaca en este rango podría estar ligeramente elevada para reposo, pero si es consistente en todas las ventanas, es indicativo de una actividad simpática moderada o un estado de alerta bajo.
> >
> > 2.  ***SDNN***: La SDNN en esta ventana es de 146.54 ms, que es un valor elevado y representa una variabilidad total de la frecuencia cardíaca alta. Comparando este valor con las otras ventanas, vemos que SDNN ha sido consistentemente alto en todos los segmentos, lo cual sugiere una alta variabilidad de largo plazo. Esto puede ser un indicativo de buena salud cardiovascular y de una regulación autonómica adecuada.
> >
> > 3.  ***RMSSD:*** El RMSSD en esta ventana es también alto, a 206,93 ms, lo cual representa una fuerte influencia parasimpática y alta variabilidad a corto plazo. Este valor es coherente con las ventanas anteriores, donde RMSSD también se ha mantenido en niveles altos. Esto indica que la persona tiene un buen tono vagal y una alta capacidad de recuperación, lo cual es positivo para la salud cardíaca y la capacidad de adaptación.
> >
> > 4.  ***NN50 y pNN50:*** NN50 y pNN50 indican el número y porcentaje de intervalos RR sucesivos que difieren en más de 50 ms. En esta ventana, pNN50 es 65.38%, lo cual sugiere que más del 65% de los intervalos RR tienen variaciones significativas. Este valor es consistente con las de las ventanas anteriores y confirma la alta variabilidad de la frecuencia cardíaca, en particular la influencia del sistema parasimpático, lo cual es positivo y se asocia con un buen tono vagal.
> >
> > 5.  ***SDSD:*** SDSD es igual al RMSSD en esta ventana, a 206,93 ms, lo cual es una medida adicional de la variabilidad a corto plazo y del tono parasimpático. Al igual que en las otras ventanas, este alto valor de SDSD confirma una buena variabilidad a corto plazo, compatible con una actividad parasimpática significativa.

> > #### ***VENTANA 5***

> > En la gráfica de la señal ECG en la ventana 5, se observa una serie de picos R marcados en rojo que sobresalen de una señal de fondo con oscilaciones de menor amplitud. La amplitud de estos picos alcanza aproximadamente los 30 mV, mientras que el resto de la señal varía entre -20 mV y 20 mV, lo cual es característico de una señal ECG adecuada y bien capturada. Los picos R están regularmente espaciados, lo que sugiere un ritmo cardíaco estable sin grandes fluctuaciones. Esta regularidad es clave para calcular intervalos R-R precisos, ya que indica que el proceso de filtrado ha sido efectivo para reducir ruido sin alterar la forma de la onda cardíaca

![VENTANA 5](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/ventana5.png
)

![PARAMETROS BASICOS VENTANA 5](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/parametros%20basicos5.png
)

> > 1.  ***MEDIA RR:*** Con una Media RR de 668.89 ms, la frecuencia cardíaca es de aproximadamente 89.7 rpm , lo cual es ligeramente menor que en las ventanas anteriores pero sigue en el mismo rango de actividad ligera o alerta. SDNN: es un indicador de la variabilidad total de la frecuencia cardíaca, y un valor de 147,94 ms sigue reflejando una alta variabilidad. Este valor es similar a los SDNN de las ventanas anteriores, lo cual indica una estabilidad de la variabilidad cardíaca a largo plazo en esta señal.
> >
> > 2.  ***SDNN:*** es un indicador de la variabilidad total de la frecuencia cardíaca, y un valor de 147,94 ms sigue reflejando una alta variabilidad. Este valor es similar a los SDNN de las ventanas anteriores, lo cual indica una estabilidad de la variabilidad cardíaca a largo plazo en esta señal
> >
> > 3.  ***RMSSD:*** mide la variabilidad a corto plazo y es un indicador de la actividad parasimpática. Un valor de 200,88 ms es elevado, reflejando una alta influencia del sistema parasimpático. Este valor sigue en el mismo rango que las otras ventanas, lo que sugiere que el tono parasimpático (vagal) permanece constante en la señal y que la persona está en un estado de relajación o con buena recuperación vagal.
> >
> > 4.  ***NN50 y pNN50:*** Un pNN50 de 58.33% indica que el 58% de los intervalos RR tienen variaciones significativas. Aunque es ligeramente más bajo que en algunas de las ventanas anteriores, sigue siendo un valor alto que sugiere una buena variabilidad cardíaca. La influencia parasimpática es evidente aquí, ya que un pNN50 alto se relaciona con un buen tono vagal y una salud cardiovascular estable.
> >
> > 5.  ***SDSD:*** es la desviación estándar de las diferencias entre intervalos RR sucesivos y, al igual que RMSSD, refleja la actividad parasimpática. Un SDSD de 200,40 ms indica alta variabilidad a corto plazo, lo cual es consistente con una buena regulación parasimpática y apoya los hallazgos de RMSSD y pNN50

> > #### ***VENTANA 6***

> > En la gráfica de la señal ECG en la ventana 6, observamos la representación de la señal cardíaca con los picos R identificados en rojo, que corresponden a cada latido del corazón. A primera vista, la señal parece estar bien capturada, con un rango de amplitud que se extiende desde aproximadamente -25 mV hasta 25 mV, con un pico atípico que alcanza los 75 mV alrededor de la muestra 3000. Este pico anómalo podría ser un artefacto o ruido inesperado en la señal,

![VENTANA 6](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/ventana6.png)

![PARAMETROS BASICOS VENTANA 6](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/parametros%20basicos6.png)

> > 1.  ***MEDIA RR:*** La Media RR de 657,73 ms representa frecuencia cardiaca de aproximadamente 91 rpm (latidos por minuto). Este valor es coherente con las ventanas anteriores, mostrando una frecuencia cardíaca levemente elevada pero estable, lo que podría reflejar un estado de actividad ligera o alerta moderada.
> >
> > 2.  ***SDNN:*** es un indicador de la variabilidad total de la frecuencia cardíaca y sigue siendo alto en esta ventana, a 140,31 ms. Un SDNN alto en todas las ventanas es un buen indicio de la capacidad del sistema cardiovascular para mantener la variabilidad en el tiempo, reflejando buena salud cardiovascular y una capacidad de adaptación a cambios.
> >
> > 3.  ***RMSSD:*** Con un valor de 211,10 ms, RMSSD es alto, lo cual refleja una fuerte influencia del sistema nervioso parasimpático (vagal) y una capacidad de recuperación rápida. Este valor también es consistente con las ventanas previas, lo que indica una influencia parasimpática continua en la señal y un buen tono vagal.
> >
> > 4.  ***NN50 y pNN50:*** Un pNN50 de 76% es bastante elevado, indicando que más del 75% de los intervalos tienen diferencias significativas, lo cual es un signo de alta variabilidad y buena salud cardiovascular. Este valor es el más alto en las ventanas que ha presentado, sugiriendo una influencia parasimpática muy marcada en esta ventana, lo cual podría indicar una fase de relajación o recuperación.
> >
> > 5.  ***SDSD:*** es la desviación estándar de las diferencias entre intervalos RR consecutivos y, como RMSSD, indica la variabilidad a corto plazo. Con 211.08 ms, SDSD sigue siendo alto, consistente con los valores de RMSSD y pNN50, confirmando la actividad parasimpática predominante.
> >
> > En conclusión, estos datos de HRV en todas las ventanas reflejan una señal saludable y estable, con un buen equilibrio autónomo y una alta variabilidad que indica un sistema cardiovascular adaptable y en buen estado.

-El codigo que se utilizo fue el siguiente

```         

#################################VENTANEAMIENTO RECTANGULAR #######################

# Definimos el tamaño de la ventana y el número total de ventanas
ventana_muestras = 5000  # Tamaño de cada ventana en muestras
num_ventanas = len(ecg_filtered_bandpass) // ventana_muestras  # Número de ventanas
colores = plt.cm.tab10.colors  # Colores para las ventanas en la gráfica

# Diccionario para almacenar los resultados del análisis de HRV por ventana
hrv_results = []

# Gráfica completa de la señal con ventanas coloreadas
plt.figure(figsize=(18, 6))
for i in range(num_ventanas):
    inicio = i * ventana_muestras  # Índice de inicio de la ventana
    fin = (i + 1) * ventana_muestras  # Índice final de la ventana
    color = colores[i % len(colores)]  # Color de la ventana basado en el índice
    plt.plot(range(inicio, fin), ecg_filtered_bandpass[inicio:fin], label=f'Ventana {i+1}', color=color)
plt.title('Señal ECG Completa con Ventanas')
plt.xlabel('Muestras')
plt.ylabel('Amplitud (mV)')
plt.legend()
plt.grid(True)
plt.show()
#############################################ANALISIS HRV POR VENTANA ##########################

for i in range(num_ventanas):
    inicio = i * ventana_muestras  # Índice de inicio de la ventana
    fin = (i + 1) * ventana_muestras  # Índice final de la ventana
    ventana = ecg_filtered_bandpass[inicio:fin]  # Segmento de la señal de la ventana actual
    
    # Detectar los picos R en la ventana
    picos_R, _ = find_peaks(ventana, height=0.02, distance=150)
    
    # Calcular los intervalos R-R en milisegundos
    intervalos_RR = np.diff(picos_R) / fs * 1000
    
    # Calcular parámetros de HRV si hay intervalos R-R
    if len(intervalos_RR) > 0:
        media_RR = np.mean(intervalos_RR)  # Media de los intervalos R-R
        std_RR = np.std(intervalos_RR)  # Desviación estándar de los intervalos R-R
        rmssd = np.sqrt(np.mean(np.square(np.diff(intervalos_RR))))  # RMSSD
        nn50 = np.sum(np.abs(np.diff(intervalos_RR)) > 50)  # NN50: cantidad de intervalos con cambio >50ms
        pnn50 = nn50 / len(intervalos_RR) * 100  # pNN50: porcentaje de NN50
        sdsd = np.std(np.diff(intervalos_RR))  # SDSD: desviación estándar de las diferencias sucesivas
        
        # Almacenar resultados de HRV
        hrv_results.append({
            'Ventana': i + 1,
            'Media RR (ms)': media_RR,
            'STD RR (ms)': std_RR,
            'RMSSD (ms)': rmssd,
            'NN50': nn50,
            'pNN50 (%)': pnn50,
            'SDSD (ms)': sdsd
        })

        # Gráfica de la ventana con picos R y color consistente
        plt.figure(figsize=(10, 4))
        plt.plot(ventana, label=f'Ventana {i+1}', color=colores[i % len(colores)])  # Asignación del mismo color
        plt.plot(picos_R, ventana[picos_R], 'ro', label='Picos R')
        plt.title(f'Señal ECG en Ventana {i+1} con Picos R')
        plt.xlabel('Muestras')
        plt.ylabel('Amplitud (mV)')
        plt.grid(True)
        plt.legend()
        plt.show()

# Imprimir los resultados de HRV para cada ventana
for resultado in hrv_results:
    print(f"Ventana {resultado['Ventana']}:")
    print(f" - Media RR = {resultado['Media RR (ms)']:.2f} ms")
    print(f" - STD RR = {resultado['STD RR (ms)']:.2f} ms")
    print(f" - RMSSD = {resultado['RMSSD (ms)']:.2f} ms")
    print(f" - NN50 = {resultado['NN50']}")
    print(f" - pNN50 = {resultado['pNN50 (%)']:.2f} %")
    print(f" - SDSD = {resultado['SDSD (ms)']:.2f} ms")
```

> > ### *APLICACIÓN DE LA TRANSFORMADA WAVELET MORLET CONTINUA PARA ECG*

La wavelet Morlet es una función compleja de tipo sinusoidal modulada por una envolvente gaussiana. Esto permite un análisis en frecuencia muy preciso, ideal para la representación de señales en el dominio de tiempo-frecuencia, como en el espectrograma de HRV. La Morlet es particularmente adecuada para la transformada wavelet continua (CWT) debido a su alta resolución en frecuencia, lo cual facilita la identificación de componentes de frecuencia en la señal HRV, además la señal fisiológica proporcionada del AD8232, es una señal continua y por ende la wavelet Daubechies esta en el dominio discreto impidiendo procesar señales continuas.

![ESPECTOGRAMA DE HVR USANDO TRANSFORMADA WAVELET5 CONTINUA(MORLET)](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/espectograma.png)

Este espectrograma de HRV muestra la variación de la amplitud en diferentes frecuencias de la señal HRV a lo largo del tiempo, obtenida mediante la transformada wavelet continua (CWT) con la wavelet Morlet. La amplitud de la CWT está codificada en colores, donde los colores más cálidos (amarillo, naranja y rojo) representan amplitudes mayores, mientras que los colores fríos (azul) representan amplitudes menores.

> > -   ***Variación en la Banda HF (0,15 - 0,4 Hz) :*** la banda HF muestra variaciones significativas, especialmente en la parte superior de la gráfica (aproximadamente entre 0,2 y 0,35 Hz). Las regiones de mayor amplitud (naranja a rojo) en esta banda pueden indicar fluctuaciones en la actividad parasimpática, posiblemente relacionadas con la respiración. Estas variaciones en HF pueden representar momentos en los que el sistema parasimpático está más activo, ayudando en la regulación del ritmo cardíaco. Este patrón sugiere que la persona podría estar en un estado donde la regulación respiratoria o relajación tiene una influencia notable en la VFC
> >
> > <!-- -->
> >
> > -   ***Variación en la Banda LF (0,04 - 0,15 Hz):*** La banda LF muestra áreas con menor intensidad, principalmente en colores amarillos, lo cual indica moderada presencia de actividad en la banda de baja frecuencia. La banda LF se asocia con la actividad simpática y el control a largo plazo de la frecuencia cardíaca, que puede incluir la regulación de la presión arterial y la respuesta al estrés. La menor amplitud en la banda LF en comparación con HF puede sugerir que, en este momento, la señal HRV está más influenciada por el sistema parasimpático que por el simpático, lo cual es común en condiciones de relajación o en estado basal.
> > -   ***Cambios Temporales en la Amplitud***: A lo largo del tiempo, se observa que la amplitud en ambas bandas cambia, aunque la banda HF tiene mayor intensidad de forma más frecuente. Esto sugiere que hay un equilibrio dinámico entre los sistemas simpático y parasimpático. En algunos momentos, el sistema parasimpático puede estar predominante (cuando la banda HF tiene mayor intensidad), mientras que, en otros momentos, la actividad simpática también contribuye (cuando hay amplitud en LF). Este espectrograma muestra que la banda de alta frecuencia (HF) tiene una mayor amplitud en varios momentos, lo cual indica una mayor influencia del sistema parasimpático. Esto es típico de estados de relajación o de actividad ligera, donde la variabilidad a corto plazo (regulada por el sistema parasimpático) es más prominente. La presencia de la banda LF en menor intensidad sugiere que el sistema simpático también está activo, pero con menor influencia que el parasimpático en esta señal HRV.

> > #### ***POTENCIA EN BANDAS DE BAJA Y ALTA FRECUENCIA***

![POTENCIA EN BANDAS DE BAJA Y AKTA FRECUENCIA )](https://github.com/a2002valiente/lab4-Variabilidad-de-la-Frecuencia-Cardiaca-usando-la-Transformada-Wavelet/blob/main/imagenes/potencia.png)

-   ***Potencias en LF (frecuencia baja)***: Representan la actividad simpática, que puede estar más constante y reflejar el estado basal del individuo. -Potencias en HF (frecuencia alta) : Muestran los efectos de la regulación parasimpática, como la respiración o relajación, y parecen tener episodios de aumento en el espectrograma.

> > 1.  ***Análisis de la Banda de Baja Frecuencia (LF) - Línea Azul:***

-   ***Incremento de Potencia en LF*** : Observamos que la potencia en la banda LF aumenta de manera significativa desde el inicio del registro, alcanzando un máximo alrededor de los 2.5 segundos y luego disminuyendo gradualmente. Este patrón sugiere una activación del sistema nervioso simpático, que generalmente se asocia con una respuesta al estrés o al esfuerzo. En contextos clínicos, un aumento en la potencia en LF puede indicar una regulación a largo plazo de la frecuencia cardíaca debido a la respuesta autónoma.

-    ***Forma de la curva:*** La forma de campana en la potencia de LF sugiere que la actividad simpática tiene un episodio de activación que alcanza su punto máximo y luego regresa a niveles más bajos. Esto podría ser el resultado de un cambio temporal en el sistema cardiovascular, como una transición entre estados de reposo y un evento estresante, seguido de un retorno a un estado basal.

> > ***2.Análisis de la Banda de Alta Frecuencia (HF) - Línea Roja***

-   ***Baja Potencia en HF:*** La potencia en la banda HF permanece relativamente baja y constante durante el tiempo observado, con un leve aumento en torno a los 2 segundos, pero sin cambios significativos. La banda HF está asociada con la actividad parasimpática y la regulación respiratoria. Un bajo nivel en esta banda indica una menor influencia del sistema parasimpático durante este período, lo cual sugiere que el control autónomo está dominado por el sistema simpático.

-   ***Interpretación del Bajo Nivel en HF:*** En circunstancias normales, un aumento en la potencia en la banda HF podría indicar actividad de relajación o influencia de la respiración profunda en la regulación cardíaca. Sin embargo, en este caso, el nivel de HF es bajo en comparación con LF, lo cual puede indicar que la señal HRV está siendo menos influenciada por la respiración o la actividad parasimpática y más por factores simpáticos.

En conclusión La gráfica indica un episodio en el que el sistema simpático domina la regulación de la HRV, con un pico de actividad alrededor de los 2.5 segundos, seguido de un retorno gradual a niveles bajos de potencia en LF. La poca actividad en HF sugiere una baja influencia del sistema parasimpático en la regulación de la frecuencia cardíaca en este período, lo cual podría estar asociado con un estado de alerta o nivel de estrés.

-   Se muestra acontinuación el codigo que se implemento

```         
intervalos_RR_s = intervalos_RR / 1000  # Convertir a segundos
tiempo_rr = np.cumsum(intervalos_RR_s)  # Tiempos acumulados de los intervalos R-R

# Definir una frecuencia de muestreo para la señal de HRV interpolada (por ejemplo, 4 Hz)
fs_hrv = 4  # Frecuencia de muestreo de la señal HRV en Hz

# Interpolamos los intervalos R-R para obtener una señal de HRV continua
tiempo_hrv = np.arange(0, tiempo_rr[-1], 1/fs_hrv)  # Eje temporal de la señal de HRV
hrv_signal = np.interp(tiempo_hrv, tiempo_rr, intervalos_RR_s)  # Señal HRV interpolada

# Parámetros para la CWT
wavelet = 'morl'  # Usamos la wavelet Morlet en lugar de Daubechies
scales = np.arange(1, 128)  # Definimos las escalas para la CWT, ajustar según sea necesario

# Aplicamos la CWT a la señal de HRV
coefficients, frequencies = pywt.cwt(hrv_signal, scales, wavelet, 1/fs_hrv)

# Visualización del espectrograma
plt.figure(figsize=(10, 6))
plt.imshow(np.abs(coefficients), extent=[0, tiempo_hrv[-1], frequencies[-1], frequencies[0]], aspect='auto', cmap='jet')
plt.colorbar(label='Amplitud de la CWT')
plt.ylim(0.04, 0.4)  # Limitar el rango de frecuencias de interés en HRV (0.04 - 0.4 Hz)
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.title('Espectrograma de HRV usando Transformada Wavelet Continua (Morlet)')
plt.show()

# Convertimos intervalos_RR a segundos y calculamos los tiempos acumulativos
intervalos_RR_s = intervalos_RR / 1000  # Convertir a segundos
tiempo_rr = np.cumsum(intervalos_RR_s)  # Tiempos acumulados de los intervalos R-R

# Definir una frecuencia de muestreo para la señal de HRV interpolada (por ejemplo, 4 Hz)
fs_hrv = 4  # Frecuencia de muestreo de la señal HRV en Hz

# Interpolamos los intervalos R-R para obtener una señal de HRV continua
time_hrv = np.arange(0, tiempo_rr[-1], 1/fs_hrv)  # Eje temporal de la señal de HRV
hrv_signal = np.interp(time_hrv, tiempo_rr, intervalos_RR_s)  # Señal HRV interpolada

# Parámetros para la CWT
wavelet = 'morl'  # Usamos la wavelet Morlet en lugar de Daubechies
scales = np.arange(1, 128)  # Definimos las escalas para la CWT, ajustar según sea necesario

# Aplicamos la CWT a la señal de HRV
coefficients, frequencies = pywt.cwt(hrv_signal, scales, wavelet, 1/fs_hrv)

# Calcular la potencia en bandas LF (0.04 - 0.15 Hz) y HF (0.15 - 0.4 Hz)
lf_band = (frequencies >= 0.04) & (frequencies <= 0.15)  # Índices de la banda LF
hf_band = (frequencies >= 0.15) & (frequencies <= 0.4)   # Índices de la banda HF

# Potencia en la banda LF
lf_power = np.mean(np.abs(coefficients[lf_band, :])**2, axis=0)

# Potencia en la banda HF
hf_power = np.mean(np.abs(coefficients[hf_band, :])**2, axis=0)

# Graficar la potencia en las bandas LF y HF a lo largo del tiempo
plt.figure(figsize=(10, 5))
plt.plot(time_hrv, lf_power, label="Potencia en Banda LF (0.04 - 0.15 Hz)", color='blue')
plt.plot(time_hrv, hf_power, label="Potencia en Banda HF (0.15 - 0.4 Hz)", color='red')
plt.xlabel("Tiempo (s)")
plt.ylabel("Potencia")
plt.title("Potencia en Bandas de Baja Frecuencia (LF) y Alta Frecuencia (HF) en la HRV")
plt.legend()
plt.grid(True)
plt.show()
```
