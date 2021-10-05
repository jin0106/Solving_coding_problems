T = int(input())



def dfs(cnt):
    global ans

    if cnt == limit or cnt==length:
        a = 0
        for n in arr:
            a *= 10
            a += (int(n))

        if a > ans:
            ans = a
        return

    for i in range(length-1):
        for j in range(i+1, length):
            arr[i], arr[j] = arr[j], arr[i]
            dfs(cnt+1)
            arr[j], arr[i] = arr[i], arr[j]
for t in range(1, T+1):
    ans = -1
    num, c = input().split()
    arr = list(num)
    limit = int(c)
    length = len(arr)
    dfs(0)
    print(f'#{t} {ans}')
