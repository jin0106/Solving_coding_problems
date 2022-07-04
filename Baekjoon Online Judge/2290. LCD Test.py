import sys
input = sys.stdin.readline

s, n = map(str, input().split())
s = int(s)
hori = s+2
ver = 2*s+3
char1 = '-'
char2 = '|'

arr = []

def top():
  for i in range(hori):
    if i != 0 and i != hori-1:
      temp[0][i] = char1
  return temp

def top_right():
  for i in range(ver//2):
    if i != 0:
      temp[i][hori-1] = char2
  return temp

def top_left():
  for i in range(ver//2):
    if i != 0 :
      temp[i][0] = char2
  return temp

def center():
  for i in range(hori):
    if i != 0 and i != hori-1:
      temp[ver//2][i]= char1
  return temp

def bottom_left():
  for i in range(ver//2+1, ver):
    if i != ver-1:
      temp[i][0] = char2

def bottom_right():
  for i in range(ver//2+1, ver):
    if i!= ver-1:
      temp[i][hori-1] = char2

def bottom():
  for i in range(hori):
    if i != 0 and i != hori-1:
      temp[ver-1][i] = char1
  return temp


for i in n:
  i = int(i)
  temp = [[' ']* hori for _ in range(ver)]
  if i in [2,3,5,6,7,8,9,0]:
    top()
  if i in [1,2,3,4,7,8,9,0]:
    top_right()
  if i in [4,5,6,8,9,0]:
    top_left()
  if i in [2,3,4,5,6,8,9]:
    center()
  if i in [2,6,8,0]:
    bottom_left()
  if i in [1,3,4,5,6,7,8,9,0]:
    bottom_right()
  if i in [2,3,5,6,8,9,0]:
    bottom()
  arr.append(temp)
  

ans = [[] for _ in range(ver)]


for i in range(ver):
  for j in range(len(arr)):
    ans[i] += arr[j][i]
    ans[i].append(' ')


for i in ans:
  print(''.join(i))
