num = int(input())

while True:
    if num > 0:
        print("#", end='')
        num -= 1
        continue
    elif num == 0:
        break
