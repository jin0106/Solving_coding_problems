

N = int(input())
lst = list(map(int, input().split()))
ans = []
for i in range(N):
    if i == N-1:
        ans.append(-1)
    else:
        temp = lst[i]
        for j in range(i+1, N):
            if temp < lst[j]:
                temp = lst[j]
                ans.append(temp)
                break
        else:
            ans.append(-1)
print(*ans)
