import numpy as np 
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

def calculate_multiscale_entropy(channel, scale_factor, num_samples): 
    entropies_multiscale = []
    channel_info = {}

    #Calculamos entropias de diferentes escalas dividiendo los datos en segmentos y calculando la entropia de cada segmento 
    for i in range(0, num_samples, scale_factor):
        segment = channel.iloc[i:i+scale_factor]
        channel_entropy = calculate_entropy(segment, scale_factor)
        entropies_multiscale.append(channel_entropy)

    channel_info['name'] = channel.name #asignamos el noombre del canal 
    channel_info['entropy'] = entropies_multiscale #agregamos su conjunto de entropias por segmento 

    return channel_info


def get_channels(data): 
    scale_factor = 100
    num_samples, num_channels = data.shape
    entropies_multiscale = []

    #recorremos los canales para calcular sus entropias 
    for i in range(0, num_channels): 
        column = data.iloc[:, i]
        channel_entropy_object = calculate_multiscale_entropy(channel=column, scale_factor=scale_factor, num_samples=num_samples)
        entropies_multiscale.append(channel_entropy_object)
        
    return entropies_multiscale

#definicion del factor de escala 
data = pd.read_csv('./data_combined.csv')
dataframe = pd.DataFrame(data, columns=data.columns)
print(get_channels(dataframe))