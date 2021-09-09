# 아래 그림과 같은 미로가 있다. 16*16 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.

# 가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.

# 주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.

# 아래의 예시에서는 도달 가능하다.

# bfs 방식 풀이

from collections import deque


def bfs(r, c):
    global visited
    dr = [-1, 1, 0, 0]  # 델타 검색
    dc = [0, 0, -1, 1]
    queue = deque()  # queue 생성
    queue.append((r, c))  # 첫 시작 좌표 추가

    while queue:        # queue가 있는동안
        r, c = queue.popleft()  # 제일 처음 좌표를 pop
        for i in range(4):  # 델타 검색
            ny = r + dr[i]
            nx = c + dc[i]
            # 인덱스 조건에 맞고 한번도 방문한적 없으면
            if ny >= 0 and ny < 16 and nx >= 0 and nx < 16 and visited[ny][nx] == 0:
                if M[ny][nx] == 0:      # 0이면 통로 이므로 방문기록을 남기고 queue에 좌표 추가
                    visited[ny][nx] = 1
                    queue.append((ny, nx))
                elif M[ny][nx] == 1:    # 1이면 벽이므로 방문기록만 남김
                    visited[ny][nx] = 1
                    continue
                elif M[ny][nx] == 3:    # 3이면 답을 찾은것이므로 return
                    return 1
    return 0


for t in range(1, 11):
    tc = int(input())
    M = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    for y in range(16):
        for x in range(16):
            if M[y][x] == 2:
                visited[y][x] = 1
                ret = bfs(y, x)
                break
    print("#{} {}".format(t, ret))


# dfs 방식 풀이

r = [-1, 1, 0, 0]
c = [0, 0, -1, 1]


def dfs(y, x):
    global ans  # dfs는 3을 찾고 return을해도 바로 함수가 끝나지 않으므로 변수를 생성해놓고 하는게 좋다.
    if M[y][x] == 3:
        ans = 1
        return
    for i in range(4):
        ny = y+r[i]
        nx = x+c[i]
        if ny >= 0 and nx >= 0 and ny < 16 and nx < 16 and visited[ny][nx] == 0:
            if M[ny][nx] == 0 or M[ny][nx] == 3:
                visited[ny][nx] = 1
                dfs(ny, nx)
    return


for t in range(1, 11):
    tc = int(input())
    M = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    ans = 0
    for y in range(16):
        for x in range(16):
            if M[y][x] == 2:
                visited[y][x] = 1
                dfs(y, x)
                break
    print("#{} {}".format(t, ans))
