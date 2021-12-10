N= input()


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr)//2

    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    low, high = 0, 0
    merged_arr = []
    while low < len(low_arr) and high < len(high_arr):
        if low_arr[low] < high_arr[high]:
            merged_arr.append(low_arr[low])
            low += 1
        else:
            merged_arr.append(high_arr[high])
            high += 1

    merged_arr += low_arr[low:]
    merged_arr += high_arr[high:]

    return sorted(merged_arr, reverse=True)

print(''.join(map(str,merge_sort(N))))
