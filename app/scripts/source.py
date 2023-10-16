import pandas as pd
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

def get_dataframe(data):
    return pd.DataFrame(data)

def get_merged_dataframe(alfa, beta, delta, gamma, theta) -> pd.DataFrame:
    """get_merged_dataframe regresa un dataframe con los canales fusionados en un solo dataframe

    Args:
        alfa (list): Lista de objetos de tipo Wave con las ondas alfa
        beta (list): Lista de objetos de tipo Wave con las ondas beta
        delta (list): Lista de objetos de tipo Wave con las ondas delta
        gamma (list): Lista de objetos de tipo Wave con las ondas gamma
        theta (list): Lista de objetos de tipo Wave con las ondas theta

    Returns:
        pd.DataFrame: DataFrame con los canales fusionados
    """
    merge = pd.merge(alfa, beta, on=['time'], suffixes=('_alfa', '_beta'))
    merge2= pd.merge(delta, gamma, on=['time'], suffixes=('_delta', '_gamma'))
    merge3 = pd.merge(merge, merge2, on=['time'])
    merge4 = pd.merge(merge3, theta, on=['time'], suffixes=('', '_theta'))
    # data = pd.DataFrame()
    # types = ['alfa', 'beta', 'delta', 'gamma', 'theta']
    # for i in range(len(datas)):
    #     dt = get_dataframe(datas[i])
    #     if i == 0:
    #         data = dt
    #     else:
    #         data = pd.merge(data, dt, on=['time'], suffixes=('', f'_{types[i]}'))
    # data.drop(['time'], axis=1, inplace=True)
    # column_rename_dict = {
    #     f'channel{i}': f'channel{i}_{types[0]}' for i in range(1, 15)
    # }
    # data.rename(columns=column_rename_dict, inplace=True)
    # return data

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

def get_channels(data):
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
    scale_factor = 100
    num_samples, num_channels = data.shape
    entropies_multiscale = {}

    #recorremos los canales para calcular sus entropias 
    for i in range(0, num_channels):
        column = data.iloc[:, i]
        entropies_multiscale[column.name] = calculate_multiscale_entropy(channel=column, scale_factor=scale_factor, num_samples=num_samples)
    
    return entropies_multiscale

def get_preprocessed_data(alfa, beta, delta, gamma, theta):
    """get_preprocessed_data regresa un dataframe con los canales y sus entropias

    Args:
        datas (list): lista de listas de objetos de tipo Wave

    Returns:
        DataFrame: DataFrame con los canales y sus entropias
    """
    merged = get_merged_dataframe(alfa, beta, delta, gamma, theta)
    return pd.DataFrame(get_channels(pd.DataFrame(scaler.fit_transform(merged), columns=merged.columns)))
