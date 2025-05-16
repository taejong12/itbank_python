# list, dictionary 두 가지를 자료형으로 가장 많이 사용
# tuple 같은 경우 함수 return 값으로 많이 사용

# list -> 자바 ArrayList
# tuple -> 자바 HashSet
# dictionary -> 자바 HashMap

# dictionary
# 키를 이용하여 값을 가져오는 방식 
# 탐색 속도가 빠르고 사용하기 편리함
# 중괄호를 사용한다.

# list = [] 
# tuple = ()
# dictionary = {}

stu1 = {'이름':'홍길동', '연락처':'010-1111-1111',
        '주소':'서울 종로구'}
print(stu1)
print(type(stu1))

# 각 요소를 호출 하거나 값을 입력할 때는 [] 를 사용한다.
print(stu1['이름'])
print(stu1['연락처'])

stu1['이름'] = '이순신'
print(stu1)