multiple = int(input("배수 입력 : "))
for i in range(1, 101):
    if i % multiple == 0:
        print(i, end = " ")
print()

num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번재 정수 입력 : "))
sum = 0
for i in range(num1, num2+1):
    sum += i
print(f"{num1} ~ {num2} 합 : {sum}") 
        