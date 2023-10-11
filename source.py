import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Obtain data
data_alfa = pd.read_csv('./data/alfa.csv')
data_beta = pd.read_csv('./data/beta.csv')
data_delta = pd.read_csv('./data/delta.csv')
data_gama = pd.read_csv('./data/gama.csv')
data_theta = pd.read_csv('./data/theta.csv')

# Merge data
data = pd.merge(data_alfa, data_beta, on=['Time:128Hz', 'Epoch', 'Event Id', 'Event Date', 'Event Duration'], suffixes=('_alfa', '_beta'))
data_frames = [data_delta, data_gama, data_theta]
suffixes = ['_delta', '_gama', '_theta']
for i in range(len(data_frames)):
    data = pd.merge(data, data_frames[i], on=['Time:128Hz', 'Epoch', 'Event Id', 'Event Date', 'Event Duration'], suffixes=('', suffixes[i]))
data.drop(['Time:128Hz', 'Epoch', 'Event Id', 'Event Date', 'Event Duration'], axis=1, inplace=True)
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
new_data = data_scaled.to_csv("data_combined.csv", sep=',', index=False)

data_scaled.plot()
plt.show()

