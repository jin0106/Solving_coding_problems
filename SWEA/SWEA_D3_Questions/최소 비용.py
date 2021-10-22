from collections import deque
T = int(input())
for tc in range(1,T+1):
    N = int(input())

    area = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float('inf')]*N for _ in range(N)]
    q = deque()
    q.append((0,0))
    visited[0][0] = 0   # 시작값 0 으로 설정

    dr = [-1,1,0,0] # 상하좌우
    dc = [0,0,-1,1]

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dr[i]
            nx = x + dc[i]

            if 0 <= ny < N and 0 <= nx < N:
                if area[ny][nx] > area[y][x]:   # ny,nx 위치한 값이 더 클때
                    temp = area[ny][nx] - area[y][x]    # 두 값의 차이 + 1을 더해줘야하므로
                    if visited[ny][nx] > visited[y][x]+temp+1:  # 최소값 찾아주기
                        visited[ny][nx] = visited[y][x]+temp+1
                        q.append((ny,nx))
                else:   # 두 값이 같거나 y,x가 더 클때
                    if visited[ny][nx] > visited[y][x] +1:  # 최소값 찾아주기
                        visited[ny][nx] = visited[y][x]+1
                        q.append((ny,nx))

    print(f'#{tc} {visited[-1][-1]}')