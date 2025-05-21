# 매개변수 없고 반환값도 없음
def add():
    num1 = int(input("첫번째 정수 입력 : "))
    num2 = int(input("두번째 정수 입력 : "))
    print(f"{num1} + {num2} = {num1 + num2}")

add()

# 매개변수는 있고 반환값 없음
def add(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")

num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번째 정수 입력 : "))
add(num1, num2)

# 매개변수는 없고 반환값은 있음
def add():
    num1 = int(input("첫번째 정수 입력 : "))
    num2 = int(input("두번째 정수 입력 : "))
    return num1, num2

num1, num2 = add()
print(f"{num1} + {num2} = {num1 + num2}")

# 매개변수 있고 반환값도 있음
def add(str):
    num = int(input(str + "번째 입력 : "))
    return num

num1 = add("첫")
num2 = add("두")
print(f"{num1} + {num2} = {num1 + num2}")