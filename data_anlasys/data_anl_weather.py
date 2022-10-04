import csv

f = open('data_anlasys\seoul_weather.csv', 'r', encoding='cp949')

# data에 csv객체 저장(, 기준으로)
# data = csv.reader(f, delimiter=',')

data = csv.reader(f)

# 헤더 저장(속성값 저장) next : 첫 행을 읽으면서 다음 위치로 이동
header = next(data)
for row in data:
    print(row)
f.close()