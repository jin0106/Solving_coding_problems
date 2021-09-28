from collections import deque

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visit[0][0][0] = 1
    while q:
        y, x, z = q.popleft()
        if y == N - 1 and x == M - 1:
            return visit[y][x][z]

        for i in range(4):
            ny = y + dr[i]
            nx = x + dc[i]

            if 0 <= ny < N and 0 <= nx < M:
                if area[ny][nx] == 1 and z == 0:
                    visit[ny][nx][1] = visit[y][x][z] + 1
                    q.append((ny, nx, 1))
                elif area[ny][nx] ==0 and visit[ny][nx][z] == 0:
                    visit[ny][nx][z] = visit[y][x][z] + 1
                    q.append((ny, nx, z))


    return -1


N, M = map(int, input().split()) # N 세로
area = [list(map(int, input())) for _ in range(N)]
visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]


dr = [-1,1,0,0]
dc = [0,0,-1,1]
print(bfs())
print(visit[0][0][0])
print(visit)
