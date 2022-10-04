import csv

f = open('data_anlasys\seoul_weather.csv', 'r', encoding='cp949')

# data에 csv객체 저장(, 기준으로)
# data = csv.reader(f, delimiter=',')

data = csv.reader(f)
for row in data:
    print(row)
f.close()