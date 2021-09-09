# 틱택톰은 틱택토를 변형한 게임으로, 4 x 4 게임판에서 진행한다. 처음에 판에는 최대 하나의 ‘T’ 가 16개의 격자 중 하나에 있고, 나머지 격자 칸은 비어 있다. 두 플레이어 X, O 가 게임을 한다. 처음에는 X가 진행하며, 이후 두 사람은 번갈아서 턴을 바꾸며 게임을 진행한다. 각 턴에 플레이어는 빈 칸에 하나의 말을 놓는다. X가 놓은 말에는 ‘X’, O가 놓은 말에는 ‘O’ 가 적혀 있다.
# 턴이 끝난 이후, 어떠한 행, 열, 그리고 두 대각선 중 하나가 4개의 같은 말을 포함하거나, 3개의 같은 말과 ‘T’ 를 포함하면, 해당 말의 주인이 이기고 게임이 끝난다. 그렇지 않은 경우 게임은 계속된다. 모든 칸이 다 찼는데 게임이 끝나지 않았다면, 동점으로 게임이 끝난다.
# 'X', 'O', 'T' 와 '.' 를 포함하는 4 x 4 판이 주어진다 ('.' 는 빈 칸을 뜻함). 이 판은 게임의 현재 상태를 표현한다. 이를 토대로 현재 틱택톰 게임이 어떻게 진행되어 있는지 판단하라. 결과는 다음 4가지 중 하나이다.
#
# ∙ “X won” (게임이 끝났고 X가 이김)
# ∙ "O won" (게임이 끝났고 O가 이김)
# ∙ "Draw” (게임이 끝났고 동점)
# ∙ "Game has not completed" (게임이 안 끝남)
#
# [입력]
# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 각 테스트 케이스는 다음과 같이 구성되었다.
# ∙ 4개의 줄에 'X', 'O', 'T' 와 '.' 를 포함하는 4 x 4 판이 주어진다.
# ∙ 정상적인 게임의 진행 도중에 나온 입력임이 보장된다. 고로 위 4개의 결과가 모호하지 않게 판단될 수 있다.
#
# [출력]
# 각 테스트 케이스마다 결과를 출력하라.

# import sys
# sys.stdin = open('tic.txt','r')

def row(MAP,c,r, key):  # 가로 검사
    global ans
    cnt = 0
    while r <= 3:
        if field[c][r] == key:
            cnt +=1
        elif field[c][r] == "T":
            cnt +=1
        else:
            break
        r += 1
    if cnt == 4:
        ans = key+' won'
    return

def column(MAP,c,r, key):   # 세로 검사
    global ans
    cnt = 0
    while c <= 3:
        if field[c][r] == key:
            cnt += 1
        elif field[c][r] == "T":
            cnt += 1
        else:
            break
        c += 1
    if cnt == 4:
        ans = key+' won'
    return

def diagonal_1(MAP,c,r, key):
    global ans
    cnt = 0
    i=0
    while c+i <= 3:
        if field[c+i][r+i] == key:  # 우하향 대각선이므로 i 값 c와r에 각각 더해주기
            cnt += 1
        elif field[c+i][r+i] == "T":
            cnt += 1
        else:
            break
        i +=1
    if cnt == 4:
        ans = key+' won'
    return

def diagonal_2(MAP,c,r, key):
    global ans
    cnt = 0
    i=0
    while r+i <= 3:
        if field[c-i][r+i] == key:      # 우상향 대각선이므로 c는 빼주고 r은 더해주기
            cnt += 1
        elif field[c-i][r+i] == "T":
            cnt += 1
        else:
            break
        i +=1
    if cnt == 4:
        ans = key+' won'
    return


T = int(input())
for t in range(T):
    if t < T-1:
        field = [list(input()) for _ in range(5)]       # 한 줄 공백 감안해서 입력 받기
    else:
        field = [list(input()) for _ in range(4)]       # 마지막 테스트케이스는 공백 없음.
    ans ='1'
    # 가로 검사
    for y in range(4):
        for x in range(1):
            if field[y][x] == 'X' or field[y][x] =='T':     # X이거나 T이면
                row(field, y, x, "X")
            if field[y][x] == "O" or field[y][x] =='T':     # O이거나 T이면
                row(field, y, x, "O")

    # 세로 검사
    if ans == '1':
        for y in range(1):
            for x in range(4):
                if field[y][x] == "X" or field[y][x]=='T':  # X이거나 T이면
                    column(field, y, x, "X")
                if field[y][x] == 'O' or field[y][x]=='T':  # O이거나 T이면
                    column(field, y, x, "O")
    else:
        pass

    # 대각선 검사 1
    if ans == '1':
        if field[0][0] == "X" or field[0][0] =="T" :     # X이거나 T이면
            diagonal_1(field, 0, 0, "X")
        if field[0][0] == "O" or field[0][0] =="T" :    # O이거나 T이면
            diagonal_1(field, 0, 0, "O")
    else:
        pass
    if ans=='1':
        # 대각선 검사 2
        if field[3][0] == "X" or field[3][0] =="T":
            diagonal_2(field, 3, 0, "X")
        if field[3][0] == "O" or field[3][0] =="T":
            diagonal_2(field, 3, 0, "O")
    else:
        pass

    if ans == '1':
       for i in range(4):
           if '.' in field[i]:
                ans = 'Game has not completed'      # .이 하나라도 있으면 바로 브레이크
                break
           else:
                ans = 'Draw'
    print(f'#{t+1} {ans}')


