from collections import deque

n, k = map(int, input().split())
q = deque()

for i in range(1, n + 1):
    q.append(i)

li = []

while q:
    for _ in range(k - 1):
        q.append(q.popleft())
    li.append(q.popleft())

print("<"+ ', '.join(map(str,li))  +">")