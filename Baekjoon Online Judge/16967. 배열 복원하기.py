import sys
input = sys.stdin.readline

H,W,X,Y = map(int, input().split())
array_B = [list(map(int, input().split())) for _ in range(H+X)]
array_A = [[0]*W for _ in range(H)]

for y in range(H):
  for x in range(W):
    array_A[y][x] = array_B[y][x]

for y in range(X,H):
  for x in range(Y,W):
    array_A[y][x] = array_B[y][x] - array_A[y-X][x-Y]

for y in range(H):
  for x in range(W):
    print(array_A[y][x], end =' ')
  print('')