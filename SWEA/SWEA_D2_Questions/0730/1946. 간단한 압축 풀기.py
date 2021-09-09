# 원본 문서는 너비가 10인 여러 줄의 문자열로 이루어져 있다.

# 문자열은 마지막 줄을 제외하고 빈 공간 없이 알파벳으로 채워져 있고 마지막 줄은 왼쪽부터 채워져 있다.

# 이 문서를 압축한 문서는 알파벳과 그 알파벳의 연속된 개수로 이루어진 쌍들이 나열되어 있다. (예 : A 5    AAAAA)

# 압축된 문서를 입력 받아 원본 문서를 만드는 프로그램을 작성하시오.

# [예제]
# 압축된 문서의 내용

# A 10
# B 7
# C 5


# 압축을 풀었을 때 원본 문서의 내용

# AAAAAAAAAA
# BBBBBBBCCC
# CC


# [제약사항]

# 1. 압축된 문서의 알파벳과 숫자 쌍의 개수 N은1이상 10이하의 정수이다. (1 ≤ N ≤ 10)

# 2. 주어지는 알파벳 Ci는 A~Z의 대문자이다. (i는 줄의 번호로 1~N까지의 수)

# 3. 알파벳의 연속된 개수로 주어지는 수 Ki는 1이상 20이하의 정수이다. (1 ≤ Ki ≤ 20, i는 줄의 번호로 1~N까지의 수)

# 4. 원본 문서의 너비는 10으로 고정이다.


# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스에는 N이 주어지고 다음 줄부터 N+1줄까지 Ci와 Ki가 빈 칸을 사이에 두고 주어진다.


# [출력]

# 각 줄은 '#t'로 시작하고, 다음 줄부터 원본 문서를 출력한다.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

T = int(input())        # 테스트 케이스 입력

for i in range(1, T+1):
    N = int(input())    # N줄 입력
    a = ''      # 빈 str 생성
    cnt = 0         # 글자수를 새기 위한 cnt 생성
    for n in range(N):      # N만큼 돌기
        alp, num = input().split()
        word = str(alp)*int(num)    # 입력 받은 알파벳과 정수를 각 str타입과 int로 변환 후 곱하기
        # for문 이용해 한글자씩 돌면서 a에 추가 및 cnt +=1. 만약 cnt가 10으로 나눠지면 줄 바꿈.
        for w in word:
            a += w
            cnt += 1
            if cnt % 10 == 0:
                a += '\n'
    print(f"#{i}\n"+a)


# 처음에 보고 쉽다고 생각했었는데 문제를 제대로 이해하지 못해서였다.. 그렇게 어려웠던것은 아니지만 문제를 잘 읽고 확실히 이해한뒤 풀어야겠다고 다시 느끼게 해준 문제.
