# 계산기를 함수를 이용해서 구현
#   + - * / 함수를 만들어서 구현
def input_num(str):
    num = int(input(str+" 정수 입력 : "))
    return num
def operator(oper, num1, num2):
    if (oper == "+"):
        print(f"{num1} + {num2} = {num1 + num2}")
    elif (oper == "-"):
        print(f"{num1} - {num2} = {num1 - num2}")
    elif (oper == "*"):
        print(f"{num1} * {num2} = {num1 * num2}")
    elif (oper == "/"):
        print(f"{num1} / {num2} = {num1 / num2}")
    else :
        print(f"{oper} 는 연산할 수 없습니다.")
        
num1 = input_num("첫번째")
num2 = input_num("두번째")
oper = input("연산자 입력 : ")
operator(oper, num1, num2)


