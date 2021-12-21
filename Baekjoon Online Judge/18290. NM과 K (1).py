N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

ans = -100000

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[0]*M for _ in range(N)]


def dfs(r, c, k, num):
    global ans

    if k == K:
        ans = max(ans, num)
        return

    for y in range(r, N):
        for x in range(c if r == y else 0, M):
            if visited[y][x]:
                continue

            for i in range(4):
                ny = y + dr[i]
                nx = x + dc[i]

                if 0 <= ny < N and 0 <= nx < M and visited[ny][nx]:
                    break

            else:
                visited[y][x] = 1
                dfs(y, x, k+1, num+arr[y][x])
                visited[y][x] = 0


dfs(0, 0, 0, 0)
print(ans)
