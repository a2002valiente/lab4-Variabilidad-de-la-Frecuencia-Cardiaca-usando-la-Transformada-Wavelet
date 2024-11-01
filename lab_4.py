# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import find_peaks
import pywt
# Ruta completa donde se encuentra el archivo
file_path =  r'C:\Users\julis\OneDrive\Escritorio\LAB SEÑALES\ecg.txt'  # Cambia esto por la ruta de tu archivo

# Cargamos el archivo
ecg_data = np.loadtxt(file_path, delimiter=',')  # Lee los datos 


ecg_signal = ecg_data[:, 1]  # Suponiendo que la segunda columna es la que queremos
num_muestras = len(ecg_signal)



duracion= 300 # # Cambia esto por la duración real,Duración de la señal en segundos (para 147 muestras a 1000 Hz)
fs = 1000  # Frecuencia de muestreo en Hz
print(f"Número de muestras: {num_muestras}, Frecuencia de muestreo: {fs} Hz")


#######################################FILTROS###########################
# Frecuencias de corte para los filtros
lowcut = 0.5  # Frecuencia de corte baja en Hz (pasa alto)
highcut = 50  # Frecuencia de corte alta en Hz (pasa bajo)

# Eliminamos la media de la señal original para centrarla en cero
ecg_signal = ecg_signal - np.mean(ecg_signal)
# Filtro pasa alto (para eliminar componentes de muy baja frecuencia)
sos_high = signal.butter(2, lowcut, btype='highpass', fs=fs, output='sos')  # Orden reducido a 2
ecg_filtered_highpass = signal.sosfilt(sos_high, ecg_signal)

# Filtro pasa bajo (para eliminar componentes de alta frecuencia)
sos_low = signal.butter(2, highcut, btype='lowpass', fs=fs, output='sos')  # Orden reducido a 2
ecg_filtered_lowpass = signal.sosfilt(sos_low, ecg_signal)

# Filtro pasa banda (para dejar pasar solo el rango de 0.5 - 50 Hz)
sos_band = signal.butter(2, [lowcut, highcut], btype='bandpass', fs=fs, output='sos')  # Orden reducido a 2
ecg_filtered_bandpass = signal.sosfilt(sos_band, ecg_signal)



# Señal original
plt.figure(figsize=(18, 12))
plt.subplot(4, 1, 1)
plt.plot(ecg_signal, label='Señal original', color='blue')
plt.title('Señal ECG original en reposo')
plt.xlabel('Muestras')
plt.ylabel('Amplitud (mV)')
plt.grid(True)
plt.legend()

# Señal con el filtro pasa alto
plt.figure(figsize=(18, 12))
plt.subplot(4, 1, 2)
plt.plot(ecg_filtered_highpass, label='Señal filtrada - Pasa alto (0.5 Hz)', color='green')
plt.title('Señal ECG filtrada - Pasa alto (corte: 0.5 Hz)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud (mV)')
plt.grid(True)
plt.legend()

# Señal con el filtro pasa bajo
plt.figure(figsize=(18, 12))
plt.subplot(4, 1, 3)
plt.plot(ecg_filtered_lowpass, label='Señal filtrada - Pasa bajo (50 Hz)', color='purple')
plt.title('Señal ECG filtrada - Pasa bajo (corte: 50 Hz)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud (mV)')
plt.grid(True)
plt.legend()

