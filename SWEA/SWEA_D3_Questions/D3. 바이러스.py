
from collections import deque

def bfs():
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dr[i]
            nx = x + dc[i]

            if 0 <= ny < N and 0<= nx <M:
                if server[ny][nx] == 2 or server[ny][nx] == 1:
                    server[ny][nx] = 3
                    q.append((ny,nx))

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split()) # N 세로
    server = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    ans = 0
    q= deque()

    for y in range(N):
        for x in range(M):
            if server[y][x] == 2:
                q.append((y,x))
                bfs()
                ans += 1
    print(f'#{t} {ans}')



