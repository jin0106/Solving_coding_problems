# 다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

# 다음과 같은 5X5 배열에서 최댓값은 29이다.


# [제약 사항]

# 총 10개의 테스트 케이스가 주어진다.

# 배열의 크기는 100X100으로 동일하다.

# 각 행의 합은 integer 범위를 넘어가지 않는다.

# 동일한 최댓값이 있을 경우, 하나의 값만 출력한다.

# [입력]

# 각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.

# [출력]

# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.

for T in range(1, 11):
    t = int(input())
    lst = [list(map(int, input().split()))
           for _ in range(100)]         # 100x100칸 이차원리스트로 생성
    max_sum = 0
    for x in range(100):            # 가로, 세로들의 합을 구하고 그중에 max값을 max_sum에 저장
        sum_row = 0
        sum_col = 0
        for y in range(100):
            sum_row += lst[x][y]
            sum_col += lst[y][x]
        if sum_row > max_sum and sum_row > sum_col:
            max_sum = sum_row
        elif sum_col > max_sum and sum_col > sum_row:
            max_sum = sum_col
    y = 0
    sum_dia_r = 0
    sum_dia_l = 0
    # 대각선 두 방향 각각들의 합을 구하고 그 중 max값이 기존 max_sum보다 크면 max_sum에 저장
    for x in range(99, -1, -1):
        sum_dia_r += lst[x][y]
        sum_dia_l += lst[y][x]
        y += 1
        if sum_dia_r > max_sum and sum_dia_r > sum_dia_l:
            max_sum = sum_diar_r
        elif sum_dia_l > max_sum and sum_dia_l > sum_dia_r:
            max_sum = sum_dia_l

    print(f'#{t} {max_sum}')
