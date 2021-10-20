from collections import deque
import copy


def bfs():
    global ans
    area_copy = copy.deepcopy(area)
    for y in range(N):
        for x in range(M):
            if area_copy[y][x] == 2:
                q.append((y, x))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dr[i]
            nx = x + dc[i]

            if 0 <= ny < N and 0 <= nx < M:
                if area_copy[ny][nx] == 0:
                    area_copy[ny][nx] = 2
                    q.append((ny, nx))
    z = 0
    for i in range(N):
        z += area_copy[i].count(0)

    ans = max(ans, z)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for y in range(N):
        for x in range(M):
            if area[y][x] == 0:
                area[y][x] = 1
                wall(cnt+1)
                area[y][x] = 0


N, M = map(int, input().split())    # N 세로
area = [list(map(int, input().split())) for _ in range(N)]
q = deque()
ans = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
wall(0)
print(ans)
