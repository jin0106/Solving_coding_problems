def draw(y, x, i, g):
    dragons[y][x] = 1   # 0 세대 첫 시작

    ny = y + dr[i]
    nx = x + dc[i]


    dragons[ny][nx] = 1 # 0세대 끝

    lst =[i]    # 방향 넣어주기

    for a in range(g):  # g-1 세대만큼
        length = len(lst)   # 이전 세대의 길이
        for j in range(length-1, -1, -1): # 이전세대 길이만큼
            new_d = (lst[j]+1) % 4     # 방향 설정
            ny += dr[new_d] # 좌표 구하기
            nx += dc[new_d]
            dragons[ny][nx] =1  # 체크
            lst.append(new_d)   # 추가


N = int(input())

ans = 0

dr = [0, -1, 0, 1] #0,1,2,3 숫자 방향대로
dc = [1, 0, -1, 0]

dragons = [[0]*101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    draw(y, x, d, g)

for i in range(100):    # 완전탐색
    for j in range(100):
        if dragons[i][j] == 1 and dragons[i][j+1] == 1 and dragons[i+1][j+1] == 1 and dragons[i+1][j] == 1:
            ans += 1

print(ans)