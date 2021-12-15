
numbers = list(map(int, input().split()))

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)
    answer = ''
    for i in range(len(numbers)):
        answer += (numbers[i])
    return str(int(''.join(numbers)))