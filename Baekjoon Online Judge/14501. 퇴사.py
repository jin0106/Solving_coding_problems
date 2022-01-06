N = int(input())
T, P = [], []

max_price = 0

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t), P.append(p)


def find_price(day, price):
    global max_price

    if day > N:
        return

    if day == N:
        max_price = max(price, max_price)
        return
    find_price(day+T[day], price+P[day])
    find_price(day+1, price)


find_price(0, 0)
print(max_price)
