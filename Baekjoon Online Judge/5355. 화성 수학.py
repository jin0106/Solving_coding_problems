t = int(input())
for _ in range(t):
    formula = list(input().split())
    temp = 0
    for i in range(len(formula)):
        if formula[i] == '@':
            temp *= 3
        elif formula[i] == '%':
            temp += 5
        elif formula[i] == '#':
            temp -=7
        else:
            temp = float(formula[i])
    print('%.2f' % (temp))