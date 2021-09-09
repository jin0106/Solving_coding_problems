n = int(input())
nums = list(map(int, input().split()))
x = int(input())
ans = 0
nums.sort()
left, right = 0, n-1
while left < right:
    if nums[left]+ nums[right] == x:
        ans +=1
        right -=1
        left +=1
    elif nums[left]+nums[right] > x:
        right -=1
    else:
        left +=1
print(ans)