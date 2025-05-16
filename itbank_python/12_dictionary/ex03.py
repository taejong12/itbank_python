dic = {1:'일',2:'이',3:'삼',4:'사'}
# keys() - 키만 반환
print(f"keys() : {dic.keys()}")
# values() - 값만 반환
print(f"values() : {dic.values()}")

keys = dic.keys()
for i in keys:
    print(dic[i])

# list(dic 변수) : 키를 리스트로 반환
print(f"list(dic) : {list(dic)}")
print(f"list(dic.keys()) : {list(dic.keys())}")
print(f"list(dic.values()) : {list(dic.values())}")

for i in dic.keys():
    print(f"{i} : {dic[i]}")

# items() : 키와 값을 tuple 반환
for k,v in dic.items():
    print(f"{k} : {v}")

# get() : 키가 있으면 value 값 반환, 없으면 None 반환
print(dic.get(5))
print(dic.get(4))

# setdefault() : 키가 없으면 저장, 있으면 저장 하지 않음
dic.setdefault(4, '사사')
print(dic)
dic.setdefault(5, '오')
print(dic)

# update() : 다른 dictionary 를 추가 
dic1 = {6:'육'}
dic.update(dic1)
print(dic)

# pop() : key를 이용해서 해당 키와 값을 삭제
print(dic.pop(6))
print(dic)

# clear() : dictionary 초기화
dic.clear()
print(dic)