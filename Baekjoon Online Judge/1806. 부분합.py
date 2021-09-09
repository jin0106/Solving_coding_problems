import sys

N, S = map(int, input().split())
se = list(map(int, input().split()))
left = 0
right = 0
ans = sys.maxsize
add = 0
while True :
    if add >= S:
        add -= se[left]
        left +=1
        ans = min(ans, right-left+1)
    else:
        if right == N:
            break
        else:
            add += se[right]
            right += 1
if ans == sys.maxsize:
    ans = 0
print(ans)



