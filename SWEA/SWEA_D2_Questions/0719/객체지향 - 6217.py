# name 프로퍼티를 가진 Student를 부모 클래스로 major 프로퍼티를 가진

# GraduateStudent 자식 클래스를 정의하고 이 클래스의 객체를

# 다음과 같이 문자열로 출력하는 코드를 작성하십시오.

# input x

# output =
# 이름: 홍길동
# 이름: 이순신, 전공: 컴퓨터


class Student:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("이름: {}".format(self.name))


class GraduateStudent(Student):
    def __init__(self, major):
        self.major = major

    def print_major(self):
        print("이름: {}, 전공: {}".format(self.name, self.major))


a = Student('홍길동')
a.print_name()
b = GraduateStudent('이순신')
b.print_major()
