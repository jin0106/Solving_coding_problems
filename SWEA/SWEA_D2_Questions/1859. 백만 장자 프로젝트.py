T = int(input())
for t in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    ans = 0
    max_price = num[N-1]
    for i in range(N-2, -1, -1):
        if num[i] > max_price:
            max_price = num[i]
        else:
            ans += max_price - num[i]
    print(f'#{t} {ans}')
