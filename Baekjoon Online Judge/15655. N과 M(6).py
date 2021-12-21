N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visit = [0]*N
ans = [0]*M


def dfs(k, start):
    if k == M:
        for i in range(M):
            print(ans[i], end=' ')
        print()
        return

    for i in range(start, N):
        if visit[i] == 0:
            ans[k] = arr[i]
            visit[i] = 1
            dfs(k+1, i)
            visit[i] = 0


dfs(0, 0)
