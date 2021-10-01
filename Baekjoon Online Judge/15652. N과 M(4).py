def dfs(k, start):
    if k==M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return

    for i in range(start, N+1):
        arr[k] = i
        dfs(k+1, i)
        arr[k] = 0

N, M = map(int, input().split())
arr = [0]*8

visited = [False]*(N+1)

dfs(0,1)

