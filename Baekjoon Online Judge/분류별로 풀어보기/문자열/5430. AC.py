from collections import deque
import sys

T = int(input())
for tc in range(1,T+1):
    flag = True # 에러 확인 용
    command = list(sys.stdin.readline().rstrip())
    N = int(input())
    a = sys.stdin.readline().rstrip()[1:-1].split(",")  # [] , 빼고 받기위해서 슬라이싱과 split사용
    q = deque(a) #  deque 적용
    cnt = 0

    if N ==0:   # 빈값이 들어와도 " 가 들어가서 q길이가1 이되므로 N이 0일때는 q길이를 0으로 만들어줌
        q =[]

    for i in command:
        if i == 'R':
            cnt +=1 # reverse를 계속하면 시간초과가 떠서 짝수면 그대로 두고 홀수면 reverse 실행
        elif i =='D':
            if len(q) <1:
                flag = False
                break
            elif cnt%2==0:  # 만약 짝수면 맨 앞에꺼 제거
                q.popleft()
            elif cnt%2==1:  # 홀수이면 맨 뒤에꺼 제거(reverse 안한 상태이므로 맨 뒤에께 원래 제일 앞에 위치해야함)
                q.pop()

    if cnt % 2 == 1:
        q.reverse()

    if not flag:
        print('error')
    else:
        print("["+','.join(q)+"]")