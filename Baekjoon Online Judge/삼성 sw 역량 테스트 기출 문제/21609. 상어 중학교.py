from collections import deque

def bfs(y,x):   # 가장 큰 블록 그룹 찾기

    temp_group = [] # 큰 블록 그룹 리스트 좌표들 추가 위해 빈 리스트 생성
    temp_group.append((y, x))   # 처음꺼 추가
    rainbow_lst = []    # 레인보우들 좌표 추가 위해 빈 리스트 생성
    color = nums[y][x]  # 일반블록의 색깔 설정
    block_cnt, rainbow_cnt = 1, 0 # 블록 개수, 무지개블록 개수

    q = deque()
    q.append((y,x))

    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y + dr[i]
            nx = x + dc[i]

            # 범위내에 있고 방문하지 않았고 일반 블록 일때
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx]==0 and nums[ny][nx] == color:
                visited[ny][nx] = 1
                block_cnt +=1
                q.append((ny,nx))
                temp_group.append((ny,nx))

            elif 0 <= ny < N and 0 <= nx < N and visited[ny][nx]==0 and nums[ny][nx] == 0:
                visited[ny][nx] = 1
                rainbow_cnt +=1
                block_cnt +=1
                q.append((ny,nx))
                rainbow_lst.append((ny,nx))
                temp_group.append((ny,nx))


    for y, x in rainbow_lst:    # 무지개 블럭들 방문 체크 해제
        visited[y][x] = 0

    return [block_cnt, rainbow_cnt, temp_group]


def remove(block):
    for y,x in block:   # block의 모든것들 삭제 해야하므로 -2로 변경
        nums[y][x] = -2

def gravity(nums):
    for i in range(N-2, -1, -1):
        for j in range(N):
            if nums[i][j] > -1: # -1보다 크면 검은색이 아니라는 뜻이므로
                r = i
                while True:
                    if 0 <= r+1 < N and nums[r+1][j] == -2: # 범위 내에 있고 만약 빈 블록 이면
                        nums[r+1][j] = nums[r][j]   # 계속 바꿔주기
                        nums[r][j] = -2
                        r +=1
                    else:
                        break

def rotate(nums):
    new_nums = [[0]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            new_nums[N-1-x][y] = nums[y][x] # 인덱스 이용하여 회전
    return new_nums



dr = [-1,1,0,0]
dc = [0,0,-1,1]

N, M = map(int, input().split())

nums = [list(map(int, input().split())) for _ in range(N)]
score = 0

while True:
    max_group = [0]
    visited = [[0] * N for _ in range(N)]


    for y in range(N):
        for x in range(N):  # 가장 큰 블록 그룹 찾기
            if nums[y][x] > 0 and visited[y][x] ==0:    # 일반블록 이고 방문 한적이 없으면
                visited[y][x] = 1   # 방문 체크후
                info = bfs(y,x)     # 블록 그룹 찾기

                if info[0] >= 2:    # 길이가 최소 2여야 하니깐
                    if info[0] > max_group[0]:  # 새로운게 더 크다면 교체
                        max_group = info
                    elif info[0] == max_group[0]:   # 만약 같다면
                        if info[1] > max_group[1]:  # 레인보우 갯수로 비교
                            max_group = info
                        elif info[1] == max_group[1]:   # 레인보우 갯수도 같다면
                            if info[2][0] > max_group[2][0]:    # 기준 블록의 행 숫자로 비교
                                max_group = info
                            elif info[2][0] == max_group[2][0]: # 기준블록의 행 숫자도 같다면 열로 비교
                                if info[2][1] > max_group[2][1]:
                                    max_group = info

    if max_group[0]<2:  # 2보다 작으면 브레이크
        break
    score += max_group[0]**2    # 스코어 계산

    remove(max_group[2])    # 블록 삭제

    gravity(nums)   # 중력

    nums = rotate(nums) # 90도 반시계 회전
    gravity(nums)   # 다시 중력


print(score)    # while끝나면 출력
