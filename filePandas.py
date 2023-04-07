import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("timeTemp.txt", sep="\t")

print(data.head())

print(data.describe())

z = data['°C'].mean()
print(f"mean T: {z}")

# histogram for °C column
data.hist(column='°C')
plt.show()