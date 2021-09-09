

def set_prime(a, b, c):

    list_1 = []
    for n in range(A, B+1):
        result = True
        if n < 2:
            result = False
        for j in range(2, n):
            if n % j == 0:
                result = False
        if result:
            list_1.append(n)
    return list_1


T = int(input())

for i in range(1, T+1):
    D, A, B = map(int, input().split())
    set_prime(D, A, B)
    list_2 = []
    for w in list_1:
        if str(D) in str(w):
            list_2.append(w)
    print(len(list_2))
