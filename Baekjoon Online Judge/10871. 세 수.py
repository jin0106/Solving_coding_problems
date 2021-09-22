a = list(map(int, input().split()))

max_num = max(a)
min_num = min(a)
a.remove(min_num)
a.remove(max_num)
print(*a)