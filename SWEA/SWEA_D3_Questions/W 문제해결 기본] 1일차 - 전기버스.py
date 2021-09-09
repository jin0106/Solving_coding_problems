T = int(input())
for t in range(1, T+1):
    K, N, M = map(int, input().split())
    M = list(map(int, input().split()))
    line = []
    for i in range(N+1):
        line.append(i)
    cnt = 0
    n = 0
    for x in range(len(M)-1):
        if n + K >= N:
            break
        elif M[x] < n+K and M[x+1] == n+K:
            n += K
            cnt += 1
        elif M[x] < n+K and M[x+1] > n+K:
            if M[x+1] > n+K:
                cnt = 0
                break
            else:
                n = M[x]
                cnt += 1

        elif M[x] < n+K and M[x+1] < n+K:
            n = M[x+1]
            cnt += 1

    print("#{} {}".format(t, cnt))


# 3
# 3 10 5
# 1 3 5 7 9
# 3 10 5
# 1 3 7 8 9
# 5 20 5
# 4 7 9 14 17
