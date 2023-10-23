import pandas as pd
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

def calculate_time(time_column, scale_factor, num_samples): 
    times = []

    for i in range(0, num_samples - scale_factor, scale_factor):
        times.append(time_column[i+scale_factor] - time_column[i])
    return times

def get_dataframe(data):
    dt = pd.DataFrame(data)
    # Get the time column
    time_column = dt['time']
    dt.drop(['time'], axis=1, inplace=True)
    return dt, time_column

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

    #Calculamos entropias de diferentes escalas dividiendo los datos en segmentos y calculando la entropia de cada segmento 
    for i in range(0, num_samples, scale_factor):
        entropies_multiscale.append(calculate_entropy(channel.iloc[i:i+scale_factor], scale_factor))

    return entropies_multiscale

def get_channels(data, time_col):
    """
        get_channels separa por canales la data obtenida de data_scaled y calcula la entropia por segmentos de las series de tiempo de los canales. 

        Input: Dataframe
        Output: List of objects [{
                'name': 'channel 1_alfa', 
                'entropy': [list of float numbers]
            }, 
            {
                'name': 'channel 2_alfa', 
                'entropy': [list of float numbers]
            }, 
        ]
    """
    scale_factor = 256
    num_samples, num_channels = data.shape
    entropies_multiscale = {}
    #recorremos los canales para calcular sus entropias 
    for i in range(0, num_channels):
        column = data.iloc[:, i]
        entropies_multiscale[column.name] = calculate_multiscale_entropy(channel=column, scale_factor=scale_factor, num_samples=num_samples)
    
    entropies_multiscale['time'] = calculate_time(time_col, scale_factor, num_samples)

    return entropies_multiscale

def get_preprocessed_data(waves):
    """get_preprocessed_data regresa un dataframe con los canales y sus entropias

    Args:
        datas (list): lista de listas de objetos de tipo Wave

    Returns:
        DataFrame: DataFrame con los canales y sus entropias
    """
    waves_df, time_col = get_dataframe(waves)
    ret =  pd.DataFrame(get_channels(pd.DataFrame(scaler.fit_transform(waves_df), columns=waves_df.columns), time_col))
    print('ups')
