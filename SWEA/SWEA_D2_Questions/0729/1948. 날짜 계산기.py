# 월 일로 이루어진 날짜를 2개 입력 받아, 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력하는 프로그램을 작성하라.


# [제약 사항]

# 월은 1 이상 12 이하의 정수이다. 각 달의 마지막 날짜는 다음과 같다.

# 1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31

# 두 번째 날짜가 첫 번째 날짜보다 항상 크게 주어진다.


# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 4개의 수가 주어진다.

# 첫 번째 수가 월을 나타내고 두 번째 수가 일을 나타낸다. 그 다음 같은 형식으로 두 번째 날짜가 주어진다.

T = int(input())

for i in range(1, T+1):
    M1, D1, M2, D2 = map(int, input().split())  # 날짜 입력
    m_31 = [1, 3, 5, 7, 8, 10, 12]          # 31일을 가진 달
    m_30 = [4, 6, 9, 11]                    # 30일을 가진 달
    if M1 == M2:                       # 입력한 두달이 같으면 일끼리만 계산
        result = D2-D1
    else:
        result = 0
        while True:  # 입력한 두달이 다르면 M2를 -1 씩 하면서 M2-1이 31일 가진달인지 30일 가진달인지 확인후 result에 값을추가
            M2 -= 1  # M2와 M1의 값이 같아지면 M1이 어디에 속한지 확인하고 그 달의 날짜수에서 D1을 빼준 값을 result에 추가
            if M2 == M1:  # 마지막으로 D2의 값추가와 기준일때문에 +1
                if M2 in m_31:
                    result += (31-D1)
                    break
                elif M2 in m_30:
                    result += (30-D1)
                    break
                else:
                    result += (28-D1)
                    break
            elif M2 in m_31:
                result += 31
            elif M2 in m_30:
                result += 30
            elif M2 == 2:
                result += 28
        result += D2
    print(f'#{i} {result+1}')
