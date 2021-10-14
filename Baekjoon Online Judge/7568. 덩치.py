N = int(input())
h = []
w = []
ans = [0] *  N
for _ in range(N):
    a, b = map(int, input().split())
    w.append(a)
    h.append(b)

for i in range(N):
    cnt = 1
    for j in range(N):
        if h[i]< h[j] and w[i]<w[j]:
            cnt +=1
    ans[i] = cnt
print(*ans)