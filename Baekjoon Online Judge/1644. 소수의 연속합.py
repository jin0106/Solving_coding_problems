

def isPrime(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2,n) if sieve[i] == True]

lst = isPrime(4000000)

N = int(input())
start, end = 0, 0
cnt =0
total = 0
while True:
    if total >= N:
        if total == N:
            cnt+=1
        total -= lst[start]
        start+=1
    elif end== len(lst):
        break
    else:
        total += lst[end]
        end +=1


print(cnt)
