def bi(N):
    y = ''
    while N >0 :
        y=str(N%2)+y
        N//=2
    return y


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    y= ''.join(reversed(bi(M)))

    if y[0:N] == '1'*N:
        print(f"#{t} ON")
    else:
        print(f"#{t} OFF")




