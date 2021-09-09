# 정수론에서, 세 소수 문제란 다음과 같다.

# “5보다 큰 모든 홀수는 정확히 세 소수의 합으로 표현될 수 있다. (같은 소수를 합에 사용해도 된다.)”

# 예를 들어, 7 = 2 + 2 + 3, 11 = 2 + 2 + 7, 25 = 7 + 7 + 11로 나타낼 수 있다.

# 1939년 러시아 수학자 I. M. Vinogradov는 충분히 큰 홀수는 세 소수의 합으로 표현할 수 있다는 것을 증명했다.

# 여기서 충분히 크다는 것은 3315 ≈ 107000000 이상의 수라는 의미이다.

# 현재 가장 발전된 하한은 약 e3100 ≈ 101346 이상의 수이다.

# 러시아 수학자 I. M. Vinogradov 를 존경하는 새샘이는 직접 세 소수 문제를 풀어보기로 했다.

# 하지만 이 수는 너무 크기 때문에 컴퓨터로도 이 범위까지의 모든 수를 증명할 수는 없었다.

# 대신 어떤 크지 않은 홀수에 대해, 세 소수의 합으로 나타낼 수 있는 경우의 수를 구하기로 했다.

# 5보다 큰 홀수 N을 입력 받아 N = x + y + z (단, x ≤ y ≤ z 이고, x, y, z는 소수) 로 나타나는 경우의 수를 구하는 프로그램을 작성

# 하라.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에 하나의 정수 N ( 7 ≤ N ≤ 999 ) 이 주어진다.

# N은 홀수이다.


# [출력]

# 각 테스트 케이스마다 첫 번째 줄에는 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

# N을 세 소수의 합으로 나타낼 수 있는 경우의 수를 출력한다.


prime = list(range(2, 1001))     # 미리 소수 리스트를 만들어줌
for i in range(2, 1000):
    for j in range(i+i, 1001, i):
        if j % i == 0 and j in prime:
            prime.remove(j)


T = int(input())
for t in range(1, T+1):
    ans = 0
    N = int(input())
    for i in range(len(prime)):     # 3중 for문으로 완전 탐색. N보다 커지면 바로 break
        if prime[i] >= N:
            break
        for j in range(i, len(prime)):
            if prime[j] >= N:
                break
            for k in range(j, len(prime)):
                if prime[k] >= N:
                    break
                if prime[i] + prime[j] + prime[k] == N:
                    ans += 1
    print("#{} {}".format(t, ans))
