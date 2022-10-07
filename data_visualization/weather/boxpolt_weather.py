import csv
import matplotlib.pyplot as plt
import random

# boxplot 예
result = []

for i in range(13):
    result.append(random.randint(1, 1000))
result.sort()

# plt.boxplot(result)

# weather boxplot
f = open('data_visualization\weather\seoul_weather.csv')
data = csv.reader(f)
next(data)

month = [[], [], [], [], [], [], [], [], [], [], [], []]
print(month)

for row in data:
    if row[-1] != '':
        month[int(row[0].split('-')[1])-1].append(float(row[-1]))

plt.boxplot(month)
plt.show()