from collections import deque

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    beach = [input() for _ in range(N)]
    visited =[[0]*M for _ in range(N)]
    Q = deque()
    for y in range(N):
        for x in range(M):
            if beach[y][x] =='W':
                Q.append((y,x))

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    while Q:
        y,x = Q.popleft()
        for i in range(4):
            ny = y + dr[i]
            nx = x + dc[i]

            if 0<= ny < N and 0 <= nx < M and visited[ny][nx] == 0:
                if beach[ny][nx] == 'L':
                    visited[ny][nx] = visited[y][x] +1
                    Q.append((ny,nx))
    ans = 0
    for i in range(N):
        ans += sum(visited[i])
    print(f'#{t} {ans}')





















