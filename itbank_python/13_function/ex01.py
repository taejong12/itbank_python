# 모듈
# - 파이썬에 직접 정의한 내용들을 모아 놓은 파일
# - 함수나 변수 또는 클래스를 모아 놓은 파일
# - 이 파일들은 호출하여 사용할 수 있다.

# 함수
# - 특정한 기능을 가진 코드의 집합
# - 프로그래머가 직접 이름을 지정하고 호출하여 사용
# - def 로 시작하는 함수를 생성하고 매개변수와 반환값 지정

num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번째 정수 입력 : "))
print(f"{num1} + {num2} = {num1 + num2}")

num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번째 정수 입력 : "))
print(f"{num1} + {num2} = {num1 + num2}")

def add():
    num1 = int(input("첫번째 정수 입력 : "))
    num2 = int(input("두번째 정수 입력 : "))
    print(f"{num1} + {num2} = {num1 + num2}")

add()
add()