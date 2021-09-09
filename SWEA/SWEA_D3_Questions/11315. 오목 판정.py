T = int(input())
for t in range(1, T+1):
    N = int(input())
    omok = [list(map(str, input())) for _ in range(N)]
    result = 0
    de = -1
    for x in range(N):
        for y in range(N):      # 이중 for문으로 가로 세로 확인
            if omok[x][y] == 'o':
                nx = x
                ny = y
                cnt = 0
                while ny < N:       # 가로
                    if omok[nx][ny] == 'o':
                        cnt += 1
                    else:
                        cnt = 0
                    if cnt >= 5:
                        result += 1
                    ny += 1
                cnt = 0
                nx = x
                ny = y
                while nx < N and ny < N:  # 세로
                    if omok[nx][ny] == 'o':
                        cnt += 1
                    else:
                        cnt = 0
                    if cnt >= 5:
                        result += 1
                    nx += 1
                cnt = 0
                nx = x
                ny = y
                while nx < N and ny < N:        # 우측하단
                    if omok[nx][ny] == 'o':
                        cnt += 1
                    else:
                        cnt = 0
                    if cnt >= 5:
                        result += 1
                    nx += 1
                    ny += 1
                cnt = 0
                nx = x
                ny = y
                while nx < N and ny < N:  # 좌측하단
                    if omok[nx][ny] == 'o':
                        cnt += 1
                    else:
                        cnt = 0
                    if cnt >= 5:
                        result += 1
                    nx += 1
                    ny -= 1
    if result >= 1:
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')
