from random import randint


def old_macdonald(name):
    if len(name) < 5:
        return False
    else:
        print(name[0].capitalize() + name[1:3] +
              name[3].capitalize() + name[4:])


# old_macdonald('macdonald'


def master_yoda(text):
    x = text.split()
    print(' '.join(x[::-1]))


# master_yoda('I am home')
# master_yoda('We are ready')

def almost_there(n):
    return abs(100-n) <= 10 or abs(200-n) <= 100
    # if abs(100-n) <= 10:
    #     return True
    # elif abs(200-n) <= 10:
    #     return True
    # else:
    #     return False


# print(almost_there(209))


def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i:i+2] == [3, 3]:
            return True

    return False


# print(has_33([1, 3, 3]))


def blackjack(a, b, c):
    if sum((a, b, c)) < 21:
        return sum((a, b, c))
    elif sum((a, b, c)) > 31:
        return 'BUST'
    elif sum((a, b, c)) > 21 and 11 in (a, b, c):
        return sum((a, b, c))-10


# print(blackjack(9, 9, 11))


def summer_89(arr):
    for i in range(0, len(arr)-1):
        if arr[i] == 6:
            return sum(arr)


print(summer_89([4, 5, 6]))
