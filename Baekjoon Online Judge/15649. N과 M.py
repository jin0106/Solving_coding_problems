def dfs(k):
    if k==M:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(1, N+1):
        if i not in arr and visited[i] ==0:
            arr.append(i)
            visited[i] = True
            dfs(k+1)
            arr.pop()
            visited[i] = False



N, M = map(int, input().split())
arr = []
visited = [False]*(N+1)

dfs(0)

