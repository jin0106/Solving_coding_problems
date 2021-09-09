T = int(input())
for t in range(1,T+1):
    N = int(input())
    nums=[]
    for i in range(1,10):
        for j in range(1,10):
            if i*j not in nums:
                nums.append(i*j)
    if N in nums:
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')