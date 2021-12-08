N = int(input())
words =[]
for _ in range(N):
    words.append(input())

# 알파벳 26개
alphabet = [0]* 26

# 각 단어들을 돌며
for word in words:
    # 단어 길이-1 = 자릿수
    cnt = len(word)-1
    for w in word:
        # 자릿수만큼 곱해주기
        alphabet[ord('A')-ord(w)] += 10**cnt
        cnt -=1
# 정렬을 해서 가장 숫자가 큰것 부터 9부터 내림차순으로 곱해주고 ans에 더함
alphabet.sort(reverse=True)
value =9
ans = 0
for i in range(len(alphabet)):
    if alphabet[i]:
        ans += (alphabet[i]*value)
        value -=1
    #  0이 나오면 더이상 볼 필요 없으므로
    else:
        break
print(ans)