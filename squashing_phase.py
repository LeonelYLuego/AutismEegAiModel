import numpy as np 
from scipy.stats import entropy
import pandas as pd

# Cada fila representa una muestra y cada columna un canal 

#Función para calcular la entropía de cada canal 
def calculate_entropy(data): 
    entropies = []
    for channel_data in data.T:
        channel_entropy = entropy(channel_data)
        entropies.append(channel_entropy)
    return entropies

#Calculamos entropias de diferentes escalas dividiendo los datos en segmentos y calculando la entropia de cada segmento 
def calculate_multiscale_entropy(data, scale_factor): 
    num_samples, num_channels = data.shape
    entropies_multiscale = []

    for i in range(0, num_samples, scale_factor):
        segment = data.iloc[i:i+scale_factor, :]
        channel_entropies = calculate_entropy(segment)
        entropies_multiscale.append(channel_entropies)
    print(entropies_multiscale)

    return np.array(entropies_multiscale)

#definicion del factor de escala 
data = pd.read_csv('./data_combined.csv')
dataframe = pd.DataFrame(data, columns=data.columns)
scale_factor = 700
entropies_multiscale = calculate_multiscale_entropy(dataframe, scale_factor)
entropies_multiscale