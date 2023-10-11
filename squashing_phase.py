import numpy as np 
from scipy.stats import entropy
import pandas as pd

# Cada fila representa una muestra y cada columna un canal 

#Función para calcular la entropía de cada canal 
def calculate_entropy(data, time_scale): 
    #falta mandar el rango de empiezar y terminar el ciclo 
    multiplier = 1/time_scale
    addition_of_x = 0

    for x_data in data:
        addition_of_x += x_data

    entropy = multiplier * addition_of_x
    
    return entropy #se retorna un escalar

#Calculamos entropias de diferentes escalas dividiendo los datos en segmentos y calculando la entropia de cada segmento 
def calculate_multiscale_entropy(data, scale_factor): 
    num_samples, num_channels = data.shape
    entropies_multiscale = []

    first_column = data.iloc[:, 0] # Primera columna
    print(first_column)
    #tenermos que mandar la primera columna
    for i in range(0, num_samples, scale_factor):
        segment = first_column.iloc[i:i+scale_factor]
        channel_entropy = calculate_entropy(segment, scale_factor)
        entropies_multiscale.append(channel_entropy)
    print(entropies_multiscale)

    return np.array(entropies_multiscale)

#definicion del factor de escala 
data = pd.read_csv('./data_combined.csv')
dataframe = pd.DataFrame(data, columns=data.columns)
scale_factor = 100
entropies_multiscale = calculate_multiscale_entropy(dataframe, scale_factor)
entropies_multiscale