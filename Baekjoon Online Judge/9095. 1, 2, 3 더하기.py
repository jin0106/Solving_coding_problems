

def sum_num(n, value):
    global ans

    if value > n:
        return
    if value == n:
        ans += 1
        return

    for i in range(1, 4):
        sum_num(n, value+i)
    return


T = int(input())


for _ in range(T):
    ans = 0
    n = int(input())
    sum_num(n, ans)
    print(ans)
