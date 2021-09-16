def dfs(n,value,cnt):
    global max_num
    global min_num

    if cnt == N:
        max_num = max(max_num, value)
        min_num = min(min_num, value)
        return


    for i in range(4):
        if operator[i] >=1:
            if i ==0:
                operator[i] -= 1
                dfs(n+1,value+nums[n],cnt+1)
                operator[i] += 1
            elif i == 1:
                operator[i] -= 1
                dfs(n+1, value-nums[n],cnt+1)
                operator[i] += 1
            elif i == 2:
                operator[i] -= 1
                dfs(n+1, value*nums[n],cnt+1)
                operator[i] += 1
            elif i == 3:
                operator[i] -= 1
                dfs(n+1, int(value / nums[n]),cnt+1)
                operator[i] += 1

    return
import sys

N = int(sys.stdin.readline())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))
check = [0,0,0,0]
t = 0
max_num = -sys.maxsize
min_num = sys.maxsize

dfs(1,nums[0],1)
print(max_num)
print(min_num)
