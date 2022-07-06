import sys
input = sys.stdin.readline
from collections import deque


M,N = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
dist = [[-1]*M for _ in range(N)]
dist[0][0] = 0
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs():
  q = deque()
  q.append((0,0))

  while q:
    y,x = q.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]

      if 0 <= ny < N and 0 <= nx < M and dist[ny][nx] == -1:
        if maze[ny][nx] ==1:
          dist[ny][nx] = dist[y][x]+1
          q.append((ny,nx))
        elif maze[ny][nx] == 0:
          dist[ny][nx] = dist[y][x]
          q.appendleft((ny,nx))

bfs()
print(dist[N-1][M-1])