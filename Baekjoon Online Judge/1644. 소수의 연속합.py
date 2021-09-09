

def isPrime(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i ):
                sieve[j] = False
    return [i for i in range(2,n) if sieve[i] == True]

lst = isPrime(4000000)

N = int(input())
start, end = 0, 0
cnt =0
total = 0
while lst[end]<=N:
    if total <N:
        total += lst[end]
        end+=1
        if total == N:
            cnt += 1
            total -= lst[start]
            start += 1
        if lst[end] == N:
            cnt +=1
            break
    if total > N:
        total -=lst[start]
        start +=1
    if total == N:
        cnt += 1
        total -= lst[start]
        start += 1

print(cnt)
