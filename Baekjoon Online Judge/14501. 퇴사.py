N = int(input())
date =  [0] * (N+1)
price = [0] * (N+1)
max_paid = 0
a = N+1
for i in range(N):
    t, p = map(int, input().split())
    date[i+1] = t
    price[i+1] = p
for j in range(N, -1, -1):
    if date[j]+j >a:
        continue
    else:
        if price[j]+price[date[j]] > price[j-1]+price[date[j-1]]:
            max_paid += price[j]
            a = j
print(max_paid)

ø