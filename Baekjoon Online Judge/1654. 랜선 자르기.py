K, N = map(int,input().split())
length = []
for _ in range(K):
    length.append(int(input()))
start, end = 1, max(length)

while start<=end:
    mid = (start+end)//2
    lines =0
    for i in length:
        lines += i//mid

    if lines>= N:
        start=mid+1
    else:
        end = mid-1
print(end)

