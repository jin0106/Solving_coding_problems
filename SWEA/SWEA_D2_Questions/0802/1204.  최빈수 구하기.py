T = int(input())

for i in range(1, T+1):
    t = int(input())
    max_cnt = 0
    nums = list(map(int, input().split()))

    for x in range(101):
        if nums.count(x) == 0:
            continue
        elif nums.count(x) > nums.count(max_cnt):
            max_cnt = x

        elif nums.count(x) == nums.count(max_cnt):
            if x > max_cnt:
                max_cnt = x
    print(f"#{t} {max_cnt}")
