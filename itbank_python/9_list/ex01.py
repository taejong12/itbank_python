# list : 데이터의 목록을 다루는 자료형
# []를 이용하여 자료형을 구분
# 데이터의 종류와 상관없이 list 에 포함할 수있다.
# list 의 값을 가져오기 위해서는 index 를 이용한다.
ls = [1,2,3,4]
print(ls)

for i in ls :
    print(i)

for i in range(len(ls)):
    print(ls[i])
