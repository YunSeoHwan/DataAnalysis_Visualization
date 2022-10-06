import matplotlib.pyplot as plt

# list 1개면 y축 값
plt.plot([10, 20, 30, 40])

# list 2개면 x, y로 입력
plt.plot([1,2,3,4], [12, 43, 25, 15])

# title 설정
plt.title("plotting")
plt.plot([10, 20, 30, 40])

# label 설정
plt.title("legend")
plt.plot([10, 20, 30, 40], label = 'asc')
plt.plot([40, 30, 20, 10], label = 'desc')
plt.legend()    # 범례 설정 (loc = 1~10으로 위치 설정)

# 색깔 설정
plt.title('color')
plt.plot([10, 20, 30, 40], color = 'skyblue', label = 'skyblue')
plt.plot([40, 30, 20, 10], color = 'pink', label = 'pink')
plt.legend()


# 선 모양 바꾸기
plt.title('linestyle')
plt.plot([10, 20, 30, 40], color = 'r', linestyle = '--', label = 'dashed')
plt.plot([40, 30, 20, 10], color = 'g', ls = ':', label = 'dotted')
plt.legend()
plt.show()

# 마커 모양 바꾸기 (. : circle, ^ : triangle)
plt.title('marker')
plt.plot([10, 20, 30, 40], 'r.', label = 'circle')
plt.plot([40, 30, 20, 10], 'g^', label = 'triangle up')
plt.legend()
plt.show()