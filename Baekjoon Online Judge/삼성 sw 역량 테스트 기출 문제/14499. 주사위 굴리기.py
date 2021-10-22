N, M, y, x, K = map(int, input().split())   # N세로
Map = [list(map(int, input().split())) for _ in range(N)]
comm = list(map(int, input().split()))
dice = [0,0,0,0,0,0]    # 처음 주사위

def rota(n):
    if n == 1:
        dice[1], dice[3], dice[4],dice[5] = dice[4], dice[5],dice[3],dice[1]
    elif n == 2:
        dice[1], dice[3],dice[4], dice[5] = dice[5],dice[4],dice[1],dice[3]
    elif n ==3 :
        dice[0], dice[1], dice[2],dice[3]  = dice[1],dice[2],dice[3],dice[0]
    else:
        dice[0],dice[1], dice[2],dice[3] = dice[3], dice[0], dice[1],dice[2]

    return

def pr():
    if Map[y][x] == 0:
        Map[y][x]=dice[3]
    else:
        dice[3] = Map[y][x]
        Map[y][x] = 0
    print(dice[1])


for i in comm:
    if i == 1 and x+1 <M:   # 동쪽 이동
        x +=1
        rota(i)
        pr()    # 지도 내에서만 주사위 번호 교체 및 프린트

    elif i == 2 and x-1 >= 0:   # 서쪽 이동
        x -=1
        rota(i)
        pr()

    elif i ==3 and y-1 >=0: # 북쪽이동
        y -=1
        rota(i)
        pr()

    elif i == 4 and y+1 <N: # 남쪽 이동
        y+=1
        rota(i)
        pr()



