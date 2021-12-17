
nums = []
for _ in range(9):
    nums.append(int(input()))
value = sum(nums)-100

for i in range(9):
    for j in range(9):
        if i != j and nums[i] + nums[j] == value:
            idx1, idx2 = nums[i], nums[j]
            break
nums.pop(nums.index(idx1))
nums.pop(nums.index(idx2))
for i in sorted(nums):
    print(i)
