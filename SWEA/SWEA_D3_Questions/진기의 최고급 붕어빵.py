T = int(input())
for t in range(1,T+1):
    N, M, K = map(int, input().split())
    customers = sorted(list(map(int, input().split())))
    waiting  = N
    ans = "Possible"
    visit = 0
    for i in range(N):
        if (customers[i]//M)*K - visit  <=0:      # 손님이 왔어도 그 시간 전에 만들수 있는 갯수가 적으면
            ans ="Impossible"
            break
        else:
            visit +=1
    print("#{} {}".format(t, ans))



