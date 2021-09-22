a = []
for _ in range(5):
    a.append(int(input()))

for i in range(5):
    if a[i] <40:
        a[i] = 40
avg = sum(a)/5
print(int(avg))