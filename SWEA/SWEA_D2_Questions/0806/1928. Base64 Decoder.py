# 다음과 같이 Encoding 을 한다.

# 1. 우선 24비트 버퍼에 위쪽(MSB)부터 한 byte씩 3 byte의 문자를 집어넣는다.

# 2. 버퍼의 위쪽부터 6비트씩 잘라 그 값을 읽고, 각각의 값을 아래 [표-1] 의 문자로 Encoding 한다.


# 입력으로 Base64 Encoding 된 String 이 주어졌을 때, 해당 String 을 Decoding 하여, 원문을 출력하는 프로그램을 작성하시오.

# [제약사항]
# 문자열의 길이는 항상 4의 배수로 주어진다.
# 그리고 문자열의 길이는 100000을 넘지 않는다.

# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# 테스트 케이스는 Encoding 된 상태로 주어지는 문자열이다.

# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


T = int(input())

for i in range(1, T+1):
    sentence = input()
    list_1 = []
    for ap in sentence:         # 아스키 코드 표를 이용해 BASE64 값으로 변환
        if ord(ap) > 64 and ord(ap) < 91:
            list_1.append(ord(ap)-65)
        elif ord(ap) > 91:
            list_1.append(ord(ap)-71)
        elif ord(ap) < 58:
            list_1.append(ord(ap)+4)
        elif ord(ap) == 43:
            list_1.append(ord(ap)+19)
        elif ord(ap) == 47:
            list_1.append(ord(ap)+16)
    list_2 = []
    for x in list_1:    # BASE64값으로 변환한 것들을 다시 2진법으로 변환
        y = ""
        while x > 0:
            y = str(x % 2)+y
            x //= 2
        if len(y) < 6:
            y = '0'*(6-len(y))+y
            list_2.append(y)
        else:
            list_2.append(y)
    list_3 = []  # 2진법으로 변환한것들을 8비트씩으로 재정렬
    for z in range(0, len(''.join(list_2)), 8):
        t = ''.join(list_2)[z:z+8]
        list_3.append(t)
    s = ''
    for ten in list_3:
        e = int(ten, 2)  # 8비트씩으로 정렬한것을 10진수로 변환 및 아스키 코드를 이용해 문자로 변환

        s += chr(e)
    print(f'#{i} {s}')


# BASE64라는 것에 대해 몰라서 문제를 이해하는것이 가장 어려웠던 문제. Encoding하는법을 알아보고 그걸 역순으로 구하기만 하면 됐던 문제였다.
