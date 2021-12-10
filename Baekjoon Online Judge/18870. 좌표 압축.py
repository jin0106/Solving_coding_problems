import copy


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    low = high = 0

    merged_sort = []

    while low < len(low_arr) and high < len(high_arr):
        if low_arr[low] < high_arr[high]:
            merged_sort.append(low_arr[low])
            low += 1
        else:
            merged_sort.append(high_arr[high])
            high += 1

    merged_sort += low_arr[low:]
    merged_sort += high_arr[high:]

    return merged_sort

N = int(input())
nums = list(map(int, input().split()))
numbers = copy.deepcopy((nums))
nums = set(nums)
nums= list(nums)

sort_nums =merge_sort(nums)

ans = {}
for i in range(len(sort_nums)):
    if sort_nums[i] in ans:
        continue
    else:
        ans[sort_nums[i]] = i
for i in numbers:
    print(ans[i], end=' ')


