T = int(input())
for t in range(1, T+1):
    word= input()
    vowel = ['a','e','i','o','u']
    ans =''
    for i in word:
        if i not in vowel:
            ans += i
    print(f'#{t} {ans}')
            