from collections import deque

def dfs(start, visited={},result=[]):
    visited[start] = True   # 처음에는 리스트로 작성을 했는데 시간초과가 나서 dict로 바꿔줌
    result.append(start)    # print 반복보다 append하고 한번에 출력하는게 더 빠를거같아서. 확실하지 않음.
    for w in range(len(graph[start])):
        if w not in visited and graph[start][w] == 1:   # 방문하지 않았고 서로 연결 되어있으면
            dfs(w, visited) # 재귀
    return result

def bfs(start,visited={}):
    queue= deque()
    queue.append(start)
    visited[start] =True
    ans = []
    while queue:
        x = queue.popleft() # 제일 앞에꺼를 꺼냄
        ans.append(x)   # ans에 추가
        for w in range(len(graph[start])):
            if w not in visited and graph[x][w] == 1:   # 방문하지 않았고 연결되어있으면
                visited[w] = True   # 방문 체크
                queue.append(w) # queue에 값들 추가
    return ans


N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for m in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
print(*dfs(V))
print(*bfs(V))
