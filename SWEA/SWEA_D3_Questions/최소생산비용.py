def dfs(level,expense):
    global ans

    if expense>ans:
        return  # 기존값 보다 크면 리턴

    if level == N:
        ans = min(ans,expense)  # 최소값 구하기
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1 # 방문 입력 
            dfs(level+1, expense+fac[level][i]) # 해당값 더한뒤 재귀 실행
            visited[i] = 0 #방문 초기화


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    fac = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = float('inf')
    dfs(0,0)
    print(f'#{tc} {ans}')
