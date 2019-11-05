#While loops
x = [10, 12, 15, 0, 10, 5]
mean = sum(x)/len(x)
print(mean)

variance = []
for num in x:
    val = num - mean
    val = round(val, 2)
    variance.append(val)
print(variance)

variance2 = []
index = 0
while index < len(x):
    val = x[index] - mean
    variance2.append(val)
    index += 1
print(variance2)

deviation = []
for i in variance:
    dev = i**2
    dev = round(dev, 2)
    deviation.append(dev)
print (deviation)

deviation2 = []
index2 = 0
while index2 < len(variance2):
    dev2 = variance2[index2]**2
    deviation2.append(dev2)
    index2 += 1
print(deviation2)

file = open('meanfile.csv','w')
title = 'x, x-X, x-X2'
file.write(f'{title} \n')  

index = 0

while index < len(variance2):
    a = x[index]
    b = variance[index]
    c = deviation[index]
    note = f'{a}, {b}, {c} \n'
    file.write(f'{note}')
    index += 1


    
file.close()