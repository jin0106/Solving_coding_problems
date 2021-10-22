N, K = map(int, input().split())
arr = list(map(int, input().split()))
ans =0
robot = [0]*N   # N까지만


while True:
    ans += 1  # 1단계 벨트 회전
    temp = arr.pop()
    arr.insert(0, temp)
    temp = robot.pop()
    robot.insert(0, temp)
    robot[N-1] = 0       # 내리기

    for i in range(N-2,-1,-1): # 2단계 올라가있는 로봇 부터 이동
        if robot[i] and arr[i+1] and robot[i+1]==0:
            robot[i] = 0
            robot[i+1] = 1
            arr[i+1] -=1


    robot[N-1] =0

    if arr[0] and robot[0] == 0:  # 3단계 올리는 위치에 있는 칸의 내구도 0이 아니면 로봇 올림
        robot[0] =1
        arr[0] -=1

    cnt = arr.count(0) # 4단계 K 체크
    if cnt >= K:
        break

print(ans)


