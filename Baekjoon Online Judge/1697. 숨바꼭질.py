from collections import deque


def bfs():
    while q:
        i = q.popleft()
        if i == K:
            return time[i]
        for j in (i-1,i+1,2*i):
            if 0<= j <100001 and time[j] ==0:   # 인덱스 범위 설정 그리고 time[j] 체크
                time[j] = time[i] + 1   # 1초 추가
                q.append(j) # q에 추가


N, K = map(int, input().split())
q = deque()
q.append(N)

time = [0]*100001
print(bfs())
