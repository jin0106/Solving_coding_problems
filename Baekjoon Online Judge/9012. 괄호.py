import sys
N = int(sys.stdin.readline())
for _ in range(N):
    n = input()
    stack = []
    for j,i in enumerate(n):
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                print('NO')
                break
            else:
                stack.pop()
        if j == len(n)-1:
            if stack:
                print('NO')
                break
    else:
        print("YES")


