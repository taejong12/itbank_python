num1 = int(input("정수 입력 : "))
if num1 % 3 == 0:
    print("3의 배수 입니다.")

num2 = int(input("첫번째 정수 입력 : "))
num3 = int(input("두번째 정수 입력 : "))

if num2 > num3:
    print("첫번째 정수가 큽니다.")
if num3 > num2:
    print("두번째 정수가 큽니다.")

num4 = int(input("첫번째 정수 입력 : "))
num5 = int(input("두번째 정수 입력 : "))
sum = num4 + num5

if sum % 3 == 0:
    print("두 합의 값은 3의 배수 입니다.")