N = int(input())

nums = []
for _ in range(N):
    x, y = map(int, input().split())
    nums.append([x,y])
nums.sort(key=lambda x:(x[0],x[1]))

for x, y in nums:
    print(x, y)