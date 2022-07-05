import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def check(row):
  global ans
  flag = True
  isSlope = [False] * N

  for i in range(N-1):
    if row[i] == row[i+1]:
      continue
    elif abs(row[i]-row[i+1])>=2:
      flag = False
      break
    elif abs(row[i]-row[i+1])==1:
      if check_slope(row, i, isSlope):
        continue
      else:
        flag = False
        break
  if flag:
    ans +=1

def check_slope(line, i, isSlope):
  n= 0
  
  if line[i] > line[i+1]:
    j= 1
    while 0<=i+j<N and  n <L and not isSlope[i+j]:
      if line[i] == line[i+j]+1:
        isSlope[i+j] = True
        n +=1 
      else:
        break
      j+=1

  elif line[i]< line[i+1]:
    j = 0
    while 0<=i-j<N and  n <L and not isSlope[i-j]:
      if line[i-j]+1 == line[i+1]:
        isSlope[i-j] = True
        n+=1
      else:
        break
      j+=1


  if n == L:
    return True



for i in range(N):
  check(arr[i])

for y in range(N):
  temp = []
  for x in range(N):
    temp.append(arr[x][y])
  check(temp)

      

print(ans)