s = int(input())
i =1
cnt =0
while s >= 0:
    cnt +=1
    s -= i
    i +=1
print(cnt-1)


