from collections import deque

# 90도 회전하기
def rotate():
    global ices
    # 격자범위
    lth = 2**l
    # 임시 얼음판
    temp = [[0]*(n) for _ in range(n)]

    for y in range(0,n,lth):
        for x in range(0,n,lth):
            for i in range(lth):
                for j in range(lth):
                    temp[y+j][x+(lth-1)-i] = ices[y+i][x+j]
    # 얼음 재지정
    ices = temp

# 제거하기
def remove():
    # 한번에 제거하기 위해 빈 리스트 생성
    temp = []

    for y in range(n):
        for x in range(n):
            cnt = 0
            for i in range(4):

                ny = y + dr[i]
                nx = x + dc[i]
                if 0 <= ny < n and 0 <= nx < n:
                    if ices[ny][nx]>0:
                        cnt +=1
            # cnt 3미만이면 1빼줘야 하므로 temp에 좌표 추가
            if cnt >=3:
                continue
            else:
                temp.append((y,x))

    # 한번에 빼주기
    for y,x in temp:
        ices[y][x] -=1

# 덩어리 구하기
def bfs(y,x):
    global min_block

    # 처음 y,x 좌표에도 얼음이 있으므로 1롲 ㅣ정
    block = 1
    q = deque()
    q.append((y,x))

    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dr[i]
            nx = x + dc[i]
            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx]==0:
                visited[ny][nx]=1
                if ices[ny][nx]>0:
                    block +=1
                    q.append((ny,nx))
    # q가 빈 리스트가 되면 연결되는것 다 더했다는 뜻이므로 최대값인지 비교
    if min_block < block:
        min_block = block

    return


dr = [-1,1,0,0]
dc = [0,0,-1,1]

N, Q = map(int, input().split())
n = 2**N
ices = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

min_block = 0
for i in range(Q):
    l = L[i]
    rotate()
    remove()



ans = 0

# 방문 기록
visited = [[0]*n for _ in range(n)]

# 남은 얼음 갯수 구하면서 최대 덩어리 구하기
for y in range(n):
    for x in range(n):
        if ices[y][x]>0:
            ans += ices[y][x]
        if visited[y][x] ==0 and ices[y][x]>0:
            visited[y][x] =1
            bfs(y,x)
print(ans)
print(min_block)