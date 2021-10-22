from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input())) for _ in range(N)]

    visited =[[float('inf')]* N for _ in range(N)]
    visited[0][0] =0

    ans = float('inf')

    q= deque()
    q.append((0,0))

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    while q:
        y,x = q.popleft()


        for i in range(4):
            ny = y + dr[i]
            nx = x + dc[i]

            if 0 <= ny < N and 0 <= nx < N:
                if visited[y][x] + area[ny][nx] < visited[ny][nx]:  # 최소값 설정
                    visited[ny][nx] = visited[y][x] + area[ny][nx]
                    q.append((ny,nx))

    print(f'#{tc} {visited[N-1][N-1]}')

