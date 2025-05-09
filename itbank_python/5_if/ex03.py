# in 연산자
# 변수 또는 상수의 값이 list 안에 있는지 비교

str = "hello python!"
inputStr = input("검색할 단어 입력 : ")
if inputStr in str:
    print(f"{inputStr} 이 있습니다.")
else :
    print(f"{inputStr} 이 없습니다.")