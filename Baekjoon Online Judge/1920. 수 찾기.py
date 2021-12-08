N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
m = list(map(int, input().split()))

ans =[]

def binary_search(num, arr, start,end):
    if start> end:
        return 0
    middle = (start+end)//2

    if num == arr[middle]:
        return 1
    elif arr[middle] > num:
        return binary_search(num, arr, start, middle-1)
    else:
        return binary_search(num, arr, middle+1, end)


for i in m:
   print((binary_search(i, A, 0, N-1)))
