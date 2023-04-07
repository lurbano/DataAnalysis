import pandas as pd 
import matplotlib.pyplot as plt
# reference:
#  https://pandas.pydata.org/docs/user_guide/10min.html

# read in data file into a dataframe 
data = pd.read_csv("timeTemp.txt", sep='\t')

# print the first 5 data values
print(data.head())

# summary statistics
x = data.describe()
print(x)

# get mean of each column
y = data.mean(axis=0)
print ("mean:\n", y)
print()

# get mean of just the °C column
z = data['°C'].mean()
print(f'°C mean: {z}')
print()

# descriptive statistics of just the °C column
z = data['°C'].describe()
print(f'°C description: \n{z}')
print()

# scatter graph of data
# data.plot.scatter(x='time (s)', y='°C')
# plt.show()

# histogram for °C column
data.hist(column='°C')
plt.show()
