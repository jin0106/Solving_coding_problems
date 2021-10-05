T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split()) # N 컨테이너 M 트럭
    weight = list(map(int, input().split()))    # 화물의 무게
    truck = list(map(int, input().split())) # 트럭 적재
    weight.sort()
    truck.sort()
    ans = 0
    for i in range(len(truck)-1,-1,-1):
        temp = 0
        for j in range(len(weight)-1,-1,-1):
            if temp < weight[j] and truck[i] >= weight[j]:
                temp = weight[j]
                weight[j] = 0

        ans += temp
    print(f'#{t} {ans}')
