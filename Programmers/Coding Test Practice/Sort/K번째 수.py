def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a,b,c = commands[i][0]-1, commands[i][1], commands[i][2]-1
        answer.append(sorted(array[a:b])[c])

    return answer