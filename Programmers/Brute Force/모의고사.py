a = [1, 2, 3, 4, 5]
b = [2, 1, 2, 3, 2, 4, 2, 5]
c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

cnt = [0] * 3


answer = list(map(int, input().split()))


for i in range(len(answer)):
    if answer[i] == a[i % 5]:
        cnt[0] += 1
    if answer[i] == b[i % 8]:
        cnt[1] += 1
    if answer[i] == c[i % 10]:
        cnt[2] += 1

ans = []
max_score = max(cnt)
for i in range(3):
    if max_score == cnt[i]:
        ans.append(i+1)
print(ans)
