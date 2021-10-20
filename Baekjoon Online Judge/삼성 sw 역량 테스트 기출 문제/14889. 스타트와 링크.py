import sys

def dfs(index, cnt):
    global ans
    if cnt == n//2:
        start_team = 0
        link_team = 0
        for y in range(n):
            for x in range(n):
                if visit[y] == 1 and visit[x] == 1:
                    start_team += abilities[y][x]
                elif visit[y] ==0 and visit[x] ==0:
                    link_team += abilities[y][x]
        if ans > abs(start_team-link_team):
            ans = abs(start_team-link_team)
            return

    for i in range(index, n):
        visit[i] = 1
        dfs(i+1, cnt+1)
        visit[i] = 0


n = int(sys.stdin.readline())
abilities = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [0]*n
ans = sys.maxsize
dfs(0,0)
print(ans)