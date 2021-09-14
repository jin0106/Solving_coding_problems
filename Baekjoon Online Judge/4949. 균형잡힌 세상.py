import sys
while True:
    s = sys.stdin.readline().replace('\n','')
    if s == '.':
        break
    else:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] =='[':
                stack.append(s[i])
            elif s[i] == ')':
                if stack:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        print('no')
                        break
                else:
                    print('no')
                    break
            elif s[i] == ']':
                if stack:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        print('no')
                        break
                else:
                    print('no')
                    break
            if i == len(s)-1:
                if stack:
                    print('no')
                    break

        else:
            print('yes')
