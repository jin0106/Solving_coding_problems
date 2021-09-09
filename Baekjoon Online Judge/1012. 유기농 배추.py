import sys
sys.setrecursionlimit(10000)    # recursionlimit 늘려주기

def dfs(y,x):
    global cnt
    global visited
    cnt +=1
    visited[y][x] =1
    for i in range(4):
        ny = y + dr[i]
        nx = x + dc[i]
        if M >ny >=0 and N>nx>=0 and visited[ny][nx]==0 and farm[ny][nx]==1:
            dfs(ny,nx)

    return



dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


T = int(input())
for t in range(1,T+1):
    M,N,K = map(int, input().split())
    farm = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    cnt_lst = []
    for _ in range(K):
        y, x = map(int, input().split())
        farm[y][x] = 1
    for y in range(M):
        for x in range(N):
            cnt = 0
            if farm[y][x] == 1 and visited[y][x] ==0:
                dfs(y,x)
                cnt_lst.append(cnt)
    print(len(cnt_lst))
