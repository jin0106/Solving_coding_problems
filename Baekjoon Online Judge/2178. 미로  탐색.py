from collections import deque

N, M = map(int, input().split()) # N 세로 M 가로
maze = [list(map(int, input())) for _ in range(N)]
visited= [[0]*M for _ in range(N)]
dr = [-1,1,0,0] # 상하좌우 범위
dc = [0,0,-1,1]
Q = deque()
Q.append((0,0)) # 처음 시작 좌표 추가해주기
visited[0][0]=1 # 시작부터 1개로 치므로 1로 변경
temp =[]    # 최소값 찾기 위한 리스트 생성
while Q:
    y,x = Q.popleft()
    for i in range(4):
        ny = y + dr[i]
        nx = x + dc[i]
        if 0<=ny <N and 0<= nx < M and visited[ny][nx] ==0: # 인덱스 범위 설정에 맞고 한번도 방문하지 않았을때
            if maze[ny][nx] == 1:      # 갈수 있는 길이면
                visited[ny][nx] = visited[y][x]+1   # 1을 추가
                if ny == N-1 and nx==M-1:   # 만약에 목표로 하는 마지막 인덱스이면 temp에 값을 추가 하고 다시 0으로 만들어줌. 다른경우의수가 있을수도 있기에
                    temp.append(visited[ny][nx])
                    visited[ny][nx] =0
                else:
                    Q.append((ny, nx))
print(min(temp))



