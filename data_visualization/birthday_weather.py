import csv
import matplotlib.pyplot as plt

f = open('data_visualization\seoul_weather.csv')
data = csv.reader(f)

# 헤더부분 제거
next(data)

# 기온 값 list
high = []
low = []

for row in data:

    # 최고, 최저 온도가 존재할때
    if row[-1] != '' and row[-2] != '':

        # 2000년도 이후 데이터만
        if 2000 <= int(row[0].split('-')[0]):
            # 6월 13일 데이터만
            if row[0].split('-')[1] == '06' and row[0].split('-')[2] =='13':
                high.append(float(row[-1]))
                low.append(float(row[-2]))

# 그래프 그리기
plt.title("My birthday temperature")
# - 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False
plt.plot(high, 'r', label = 'high_temp')
plt.plot(low, 'b', label = 'low_temp')
plt.legend()
plt.show()