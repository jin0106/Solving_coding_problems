
# N2개의 방이 N×N형태로 늘어서 있다.
# 
# 위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j가 적혀 있으며, 이 숫자는 모든 방에 대해 서로 다르다.
# 
# 당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.
# 
# 물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
# 
# 처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.
# 
# 
# [입력]
# 
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N (1 ≤ N ≤ 103)이 주어진다.
# 
# 다음 N개의 줄에는 i번째 줄에는 N개의 정수 Ai, 1, … , Ai, N (1 ≤ Ai, j ≤ N2) 이 공백 하나로 구분되어 주어진다.
# 
# Ai, j는 모두 서로 다른 수이다.
# 
# 
# [출력]
# 
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 
# 한 칸을 띄운 후, 처음에 출발해야 하는 방 번호와 최대 몇 개의 방을 이동할 수 있는지를 공백으로 구분하여 출력한다.
# 
# 이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것을 출력한다.


from collections import deque

def bfs(y,x):
    global cnt
    q = deque()
    q.append((y,x))
    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y + dr[i]
            nx = x + dc[i]

            if 0<=ny<N and 0<=nx<N:
                if room[ny][nx] == room[y][x] +1:    # 바로 직전 위치보다 정확히 1보다 크면 이동
                    q.append((ny,nx))
                    cnt +=1


dr = [-1,1,0,0]
dc = [0,0,-1,1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    start = float('inf')
    for y in range(N):
        for x in range(N):
            cnt =0
            bfs(y,x)
            if cnt > ans:   # cnt가 ans보다 많으면 cnt를 ans로 설정하고 시작 좌표 start에 저장
                ans = cnt
                start = room[y][x]
            elif cnt == ans:    # 만약 cnt와 ans가 같으면 더 작은 값을 start 값으로 저장
                if start > room[y][x]:
                    start = room[y][x]


    print(f'#{tc} {start} {ans+1}')
