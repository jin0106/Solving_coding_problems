import sys
N = int(sys.stdin.readline())       # input() 보다 입출력 속도가 빠름  sys.stdin.readline > raw_input() > input()
stack = []
for _ in range(N):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        stack.append(a[1])
    elif a[0]== 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)