ls = []
# append() : 마지막 인덱스에 값을 추가
ls.append(10)
print(ls)
ls.append(20)
print(ls)
ls.append(30)
print(ls)

# pop() : 마지막 인덱스 값을 삭제하고 값을 반환
num = ls.pop()
print(num)

# sort() : list 의 값을 정렬
ls = [1,3,2,8,4]
ls.sort()
print(ls)

# reverse() : 인덱스를 역순으로 변경
ls = [1,3,2,4]
ls.reverse()
print(ls)

# index() : 지정값의 처음 위치값을 반환
ls = [1,2,3,4]
print(ls.index(2))
# print(ls.index(6))
# 찾는 값이 없으면 에러 

# insert() : 지정된 위치에 값을 삽입
ls = [1,2,3]
ls.insert(1, 100)
print(ls)

# remove() : 지정한 값의 첫번째 값을 제거
ls = [1,1,2,2]
ls.remove(1)
print(ls)

# extend() : list에 다른 list 추가 
ls1 = [1,2,3]
ls2 = [4,5,6]
ls1.extend(ls2)
print(ls1)

# del() : index 번호로 값 삭제
ls = [1,2,3]
del(ls[1])
print(ls)

# len() : list 크기를 반환
print(len(ls))

# clear() : list 를 초기화
ls.clear()
print(ls)