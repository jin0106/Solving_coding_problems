N = int(input())
arr = list(map(int, input().split()))
memorization = [0]


for case in arr:
    if memorization[-1] < case:
        memorization.append(case)
    else:
        left = 0
        right = len(memorization)

        while left < right:
            mid = (left+right) // 2

            if memorization[mid] < case:
                left = mid +1
            else:
                right = mid
        memorization[right] = case
print(len(memorization)-1)