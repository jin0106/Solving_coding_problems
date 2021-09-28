from collections import deque


T = int(input())
for t in range(1, T+1):
    H, W, N = map(int, input().split())
    area = [list(input()) for _ in range(H)]    # 지도

    ans = 0

    dr = [-1, 1, 0, 0]  # 상하좌우 탐색
    dc = [0, 0, -1, 1]
    a, b = 0, 0
    for i in range(1, N+1):  # 1번부터 N번까지 순서대로 찾기
        visit = [[0]*W for _ in range(H)]    # 방문 기록
        visit[a][b] = 1  # 처음시작 1
        q = deque()
        q.append((a, b))

        while q:
            y, x = q.popleft()

            if area[y][x] == str(i):    # 만약 i를 찾으면
                ans += visit[y][x]  # visit[y][x]의 값을 ans에 더해주기
                a, b = y, x
                q = deque()
                break

            for j in range(4):
                ny = y + dr[j]
                nx = x + dc[j]
                # 인덱스 범위 내에 있고 같은경로 반복 피하긴
                if 0 <= ny < H and 0 <= nx < W and not visit[ny][nx] == visit[y][x] + 1:
                    if area[ny][nx] != '#' and not visit[ny][nx]:   # 벽이아니고 visit[ny][nx]가 0이 아니면
                        visit[ny][nx] = visit[y][x] + 1  # 이전 기록에서 1 추가
                        q.append((ny, nx))

    print(f'#{t} {ans-N}')
