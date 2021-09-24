from collections import deque


M, N = map(int, input().split())    # M 가로 N세로
farm = [list(map(int, input().split())) for _ in range(N)]
q = deque()

dr = [-1,1,0,0] # 상하좌우
dc = [0,0,-1,1]

for y in range(N):
    for x in range(M):
        if farm[y][x] == 1: # 1인곳 좌표 확인해서 q에 추가
            q.append((y,x))
            farm[y][x] = 1
while q:
    y,x = q.popleft()   # 좌표를 얻어와서
    for i in range(4):  # 상하좌우 탐색
        ny = y + dr[i]
        nx = x + dc[i]
        if 0<= ny < N and 0 <= nx <M and farm[ny][nx] ==0:  # 인덱스 범위내에 있고 0이라면
            farm[ny][nx] = farm[y][x] +1    # 기존의 값에서 1을 추가해준후에 q에 좌표 추가
            q.append((ny,nx))
ans = 0
cnt = 0
for i in range(N):
    cnt += farm[i].count(0) # 0이 있는지 없는지 확인
if cnt >=1: # 0이 있다면 완료를 못했다는 뜻이므로 -1을 출력
    print(-1)
else:   # 0이 없다면 완료 했다는 뜻이므로 마지막 일을 찾아서 출력
    for i in range(N):
        temp = max(farm[i])
        ans=max(temp,ans)
    print(ans-1)
