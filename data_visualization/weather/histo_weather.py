import matplotlib.pyplot as plt
import random
import csv

# 히스토그램 생성
# plt.hist([1,1,2,3,4,5,6,6,7,8,10])

# 주사위 히스토그램
dice = []
for i in range(1000000):
    dice.append(random.randint(1,6))

# plt.hist(dice, bins=6)  # bins : 가로축 구간 수


# 최고온도 히스토그램
f = open('data_visualization\weather\seoul_weather.csv')
data = csv.reader(f)
next(data)

# 1, 8월 변수
aug = []
jan = []

for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '08':
            aug.append(float(row[-1]))
        elif row[0].split('-')[1] == '01':
            jan.append(float(row[-1]))

plt.title('1, 8 Month high temperature')
plt.hist(aug, bins=100, color='r', label='AUG')
plt.hist(jan, bins=100, color='b', label='JAN')
plt.legend()
plt.show()