member = {}

for i in range(3):
    name = input("이름 입력 : ")
    tel = input("전화번호 입력 : ")
    member[name] = tel

print(f"저장된 내용 : {member}")