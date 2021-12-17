N = int(input())
candy = [list(input()) for _ in range(N)]

max_cnt = 0


def find_max():
    global max_cnt
    for i in range(N):
        cnt = 1
        cnt_row = 1
        for j in range(N-1):
            if candy[i][j] == candy[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > max_cnt:
                max_cnt = cnt
            if candy[j][i] == candy[j+1][i]:
                cnt_row += 1
            else:
                cnt_row = 1
            if cnt_row > max_cnt:
                max_cnt = cnt_row


for i in range(N):
    for j in range(N-1):
        if candy[i][j] != candy[i][j+1]:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            find_max()
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        if candy[j][i] != candy[j+1][i]:
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
            find_max()
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]


print(max_cnt)
