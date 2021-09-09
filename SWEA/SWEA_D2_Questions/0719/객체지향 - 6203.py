# 다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하십시오.
# 이 때 학생 클래스의 객체는 객체 생성 시 국어, 영어, 수학 점수를 저장하며, 총점을 구하는 메서드를 제공합니다.

# input =89,90,100

# output = "국어, 영어, 수학의 총점: 279"


class sum_grade:
    def grade(self, korean, english, math):
        self.korean = korean
        self.english = english
        self.math = math

    def add_grade(self):
        result = self.korean + self.english + self.math
        return result


a = sum_grade()
a.grade(89, 90, 100)
total = a.add_grade()
print("국어, 영어, 수학의 총점: {}".format(total))
