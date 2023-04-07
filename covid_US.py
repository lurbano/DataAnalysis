import pandas as pd 
import matplotlib.pyplot as plt
# Pandas 10 min guide: https://pandas.pydata.org/docs/user_guide/10min.html
# COVID 19 data:
#  https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series

# read in data file into a dataframe 
data = pd.read_csv("time_series_covid19_confirmed_US.csv")

# print the first 5 data values
print(data.head())

print("Index:", data.index)
print("Columns:", data.columns[:12])


print()
print('For date: 3/9/23')
print(data['3/9/23'].describe())
print(f'Median: {data["3/9/23"].median()}')

print()
print('For first row of data iloc=0')
print(data.iloc[0][11:])
data.iloc[0][11:].plot()
plt.show()
print(data.iloc[0][12:].describe())

print()
print("Missouri")
missouri = data.loc[data['Province_State'] == 'Missouri']
print(missouri)
print(missouri['3/9/23'].describe())
# print out all the counties in Missouri
for p in missouri['Admin2']:
    print(p)
stLouis = missouri.loc[missouri['Admin2'] == "St. Louis"]
print('---St Louis---')
print(stLouis)
print()
print(stLouis.iloc[0][11:])
stLouis.iloc[0][11:].plot()
plt.show()

# print()
# print("US States")
# statesSum = data.groupby('Province_State')[['3/9/23']].sum()
# print(statesSum)
# print(statesSum.describe())
# statesSum.plot()
# plt.show()


# data.hist(column='3/9/23')
# plt.show()