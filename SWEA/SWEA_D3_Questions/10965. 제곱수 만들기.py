# 어떤 자연수 A가 주어진다. 여기에 자연수 B를 곱한 결과가 거듭제곱수가 되는 최소의 B를 구하는 프로그램을 작성하라. 여기서 자연수는 1이상인 정수를 뜻한다.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T 가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 하나의 자연수 A(1≤A≤107) 가 주어진다.


# [출력]
# 각 테스트 케이스마다 A에 곱한 결과가 거듭제곱수가 되는 최소의 자연수를 출력한다.

def prime_lst():
    sieve = [True] * 3164   # 범위 설정
    for i in range(2, 3165):  # 2부터 시작
        if sieve[i] == True:
            for j in range(i+i, 3164, i):  # i의 배수들 다 제거
                sieve[j] = False
    return [i for i in range(2, 3164) if sieve[i] == True]


a = prime_lst()  # 소수 리스트 만들어놓기
ans = [0]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    result = 1
    for prime in a:  # 소수의 값들로 나누어서
        if prime > N:  # 만약 소수가 N보다 크면 멈춤
            break
        cnt = 0
        while N % prime == 0:
            N //= prime
            cnt += 1
        if cnt % 2 == 1:  # 거듭제곱수가 되려면 제곱근이 2가 되어야함
            result *= prime
    if N > 1:
        result *= N
    ans.append(result)
for i in range(1, len(ans)):
    print(f'#{i} {ans[i]}')
