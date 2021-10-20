from collections import deque


def bfs(y,x):

    global eat, size, dist
    visited = [[-1] * N for _ in range(N)]
    visited[y][x] = 0
    fish = []
    q = deque()
    q.append((y, x))


    while q:
        while q:
            y, x = q.popleft()

            for i in range(4):
                ny = y + dr[i]
                nx = x + dc[i]

                if 0 <= ny < N and 0 <= nx < N:
                    if visited[ny][nx] == -1:
                        if sea[ny][nx] !=0 and sea[ny][nx] < size:      # 먹은거
                            visited[ny][nx] = visited[y][x] + 1
                            fish.append((ny,nx,visited[ny][nx]))    # 물고기 먹으면 fish에 추가

                        elif sea[ny][nx] <= size:       # 사이즈와 같거나 작으면 이동
                            visited[ny][nx] = visited[y][x] + 1
                            q.append((ny, nx))

        if fish:
            fish.sort(key=lambda x: (x[2], x[0], x[1]))  # 거리, 위, 왼쪽 순으로 정렬
            i, j= fish[0][0], fish[0][1]  # 제일 처음꺼 좌표 가지고 오기
            dist += visited[i][j]  # 이동거리 더 해주기
            sea[i][j] = 0  # 물고기 먹은 위치 0 으로
            visited = [[-1] * N for _ in range(N)]  # visited 재생성
            visited[i][j] = 0  # 시작 위치 0
            q = deque()
            q.append((i, j))
            eat += 1
            if eat == size: # 먹은 횟수와 사이즈 비교
                size += 1
                eat = 0
            fish =[]






N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
size = 2    # 아기 상어 처음 사이즈
eat = 0
dist = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for y in range(N):
    for x in range(N):
        if sea[y][x] == 9:
             sea[y][x] = 0      # 아기 상어 위치 추가
             bfs(y,x)
print(dist)

