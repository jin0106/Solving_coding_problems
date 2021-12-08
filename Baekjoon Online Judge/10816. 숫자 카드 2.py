import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

card = {}
for i in A:
    if i in card: card[i] += 1
    else: card[i] =1

ans = []

for i in m:
    if i in A:
        ans.append(card[i])
    else:
        ans.append(0)

print(' '.join(map(str, ans)))




