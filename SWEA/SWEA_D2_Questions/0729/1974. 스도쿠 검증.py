# # 스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.


# # 같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.


# # 입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.


# # [제약 사항]

# # 1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.

# # 2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.


# # [입력]

# # 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

# # 다음 줄부터 각 테스트 케이스가 주어진다.

# # 테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.


# # [출력]

# # 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

# # (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


def sudoku_check(sudoku):
    check = list(range(1, 10))
    for x in range(9):                        # 가로줄 검사
        list_1 = []
        for y in range(9):
            list_1.append(sudoku[x][y])
        if sorted(list_1) != check:
            return 0
    for x in range(9):                      # 세로줄 검사
        list_2 = []
        for y in range(9):
            list_2.append(sudoku[y][x])
        if sorted(list_2) != check:
            return 0

    for x in range(0, 9, 3):            # 3x3체크
        for y in range(0, 9, 3):
            arr_1 = []
            for a in range(y, y+3):
                for b in range(x, x+3):
                    arr_1.append(sudoku[a][b])

            if sorted(arr_1) != check:
                return 0
    else:
        return 1


T = int(input())
for i in range(1, T+1):
    sudoku = []
    for j in range(9):
        arr = list(map(int, input().split()))
        sudoku.append(arr)
    print("#{} {}".format(i, sudoku_check(sudoku)))


# <Thinking Process>

# 이중리스트로 input을 한뒤 이중 포문으로 각각의 숫자를 확인해야겠다.
# 가로줄을 먼저 확인후에 이상없으면 세로줄 확인 마지막으로는 3x3 까지 체크.

# < 마치며>
# 가로, 세로줄을 확인하는 코드를 짜는데는 그리 오랜시간이 걸리지 않았지만, 3x3을 확인하는 코드를 생각해내는데 너무 많은 시간이 걸렸다.
# 아무래도 한 두가지의 방법안에서만 해결을 하려고 했던게 원인이 아닌가 싶다. 그리고 기본이 가장 중요하다는것을 다시 한번 느끼게 해준 문제였다.
