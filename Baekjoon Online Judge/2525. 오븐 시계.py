hour, minu = map(int, input().split())
take = int(input())

h = (minu+take) // 60
if h >= 1:
    hour += h
    minu = (minu+take)-(60*h)
else:
    minu = (minu+take)
if hour>=24:
    hour -= 24

print(hour, minu)
