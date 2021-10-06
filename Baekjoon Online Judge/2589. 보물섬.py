from collections import deque


def bfs(y,x):
    q = deque()
    q.append((y,x))
    visited = [[0] * M for _ in range(N)]
    visited[y][x] = 1
    cnt = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dr[i]
            nx = x + dc[i]

            if 0 <= ny < N and 0 <= nx < M and Map[ny][nx] == 'L':
                if visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    cnt = max(cnt, visited[ny][nx])
                    q.append((ny, nx))
    return cnt-1

N, M = map(int, input().split()) # N 세로 M가로
Map = [list(input()) for _ in range(N)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]
ans = 0

for y in range(N):
    for x in range(M):
        if Map[y][x] == 'L':
            ans = max(ans, bfs(y,x))
print(ans)