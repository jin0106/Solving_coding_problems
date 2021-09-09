print('hello')

y = input()  # 숫자 넣기
x = list(y)  # y를 리스트로 반환
n = list(map(int, x))
num = 0
a = 0
b = ""
list_input = "0 1 2 3 4 5 6 7 8 9"


while num <= 9:
    a = n.count(num)
    b += "%s" % a
    num += 1
print("0 1 2 3 4 5 6 7 8 9")
print(" ".join(b))
