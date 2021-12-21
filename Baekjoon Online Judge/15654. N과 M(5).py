N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = [0]*M
visit = [0] * N


def dfs(k, start):
    if k == M:
        for i in range(M):
            print(ans[i], end=' ')
        print()
        return

    for i in range(N):
        if visit[i] == 0:
            ans[k] = arr[i]
            visit[i] = 1
            dfs(k+1, start)
            visit[i] = 0
    return


dfs(0, 0)