# Señal con el filtro pasa banda
plt.figure(figsize=(18, 12))
plt.subplot(4, 1, 4)
plt.plot(ecg_filtered_bandpass, label='Señal filtrada - Pasa banda (0.5 - 50 Hz)', color='red')
plt.title('Señal ECG filtrada - Pasa banda (0.5 - 50 Hz)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud (mV)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

ecg_filtered_bandpass = np.ravel(ecg_filtered_bandpass)
#############################PICOS ########################

# Detectar los picos R utilizando find_peaks
# Puedes ajustar la altura y distancia mínimas según tu señal
picos_R, _ = find_peaks(ecg_filtered_bandpass, height=0.02, distance=150)  # Ajusta height y distance según tu señal

# Graficar la señal con los picos R identificados
plt.figure(figsize=(28, 4))
plt.plot(ecg_filtered_bandpass, label='Señal ECG Filtrada')
plt.plot(picos_R, ecg_filtered_bandpass[picos_R], 'ro', label='Picos R')
plt.title('Detección de Picos R en la Señal ECG')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.legend()
plt.show()

# Calcular los intervalos R-R en milisegundos (si conoces la frecuencia de muestreo)

intervalos_RR = np.diff(picos_R) / fs * 1000  # Intervalos en milisegundos

# Mostrar los intervalos R-R calculados
print("Intervalos R-R (en ms):", intervalos_RR)



####ventaneamiento #####
ventana_muestras = 5000
num_ventanas = len(ecg_filtered_bandpass) // ventana_muestras
colores = plt.cm.tab10.colors

# Diccionario para almacenar los resultados de HRV
hrv_results = []

# Gráfica completa de la señal con ventanas coloreadas
plt.figure(figsize=(18, 6))
for i in range(num_ventanas):
    inicio = i * ventana_muestras
    fin = (i + 1) * ventana_muestras
    color = colores[i % len(colores)]
    plt.plot(range(inicio, fin), ecg_filtered_bandpass[inicio:fin], label=f'Ventana {i+1}', color=color)
plt.title('Señal ECG Completa con Ventanas')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.show()

# Análisis HRV por ventana y graficado individual
for i in range(num_ventanas):
    inicio = i * ventana_muestras
    fin = (i + 1) * ventana_muestras
    ventana = ecg_filtered_bandpass[inicio:fin]
    
    # Detectar los picos R en la ventana
    picos_R, _ = find_peaks(ventana, height=0.02, distance=150)
    
    # Calcular los intervalos R-R en milisegundos
    intervalos_RR = np.diff(picos_R) / fs * 1000
    
    # Calcular los parámetros de HRV
    if len(intervalos_RR) > 0:
        media_RR = np.mean(intervalos_RR)
        std_RR = np.std(intervalos_RR)
        rmssd = np.sqrt(np.mean(np.square(np.diff(intervalos_RR))))
        nn50 = np.sum(np.abs(np.diff(intervalos_RR)) > 50)
        pnn50 = (nn50 / len(intervalos_RR)) * 100
        sdsd = np.std(np.diff(intervalos_RR))
    else:
        media_RR = std_RR = rmssd = nn50 = pnn50 = sdsd = np.nan
    
    # Guardamos los resultados
    hrv_results.append({
        'Ventana': i + 1,
        'Media RR (ms)': media_RR,
        'Desviación Estándar RR (SDNN) (ms)': std_RR,
        'RMSSD (ms)': rmssd,
        'NN50': nn50,
        'pNN50 (%)': pnn50,
        'SDSD (ms)': sdsd
    })
    
    # Graficamos cada ventana en una figura nueva con su color correspondiente
    color = colores[i % len(colores)]
    plt.figure(figsize=(10, 4))
    plt.plot(ventana, label=f'Ventana {i+1}', color=color)
    plt.plot(picos_R, ventana[picos_R], 'ro', label='Picos R')
    plt.title(f'Detección de Picos R en la Ventana {i+1}')
    plt.xlabel('Muestras')
    plt.ylabel('Amplitud')
    plt.legend()
    plt.grid(True)
    plt.show()

# Imprimir los resultados de HRV para cada ventana
for resultado in hrv_results:
    print(f"Ventana {resultado['Ventana']}:")
    print(f" - Media RR = {resultado['Media RR (ms)']:.2f} ms")
    print(f" - SDNN (Desviación Estándar RR) = {resultado['Desviación Estándar RR (SDNN) (ms)']:.2f} ms")
    print(f" - RMSSD = {resultado['RMSSD (ms)']:.2f} ms")
    print(f" - NN50 = {resultado['NN50']}")
    print(f" - pNN50 = {resultado['pNN50 (%)']:.2f}%")
    print(f" - SDSD = {resultado['SDSD (ms)']:.2f} ms\n")
    
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

# Convertimos `intervalos_RR` a segundos y calculamos los tiempos acumulativos
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