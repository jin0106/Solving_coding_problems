# 달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

# 다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.


# [예제]

# N이 3일 경우,


# N이 4일 경우,


# [제약사항]

# 달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스에는 N이 주어진다.


# [출력]

# 각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

T = int(input())
for i in range(1, T+1):
    N = int(input())
    cube = [[0] * N for _ in range(N)]
    num = 1     # 기본 숫자
    rota = 1    # 방향을 위한 숫자
    x = 0    # x 값
    y = -1   # y 값
    while N > 0:
        for _ in range(N):          # 가로줄 이동 및 숫자 추가
            y += rota
            cube[x][y] = num
            num += 1
        N -= 1              # 네모를 벗어나지 않기 위해 N-=1

        for _ in range(N):         # 세로줄 이동 및 숫자 추가
            x += rota
            cube[x][y] = num
            num += 1
        rota *= -1
    print(f'#{i}')
    for j in range(len(cube)):
        print(*cube[j])
