from collections import deque
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    nums =deque(list(input()))
    lst = []
    j = 0
    while j < N//4:
        a = nums.popleft()
        nums.append(a)
        for i in range(0,len(nums)-(N//4-1), N//4):
            word = ''
            x = i
            while x < (i+(N//4)):
                word += nums[x]
                x += 1
            if word not in lst:
                lst.append(word)
        j +=1

    for i in range(len(lst)):
        lst[i] = int(lst[i],16)
    lst.sort(reverse=True)

    print(f'#{tc} {lst[K-1]}')