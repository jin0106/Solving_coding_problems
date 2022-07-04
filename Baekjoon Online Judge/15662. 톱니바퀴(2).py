import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
arr=[deque(map(int, input().strip()))for _ in range(T)]
K = int(input())
data = [list(map(int,input().split())) for _ in range(K)]

def rotate_clock(lst):
  last = lst.pop()
  lst.appendleft(last)
  return lst

def rotate_reverse(lst):
  first = lst.popleft()
  lst.append(first)
  return lst

def rotate(temp): # 
    global arr
    for i in range(T):
        if temp[i] == 0: 
            continue
        elif temp[i] == 1:
            rotate_clock(arr[i])
        else: 
            rotate_reverse(arr[i])
            
def check_dir(num, dir):
  temp = [0]* T
  temp[num] = dir

  for i in range(num,0,-1):
    if arr[i][6] == arr[i-1][2]:
      break
    temp[i-1] = temp[i] * -1
  for i in range(num, T-1):
    if arr[i][2] == arr[i+1][6]:
      break
    temp[i+1] = temp[i] * -1
  return temp



for wheel, dir in data:
  res = check_dir(wheel-1,dir)
  rotate(res)
  
ans = 0
for i in range(T):
  if arr[i][0] == 1:
    ans +=1
print(ans)
