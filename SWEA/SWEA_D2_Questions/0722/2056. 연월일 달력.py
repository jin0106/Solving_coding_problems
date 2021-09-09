# 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.


# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면

# # [그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,

# # 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.


# # 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며

# # 일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.


# # ※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)


# # [입력]

# # 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

# # 다음 줄부터 각 테스트 케이스가 주어진다.


# # [출력]

# # # 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

# # # (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


# 31 - 1, 3, 5, 7, 8, 10, 12
# 30 - 4, 6, 9, 11
# 28 - 2

T = int(input())   # 테스트 횟수 지정

for i in range(1, T+1):  # 반복
    date = input()  # 날짜 입력
    year = int(date[:4])  # 년 월 일 구분
    month = int(date[4:6])
    day = int(date[6:])

    if month > 12 or month < 1:  # 월의 범위 지정
        print("#{} -1".format(i))
        continue
    elif month in [1, 3, 5, 7, 8, 10, 12]:  # 지정월들의 일 범위 지정
        if day > 31 or day < 1:
            print("#{} -1".format(i))
            continue
    elif month in [4, 6, 9, 11]:
        if day > 30 or day < 1:
            print("#{} -1".format(i))
            continue
    elif month == 2:
        if day > 28 or day < 1:
            print("#{} -1".format(i))
            continue
    print("#%s %04d/%02d/%02d" % (i, year, month, day))
