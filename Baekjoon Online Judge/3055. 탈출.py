from collections import deque
import sys

def bfs(y,x,cnt,visit):
    global ans

    q = deque()
    q.append((y,x))

    if y == M-1 and x == N-1:
        ans = min(cnt,ans)
        return

    while q:

        for i in range(4):
            ny = y + dr[i]
            nx = x + dc[i]

            if 0 <= ny < M and 0 <= nx < N:
                if maze[ny][nx] == '1' and visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    bfs(ny,nx,cnt+1,visit)

                elif maze[ny][nx] == '0' and visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    bfs(ny,nx,cnt, visit)




N, M = map(int, input().split())
maze = [list(input()) for _ in range(M)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

visited = [[0]*N for _ in range(M)]
ans = sys.maxsize

bfs(0,0,0,visited)

print(ans)


