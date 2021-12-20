N = int(input())
M = int(input())
ans = abs(100-N)  # 처음에 채널 100에서 시작 하므로

if M:   # M이 0 부터 시작하므로 체크
    broken = list(map(str, input().split()))
else:
    broken = []

# 백만인 이유는 위아래로
for num in range(1000000):
    for j in str(num):
        if j in broken:
            break
    else:
        ans = min(ans, len(str(num))+abs(num-N))
print(ans)
