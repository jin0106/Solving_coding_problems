import sys

input = sys.stdin.readline

a = list(input().rstrip())
bomb = list(input().rstrip())
length = len(bomb)

stack =[]

for i in range(len(a)):
    stack.append(a[i])  # stack에 하나씩 넣기
    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):   # 스택의 마지막것과 bomb의 마지막 글자가 같고 stack의 갯수가 bomb 같거나 크다면
        if stack[-len(bomb):] == bomb:  # stack 뒤에서 bomb길이만큼과 bomb 이 같으면
            for _ in range(len(bomb)):  # pop해주기
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')