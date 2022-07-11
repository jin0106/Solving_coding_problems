import sys
input = sys.stdin.readline
import heapq

V,E = map(int, input().split())
K = int(input())
arr = [list(map(int, input().split())) for _ in range(E)]
graph = [[] for _ in range(V+1)]
distance = [float('INF')]*(V+1)
for a,b,c in arr:
  graph[a].append((b,c))


def djs(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))




djs(K)
print(distance)
for i in range(V):
  print('INF' if distance[i+1] == float('INF') else distance[i+1])