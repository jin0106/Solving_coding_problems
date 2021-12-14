progresses = list(map(int, input().split()))
speeds = list(map(int, input().split()))
ans = []
day = 0
cnt = 0

while len(progresses) > 0:
    if (progresses[0] + day*speeds[0]) >= 100:
        progresses.pop(0)
        speeds.pop(0)
        cnt +=1
    else:
        if cnt > 0:
            ans.append(cnt)
            cnt = 0
        day += 1
ans.append(cnt)

print(ans)