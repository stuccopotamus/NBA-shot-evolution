# fixing wrongly scaled data from three csv files '20, '21, '22

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import corrupted workbooks
df20 = pd.read_csv('shots/NBA_2020_Shots.csv')
df21 = pd.read_csv('shots/NBA_2021_Shots.csv')
df22 = pd.read_csv('shots/NBA_2022_Shots.csv')

# scale back corrupted LOC_X data
df20['LOC_X'] = (df20['LOC_X'] * 10).round(2)
df21['LOC_X'] = (df21['LOC_X'] * 10).round(2)
df22['LOC_X'] = (df22['LOC_X'] * 10).round(2)

# find minimum and maximum values in LOC_Y
print(df20['LOC_Y'].describe())
print(df21['LOC_Y'].describe())
print(df22['LOC_Y'].describe())

# set constants more accurately as possible
y_min = 5.225
y_max = 14.555 + 0.02
court_length = 94

# apply linear rescaling, taking the lowest value as close to 0 as possible and the highest as close to 94
df20['LOC_Y'] = ((df20['LOC_Y'] - y_min) / (y_max - y_min) * court_length).round(2)
df21['LOC_Y'] = ((df21['LOC_Y'] - y_min) / (y_max - y_min) * court_length).round(2)
df22['LOC_Y'] = ((df22['LOC_Y'] - y_min) / (y_max - y_min) * court_length).round(2)

# check for anomalies or errors in the fixed data
print(df20['LOC_X'].describe())
print(df21['LOC_X'].describe())
print(df22['LOC_X'].describe())
print(df20['LOC_Y'].describe())
print(df21['LOC_Y'].describe())
print(df22['LOC_Y'].describe())
sns.histplot(df20['LOC_Y'], bins=30, kde=True)
plt.show()
sns.histplot(df21['LOC_Y'], bins=30, kde=True)
plt.show()
sns.histplot(df22['LOC_Y'], bins=30, kde=True)
plt.show()

# save new files overwriting old files
df20.to_csv('shots/NBA_2020_Shots.csv', index=False)
df21.to_csv('shots/NBA_2021_Shots.csv', index=False)
df22.to_csv('shots/NBA_2022_Shots.csv', index=False)
