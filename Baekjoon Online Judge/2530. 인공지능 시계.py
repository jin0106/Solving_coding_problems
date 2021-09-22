h, m, s = map(int, input().split())
t = int(input())

nt = (s+t)//60
if nt >= 1: # 초가 60 넘을 때
    s = (s+t)-(nt*60)   # 초 계산 다시
    m += nt # 분 추가 해주기
else:   # 60 안넘을대는 그냥 더 해주기
    s +=t
if m >= 60: # 분이 60 넘을때
    i = m//60  # 몇 시간인지 구하고
    h += i  # 시간에 더해주기
    m -= (i*60) # 분 다시 구함

if h >=24:  # 24시 넘으면 24빼주기
    h %=24

print(h, m, s)