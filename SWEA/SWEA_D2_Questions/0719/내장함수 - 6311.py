# "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와

# 같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된

# 알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.

# input x
# output = 184

sentence = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
A = sentence.count("A") * 4
B = sentence.count("B")*3
C = sentence.count("C")*2
D = sentence.count("D")

# print(A)
# print(B)


def calc(sentence, x, y, c, d):
    return sentence(x, y, c, d)


grade = calc(lambda x, y, c, d: x+y+c+d, A, B, C, D)
print(grade)
