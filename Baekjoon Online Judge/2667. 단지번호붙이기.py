def dfs(y,x):
    global visited
    global cnt
    cnt +=1
    visited[y][x] = 1 # 방문 기록 체크
    for i in range(4):
        ny = y+dr[i]    # 델타 검색으로 탐색
        nx = x+dc[i]
        if N>ny >=0 and N> nx >=0 and visited[ny][nx] ==0 : # 인덱스 범위 설정 및 방문 한번도 안했으면
            if complex[ny][nx] == 1:    # 1이면 dfs
                dfs(ny,nx)
    return

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
complex = [list(map(int, input())) for _ in range(N)]
cnt_house =[]   # cnt들 저장할 빈 리스트 생성(단지수)
visited= [[0]*N for _ in range(N)] # 방문 기록 생성
for y in range(N):  # 2중 포문으로 1인곳 찾기
    for x in range(N):
        cnt = 0
        if complex[y][x] == 1  and visited[y][x] ==0:   # 1이고 한번도 방문 하지 않았다면 dfs시작
            dfs(y,x)
            if cnt != 0: # cnt가 0이 아니면 cnt_house에 추가
                cnt_house.append(cnt)
cnt_house.sort()
print(len(cnt_house))
for i in range(len(cnt_house)):
    print(cnt_house[i])