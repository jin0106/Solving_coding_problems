import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    nums = list(sys.stdin.readline().rstrip() for _ in range(n))
    numbs.sort()

    for i in range(len(nums)-1):
        if nums[i] in nums[i+1][:len(nums[i])]:
            print("NO")
            break
    else:
        print("YES")
