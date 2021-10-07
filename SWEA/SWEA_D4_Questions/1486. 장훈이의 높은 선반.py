def dfs(idx,_sum):
    global  ans

    if _sum >= B:   # 기준 값보다 많을경우 최소값 갱신
        ans = min(ans, (_sum-B))
        return

    if idx == N:    # N에 도달하면 리턴
        return

    dfs(idx+1, _sum)    # 해당 값을 포함시키지않는경우
    dfs(idx+1, _sum + S[idx])   # 해당 값을 포함시키는 경우


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))
    ans = float('inf')  # 최대값 설정
    dfs(0,0)
    print(f'#{tc} {ans}')
