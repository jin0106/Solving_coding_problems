def dfs(y,x):
    global cnt, visited, ans, ch

    cnt += 1
    ans = max(cnt, ans)

    for i in range(4):
        ny = y+dr[i]
        nx = x+dc[i]
        if 0<=ny<N and 0<=nx<N and visited[ny][nx] ==0:     # 인덱스 범위 설정 및 방문한적없을때
            if trail[ny][nx] < trail[y][x]: # 새로운 길이 기존의 길보다 낮을때
                visited[ny][nx] = 1 # 방문체크
                dfs(ny,nx)  # dfs
                visited[ny][nx] =0  # 방문 초기화
                cnt -=1# cnt -1
            elif ch ==0 and trail[ny][nx] >= trail[y][x]: # 만약 한번도 안깎았을대, 새로운 트레일 높이 -k가 기존 트레일보다 낮을때
                ch=1
                for i in range(1,K+1):  # 어떤게 최적의 값인지 모르므로 전부 다 탐색
                    trail[ny][nx] -= i  # 새로운 트레일 값 변경
                    if trail[ny][nx] < trail[y][x]: # i를 빼준값이 기존의 트레일 높이 보다 낮을때
                        visited[ny][nx] = 1 # 방문 체크
                        dfs(ny,nx)  # dfs
                        visited[ny][nx] = 0 # 방문 초기화
                        cnt -=1 # 카운트 초기화
                    trail[ny][nx] = trail[ny][nx] + i   # 다시 값 초기화
                ch =0
dr = [-1,1,0,0]
dc = [0,0,-1,1]


T = int(input())
for t in range(1,T+1):
    N, K = map(int, input().split())
    trail = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
    ans = 0
    for i in range(N):
        temp = max(trail[i])
        if max_num < temp:
            max_num = temp
    for y in range(N):
        for x in range(N):
            if trail[y][x] == max_num:
                cnt = 0
                ch = 0
                visited = [[0] * N for _ in range(N)]
                visited[y][x] =1
                dfs(y,x)


    print(f'#{t} {ans}')