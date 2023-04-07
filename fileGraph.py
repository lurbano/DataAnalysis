import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def C2F(c):
    return (c*9/5)+32

with open("timeTemp.txt", 'r') as f:
    lines = f.readlines()
    
print(lines[0:5])

# create arrays for time and temperature
t = []
T = []

for i in lines[1:]: # do every line except the first
    # print(i)
    # split each line 
    a, b = i.strip().split('\t')
    # convert from string to numbers
    t.append(float(a))
    T.append(float(b))

t = np.array(t, float)
T = np.array(T, float)

print(f't: {t}')
print(f'T: {T}')

avgT = np.average(T)
maxT = np.max(T)
skewT = stats.skew(T)

print(f"Avg T: {avgT} °C, {C2F(avgT)} °F")
print(f"Max T: {maxT} °C, {C2F(maxT)} °F")
print(f"Skew T: {skewT} ")

# graph
fig, ax = plt.subplots()
ax.plot(t, T)
plt.show()
