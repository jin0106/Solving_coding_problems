binary = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
         '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for t in range(1, T+1):
    N, M  = map(int, input().split())
    scanner = [input() for _ in range(N)]
    start = 0
    for i in range(M):
        if '1' in scanner[i]:
            start = i
            break
    scanner = scanner[start:start+7]
    end = M
    for j in range(M-1, -1, -1):
        if scanner[0][j] =='1':
            end = j
            break
    code = scanner[0][end-55:end+1]

    lst =[]
    for i in range(0,56,7):
        temp_code = code[i:i+7]
        lst.append(binary[temp_code])
    odd_num = 0
    even_num =0
    for i in range(8):
        if i %2 == 0:
            even_num += lst[i]
        else:
            odd_num += lst[i]
    even_num *=3
    if (even_num+odd_num) % 10 == 0:
        print(f'#{t} {sum(lst)}')
    else:
        print(f'#{t} {0}')



