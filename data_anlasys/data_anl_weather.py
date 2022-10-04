import csv

f = open('data_anlasys\seoul_weather.csv', 'r', encoding='cp949')

# data에 csv객체 저장(, 기준으로)
# data = csv.reader(f, delimiter=',')

data = csv.reader(f)

# 헤더 저장(속성값 저장) next : 첫 행을 읽으면서 다음 위치로 이동
header = next(data)

# 최고기온, 해당 날짜 변수
max_temp = -999
max_date = ''

for row in data:
    # 최고기온이 없을때
    if row[-1] == '':
        row[-1] = -999
    
    # float로 형변환
    row[-1] = float(row[-1])

    # 최댓값보다 큰 온도일 경우 max_date, max_temp 할당
    if row[-1] > max_temp:
        max_date = row[0]
        max_temp = row[-1]
        
# 최대온도, 날짜 출력
print(max_date, max_temp)
f.close()