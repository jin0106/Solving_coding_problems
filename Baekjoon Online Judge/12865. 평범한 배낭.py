import sys
input = sys.stdin.readline

def pack(N,K, items):
    dp = [[0]*(K+1) for _ in range(N+1)]

    # 가방에 담을 수 있는 물건 개수를 1개부터 하나씩 늘려 간다.
    for i in range(1, N+1):
        weight, value = map(int, items[i-1])
        # 가방에 담을 수 있는 최대 무게를 1부터 차대로 증가 시켜 나가며
        for j in range(1, K+1):   #j : 가방에 담을 수 있는 무게
            if weight <= j: # 가방에 담을 수 있는 무게이면 최대값 비교 해서 저장
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
            else:   # 그게 아니면 전의 값 가져오기
                dp[i][j] = dp[i-1][j]
    print(dp[N][K])



# N : 물건의 개수  K: 가방에 담을 수 있는 최대 무게
N,K = map(int, input().split())
# 각 물건의 무게와 가치
items = [list(map(int, input().split())) for _ in range(N)]
pack(N,K,items)