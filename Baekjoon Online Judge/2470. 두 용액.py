import sys

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
left, right = 0, N-1
check = sys.maxsize
ans = []

while left< right:      # 처음에 시간 초과가 났었는데, 0 일 때의 조건식을 안넣었어서 그런거였다.
    value = nums[left]+nums[right]
    if abs(value) < check:
        check = abs(value)
        ans = [nums[left], nums[right]]
        if check == 0:
            break
    if value <0 :
        left +=1
    elif value > 0 :
        right-=1
print(*ans)