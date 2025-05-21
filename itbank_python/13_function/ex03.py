# 매개변수의 값이 전달되지 않으면 기본값을 사용
def aaa(num = 10):
    print(num)

aaa(100)
aaa()

def bbb ():
    return (10, 20, 30)

num1, num2, num3 = bbb()
print(num1, num2, num3)