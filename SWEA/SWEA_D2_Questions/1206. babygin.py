# 0~9 사이의 숫자카드에서 임의의 카드 6장을 뽑았을때,
# 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고,
# 3장의 카드가 동일한 번호를 갖는 경우를 tripletes이라고 한다.

# 그리고, 6장의 카드가 run과 tripletes로만 구성된 경우를 Baby-Gin이라고 하는데,
# 6자리의 숫자를 입력받아 Baby-Gin 여부를 판단하는 프로그램을 작성해보자.

# 예)
# 667767은 두 개의 triplet이므로 Baby-Gin이다. (666,777)
# 054060은 한 개의 run과 한 개의 triplet이므로 Baby-Gin이다. (456,000)
# 101123은 한 개의 triplet가 존재하나, 023이 run이 아니므로 Baby-Gin이 아니다.

# [입력]
# 첫 번째 줄에 Test Case의 수 T가 주어집니다.
# T개의 줄에 걸쳐 각 Baby-Gin인지 확인할 TestCase가 6자리 수로 주어집니다.

# [출력]
# 각 TestCase에 대하여 '#'과 TestCase번호, Baby Gin의 여부를 출력합니다.
# Baby Gin의 여부로 Baby Gin인 경우 Baby Gin을 출력하고, 아닌 경우 Lose를 출력합니다.

tc = int(input())
for t in range(1, tc+1):
    lst = list(map(int, input().strip()))
    check = [0]*10      # 0~9 갯수 받기 위한 리스트 생성
    for num in lst:     # check 리스트에 숫자의 갯수만큼 +1 씩 해줌으로써 카드의 숫자들을 확인 가능
        check[num] += 1
    row = 0
    trip = 0
    i = 0
    while i < 10:
        if check[i] >= 3:    # 3이상이면 triplet이라는 뜻이므로 중복 방지를 위해 -=3을 해주는 동시에 trip에 +=1
            check[i] -= 3
            trip += 1
            continue
        if i <= 7:
            if check[i] >= 1 and check[i+1] >= 1 and check[i+2] >= 1:   # Run 확인 중복 방지위해 -1씩 해줌
                row += 1
                check[i] -= 1
                check[i+1] -= 1
                check[i+2] -= 1
                continue
        i += 1

    if row+trip == 2:
        print(f'#{t} Baby Gin')
    else:
        print(f'#{t} Lose')


# 처음에 이중 for문으로 풀려고 해서 생각보다 오래 걸렸던 문제. 이중 for문으로도 계속 풀었으면 어떻게든 풀었겠지만 while보다 효율이 떨어졌을것이라고 생각된다. 그리고 쉬운 방법 놔두고 굳이 어려운 방법으로 할 필요는 없으니..
