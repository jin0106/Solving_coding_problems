e, s, m = map(int, input().split())
a = b = c = 0
i = 0
while True:
    if a == e and b == s and c == m:
        print(i)
        break
    a += 1
    b += 1
    c += 1
    i += 1
    if a == 16:
        a = 1
    if b == 29:
        b = 1
    if c == 20:
        c = 1
