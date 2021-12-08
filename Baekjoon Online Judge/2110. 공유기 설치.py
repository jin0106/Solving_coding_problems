N, C = map(int, input().split())
homes = sorted(list(int(input()) for _ in range(N)))

start, end = 1, homes[-1]-homes[0]

result = 0

while start <= end :
    mid = (start + end) // 2
    current = homes[0]
    cnt = 1

    for i in range(1, N):
        if homes[i] >= current + mid :
            cnt += 1
            current = homes[i]

    if cnt >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)



