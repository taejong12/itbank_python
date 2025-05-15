# indexing
# 연속적인 객체에 부여된 번호를 의미하고 원하는 위치값을 출력
ls = [1,2,3,4]
print(ls[1])
print(ls[2])

# slicing 
# 연속적인 객체에 부여된 번호의 일부의 값을 추출
# list[start:stop-1:step]
ls = [1,2,3,4]
print(ls[1:2])
print(ls[:2])
print(ls[:2:2])
print(ls[::])
print(ls[:])

str = "hello python"
print(str[:3])
print(str[5:])