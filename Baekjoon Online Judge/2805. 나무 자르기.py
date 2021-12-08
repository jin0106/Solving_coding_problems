N, M = map(int,input().split())
trees = sorted(list(map(int, input().split())))


start, end = 1, trees[-1]

def cut(num):
    value = 0
    for i in trees:
        if i > num:
            value += (i-num)
    return value

max_height = 0

while start<=end:
    mid = (start+end)//2

    if cut(mid) >= M:
        max_height = max(max_height, mid)
        start = mid +1
    else:
        end = mid-1
if len(trees) ==1:
    print(trees[0]-M)
else:
    print(max_height)

