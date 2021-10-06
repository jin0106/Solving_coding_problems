from collections import deque

dr = [-1,1,0,0,-1,-1,1,1]
dc = [0,0,-1,1,-1,1,-1,1]

N, M = map(int, input().split()) # N 세로 M 가로
sea = [list(map(int, input().split())) for _ in range(N)]
ans = 0
q = deque()

for y in range(N):
    for x in range(M):
        if sea[y][x] == 1:  # 상어들 q에 다 추가
            q.append((y,x))

while q:
    y,x = q.popleft()

    for i in range(8):  # 8 방향 탐색
        ny = y + dr[i]
        nx = x + dc[i]

        if 0 <= ny < N and 0 <= nx < M and sea[ny][nx] ==0:
            sea[ny][nx] = sea[y][x] +1  # 전에 있던곳 보다 1증가
            ans = max(sea[ny][nx],ans)  # 최대값 찾기
            q.append((ny,nx))

print(ans-1)