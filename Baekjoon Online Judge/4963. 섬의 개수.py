from collections import deque

def bfs(y,x):
    global ans
    ans +=1

    q = deque()
    q.append((y,x)) # 좌표를 추가

    while q:
        y, x = q.popleft()  # 좌표를 받아서
        for i in range(8):  # 8방향 탐색
            ny = y + dr[i]
            nx = x + dc[i]

            if 0 <= ny < h and 0 <= nx < w: # 인덱스 범위내에 있으면
                if Map[ny][nx] == 1: # 1(땅) 이면
                    q.append((ny,nx))   # 좌표 추가 하고
                    Map[ny][nx] = 0 # 방문 체크용으로 0으로 변경

while True:
    ans = 0
    w, h = map(int, input().split())
    if w ==0 and h == 0:    # h 높이
        break

    Map = [list(map(int, input().split())) for _ in range(h)]

    dr = [-1, 1, 0, 0, 1, 1, -1, -1]  # 상 하 좌 우 좌하 우하 좌상 우상
    dc = [0, 0, -1, 1, -1, 1, -1, 1]

    for y in range(h):
        for x in range(w):
            if Map[y][x] == 1:  # 1이면 bfs
                bfs(y,x)



    print(ans)


