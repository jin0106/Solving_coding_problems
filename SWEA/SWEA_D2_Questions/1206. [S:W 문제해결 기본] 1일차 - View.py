tc = 10
for t in range(1, tc+1):
    N = int(input())
    apt_nums = list(map(int,input().split()))
    min_num =0
    for n in range(2, N-2):
        if apt_nums[n]-apt_nums[n+1] >=1 and apt_nums[n]-apt_nums[n+2]>=1 and apt_nums[n]-apt_nums[n-1]>=1 and apt_nums[n]-apt_nums[n-2]>=1:
            a1 = apt_nums[n]-apt_nums[n+1]
            a2 = apt_nums[n]-apt_nums[n+2]
            a3 = apt_nums[n]-apt_nums[n-1]
            a4 = apt_nums[n]-apt_nums[n-2]
            min_gap = a1

            for x in [a1,a2,a3,a4]:
                if min_gap > x:
                    min_gap = x
            min_num += min_gap
    print(f'#{t} {min_num}')
