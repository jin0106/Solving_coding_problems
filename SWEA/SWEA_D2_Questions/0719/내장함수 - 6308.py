# 다음의 결과와 같이 이름과 나이를 입력 받아

# 올해를 기준으로 100세가 되는 해를 표시하는 코드를 작성하십시오.

# input = 홍길동 20
# output = 홍길동(은)는 2099년에 100세가 될 것입니다.
from datetime import datetime, date
now = date(2018, 1, 1).year
name, age = input('입력하세요: ').split()
name = str(name)
age = int(age)
# more_year = 100 - age
# year = 2018 + more_year


print("{}(은)는 {}년에 100세가 될 것입니다.".format(name, now-age+101))
