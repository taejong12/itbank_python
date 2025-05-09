num1 = 7
num2 = 5

print(num1,"+",num2,"=",num1+num2)
print(num1,"-",num2,"=",num1-num2)
print(num1,"*",num2,"=",num1*num2)
print(num1,"/",num2,"=",num1/num2)

kor = 100
eng = 98
math = 97
sum = kor + eng + math
avg = sum / 3
print("합계 : ", sum)
print("평균 : ", avg)
print("평균 : %.2f"%avg)
print("평균 : {:.2f}".format(avg))
print(f"평균 : {avg:.2f}")