n, m = map(int, input().split())


def dfs(num, ans):
    if len(ans) == m+1:
        print(' '.join(map(str, ans[1::])))
        return
    else:
        for i in range(num, n+1):
            dfs(i+1, ans+str(i))


dfs(1, '1')
