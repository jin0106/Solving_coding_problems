from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()
ans = [round(sum(nums)/N), nums[N//2], 0, max(nums)-min(nums)]
ans[2] = Counter(nums).most_common()
if len(ans[2])>1 and ans[2][0][1] == ans[2][1][1]:
    ans[2] = ans[2][1][0]
else:
    ans[2] = ans[2][0][0]

for i in ans:
    print(i)