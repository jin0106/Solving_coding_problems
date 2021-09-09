def row(arr):
    total = 0
    idx = 0
    i =0
    while arr[y][x + i] != 0:
        total += arr[y][x + i]
        i += 1
        if x+i == H:
            idx = x+i
            break
        if arr[y][x + i] == 0:
            idx = x + i

    for a in range(y+1,W):
        i =0
        if arr[a][x] ==0:
            break
            return total
        else:
            while arr[a][x] != 0:
                total += arr[a][x+i]
                i +=1
                if x+i == idx:
                    break
    return total




T = int(input())
for t in range(1,T+1):
    W, H = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(W)]
    max_v =0
    for y in range(W):
        for x in range(H):
            if land[y][x] != 0:
                ans =row(land)
                if ans >max_v:
                    max_v = ans
    print(f'#{t} {max_v}')