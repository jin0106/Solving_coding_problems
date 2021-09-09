T = int(input())
for t in range(1, T+1):
    nums = list(map(int, input().split()))
    sum_list = []
    for i in range(5):
        for j in range(i+1, 6):
            for k in range(j+1, 7):
                if nums[i]+nums[j]+nums[k] not in sum_list:     # 3중 for문을 세 값을 더한뒤 중복 아니면 sum_list에 추가
                    sum_list.append(nums[i]+nums[j]+nums[k])
    # sort_lst = list(reversed(sum_list))   reversed는 정렬을 반대로 할뿐 내림차순으로 변경되는것이 아니다.
    sum_list.sort(reverse=True) # 큰 순서대로이므로 reverse사용하여 내림차순으로 정렬
    print("#{} {}".format(t, sum_list[4]))

