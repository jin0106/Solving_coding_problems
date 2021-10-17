N = list(map(int, input()))
nums = [0]* 11  # 입력 받은 번호들 count 해 줄 리스트
lst = [0]* 11 # 0 0 0 0 .. 초기화 리스트
for i in range(len(N)):
    nums[N[i]]+= 1 # 입력 받은것들 하나씩 카운트

ans = 0

while nums != lst:
    for i in range(len(nums)):
        if nums[i]>0:   # 0보다 크면 -1
            nums[i]-=1
        elif i == 6 and nums[6] ==0 and nums[9]>0:  # 숫자 6인데 6이 0 이면 9를 사용
            nums[9]-=1
        elif i == 9 and nums[9] ==0 and nums[6]>0:  # 숫자 9인데 9이 0 이면 6를 사용
            nums[6] -=1

    ans +=1 # 한 번 다 돌고 안끝나면 추가
print(ans)