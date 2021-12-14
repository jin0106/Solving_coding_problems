prices = list(map(int, input().split()))

ans = [0] * len(prices)


idx = len(prices) -1
for i in range(len(prices)-1):
    cnt = 1
    for j in range(i+1, len(prices)):
        if j == len(prices)-1:
            ans[i] = cnt
        elif prices[i] <= prices[j]:
            cnt += 1

        else:
            ans[i] = cnt
            break
print(ans)