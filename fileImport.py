

with open("timeTemp.txt", 'r') as f:
    lines = f.readlines()

# print(lines)

print(lines[0:5])

totalT = 0
for i in lines[1:]: # do every line except the first
    print(i)
    # split each line 
    t, T = i.strip().split('\t')
    # convert from string to numbers
    t = float(t)
    T = float(T)
    totalT += T

print(f'T_total: {totalT}')
avgT = totalT / len(lines[1:])
print(f'Avg T: {avgT}')