import sys
from itertools import combinations
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chicken = []    # 치킨집들 좌표
houses = [] # 집들 좌표
distance = []   # 거리 추가할 리스트 생성
temp_lst = []


for y in range(N):  # 치킨집과 집들의 좌표 구하기
    for x in range(N):
        if city[y][x] == 2:
            chicken.append((y,x))
        elif city[y][x] ==1:
            houses.append((y,x))

for i in list(combinations(chicken, M)):    # 치킨집 리스트중 M개 뽑아서 조합
    city_dist = 0
    for r, c in houses:
        dists = []
        for y,x in i:   # 각 치킨집 조합별 최단거리 구하기
            dist = abs(y-r)+ abs(x-c)
            dists.append(dist)
        city_dist += min(dists)
    distance.append(city_dist)

print(min(distance))    # 조합별 최단거리 중에 최소값 출력
