# N개의 정점과 M개의 간선으로 구성된 가중치가 없는 무방향 그래프에서의 최장 경로의 길이를 계산하자.
#
# 정점의 번호는 1번부터 N번까지 순서대로 부여되어 있다.
#
# 경로에는 같은 정점의 번호가 2번 이상 등장할 수 없으며, 경로 상의 인접한 점들 사이에는 반드시 두 정점을 연결하는 간선이 존재해야 한다.
#
# 경로의 길이는 경로 상에 등장하는 정점의 개수를 나타낸다.
#
#
# [입력]
#
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
#
# 각 테스트 케이스의 첫 번째 줄에는 두 개의 자연수 N M(1 ≤ N ≤ 10, 0 ≤ M ≤ 20)이 주어진다.
#
# 두 번째 줄부터 M개의 줄에 걸쳐서 그래프의 간선 정보를 나타내는 두 정수 x y(1 ≤ x, y ≤ N)이 주어진다.
#
# x와 y는 서로 다른 정수이며, 두 정점 사이에 여러 간선이 존재할 수 있다.

def dfs(now, cnt):      # cnt 변수를 여기서 안주고 함수 안에서 주면 전부다 카운트가 되버림.
    global max_length   # 글로벌 변수 변경

    for next in range(N+1):
        if adj[now][next] ==1 and visited[next] ==0:        # 서로 연결이 되있고 한번도 가지 않았다면
            visited[next] =1    # 방문 기록 1 체크
            dfs(next, cnt+1)    # 연결된 경로로 다시 함수 실행 및 cnt + 1
            visited[next] =0    # 위의 함수가 종료되서 다시 반환되면 다음 차례를 위해 방문 기록 0 으로 변경
        else:
            if cnt> max_length: # 최장거리인지 체크
                max_length = cnt

    return

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    if M > 0:
        adj = list([0]*(N+1) for _ in range(N+1))      # adj 생성
        lst = []
        visited = [0] * (N + 1)     # 방문 기록
        max_length =0
        for i in range(M):
            x, y = map(int, input().split())    # x,y를 입력받으며 adj에 기록
            adj[x][y] = 1
            adj[y][x] = 1
        for i in range(1,N+1):  # 어디서 출발하는게 최장경로인지 모르므로 모든 숫자에서 출발을 해봐야함.
            visited[i] =1   # 첫 시작점에 1을 체크
            dfs(i, 1)
            visited[i] =0   # 다음차례를 위해 i를 다시 0으로 변경

        print(f'#{t} {max_length}')
    else:
        print(f'#{t} {1}')


