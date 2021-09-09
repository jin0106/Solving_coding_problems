def dfs(start, visited={}):
    global cnt
    visited[start] = True
    cnt +=1
    for n in range(N+1):
        if graph[start][n] == 1 and n not in visited:
            dfs(n,visited)
    return

N = int(input()) # 컴퓨터의 수
L = int(input()) # 연결된 컴퓨터 쌍의 수

graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(L):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
cnt =0
dfs(1)
print(cnt-1)