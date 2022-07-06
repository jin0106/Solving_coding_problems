import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N)]
ans = False
visited = [False] * N

for _ in range(M):
  y, x = map(int, input().split())
  arr[y].append(x)
  arr[x].append(y)

def dfs(idx, num):
  global ans
  if num == 4:
    ans = True
    return
  for i in arr[idx]:
    if not visited[i]:
      visited[i] = True
      dfs(i, num +1)
      visited[i] = False


for i in range(N):
  visited[i] = True
  dfs(i,0)
  visited[i] = False

  if ans:
    print(1)
    break
if not ans:
  print(0)