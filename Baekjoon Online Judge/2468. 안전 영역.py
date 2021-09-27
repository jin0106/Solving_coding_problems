from collections import deque


def bfs(y,x,j):
    global ans

    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dr[i]
            nx = x + dc[i]

            if 0<= ny <N and 0<= nx < N:
                if area[ny][nx] > j and visited[ny][nx] ==0:
                    visited[ny][nx] = 1
                    q.append((ny,nx))

dr = [-1,1,0,0]
dc = [0,0,-1,1]

N = int(input())

area = [list(map(int, input().split())) for _ in range(N)]
highest = 0
for i in range(N):      # 가장 높은 높이 구하기
    s = max(area[i])
    highest = max(s,highest)


lst = []    # max 값 찾기 위해 리스트 생성

for j in range(highest+1):  # 가장 높은 높이보다 큰 높이들이 오면 안전지역은 0이므로 가장 높은 높이까지만 체크
    visited = [[0] * N for _ in range(N)]   # 방문 체크
    ans = 0
    for y in range(N):
        for x in range(N):
            if area[y][x] > j and visited[y][x] == 0:   # 기준 높이보다 높고 한번도 방문하지 않았으면
                bfs(y,x,j)  # 함수 실행
                ans += 1    # 안전지역 수 추가
    lst.append(ans)
print(max(lst))