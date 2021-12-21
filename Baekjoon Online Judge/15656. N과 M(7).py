N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = [0]*M


def dfs(k):
    if k == M:
        for i in range(M):
            print(ans[i], end=' ')
        print()
        return

    for i in range(N):
        ans[k] = arr[i]
        dfs(k+1)


dfs(0)
