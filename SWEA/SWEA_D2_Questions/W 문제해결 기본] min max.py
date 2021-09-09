T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    min_num = nums[0]
    max_num = 0

    for i in range(len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
        if nums[i] < min_num:
            min_num = nums[i]
    value = max_num - min_num
    print(f'#{t} {value}')
