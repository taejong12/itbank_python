# random : 난수 발생 모듈
# Python 에 내장 되어 있는 모듈 (내장 모듈)

# import 모듈명
import random

# 소수점 난수 발생 (0.0 ~ 0.9999999999... 사이의 값)
for i in range(5):
    print(f"{i} 번째 : {random.random()}")

# 정수형 난수 발생
# int(random.random() * 숫자) : 0 ~ 숫자-1
for i in range(5):
    print(f"{i} 번째 : {random.random() * 100}")

for i in range(5):
    print(f"{i} 번째 : {int(random.random() * 100)}")