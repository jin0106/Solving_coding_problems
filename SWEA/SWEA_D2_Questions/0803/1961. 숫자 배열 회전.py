# N x N 행렬이 주어질 때,

# 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.


# [제약 사항]

# N은 3 이상 7 이하이다.

# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에 N이 주어지고,

# 다음 N 줄에는 N x N 행렬이 주어진다.

# [출력]

# 출력의 첫 줄은 '#t'로 시작하고,

# 다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.

# 입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

def rotate(arr):        # 함수 설정
    new_list = [[0]*t for _ in range(t)]  # t x t 리스트 생성

    for j in range(t):              # 회전
        for x in range(t):
            new_list[j][x] = arr[t-x-1][j]

    return new_list  # 리턴


T = int(input())
for i in range(1, T+1):
    t = int(input())
    my_list = [list(map(int, input().split()))
               for _ in range(t)]        # 입력받을 값
    a = rotate(my_list)     # 90, 180, 270도 이므로 3번 함수 실행
    b = rotate(a)
    c = rotate(b)

    print(f'#{i}')
    for j in range(t):
        print(''.join(map(str, a[j])), ''.join(
            map(str, b[j])), ''.join(map(str, c[j])))
