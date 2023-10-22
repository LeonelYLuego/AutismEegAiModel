import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Obtain data
data_alfa = pd.read_csv('./data/alfa.csv')
data_beta = pd.read_csv('./data/beta.csv')
data_delta = pd.read_csv('./data/delta.csv')
data_gama = pd.read_csv('./data/gamma.csv')
data_theta = pd.read_csv('./data/theta.csv')

# Merge data
data = pd.merge(data_alfa, data_beta, on=['Time:256Hz', 'Epoch', 'Event Id', 'Event Date', 'Event Duration'], suffixes=('_alfa', '_beta'))
data_frames = [data_delta, data_gama, data_theta]
suffixes = ['_delta', '_gama', '_theta']
for i in range(len(data_frames)):
    data = pd.merge(data, data_frames[i], on=['Time:256Hz', 'Epoch', 'Event Id', 'Event Date', 'Event Duration'], suffixes=('', suffixes[i]))
data.drop(['Epoch', 'Event Id', 'Event Date', 'Event Duration'], axis=1, inplace=True)
column_rename_dict = {
    f'Channel {i}': f'Channel {i}_delta' for i in range(1, 15)
}
data.rename(columns=column_rename_dict, inplace=True)

# Show relevant information
print('------ Columns -------')
print(data.info())
print('------ Extra information -------')
print(data.describe())

# data.plot()
# plt.show()
# data.hist(bins=50, figsize=(20, 15))
# plt.show()

# Preprocessing the data
## Standardize
scaler = StandardScaler()
data_scaled = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
def calculate_entropy(data, time_scale): 
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

'''
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


'''
def get_channels(data): 
    scale_factor = 100
    num_samples, num_channels = data.shape
    entropies_multiscale = []

    #recorremos los canales para calcular sus entropias 
    for i in range(0, num_channels): 
        column = data.iloc[:, i]
        channel_entropy_object = calculate_multiscale_entropy(channel=column, scale_factor=scale_factor, num_samples=num_samples)
        entropies_multiscale.append(channel_entropy_object)
    
    print(entropies_multiscale) # entropies multiscale es una lista de diccionarios
    return entropies_multiscale

# dataframe = pd.DataFrame(data, columns=data.columns)
get_channels(data_scaled)

data_scaled.plot()
plt.show()
