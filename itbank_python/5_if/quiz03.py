saveId = 'hong'
savePwd = '1234'

inputId = input("아이디 입력 : ")
inputPwd = input("암호 입력 : ")

if saveId == inputId:
    if savePwd == inputPwd :
        print("로그인에 성공했습니다.")
    else :
        print("암호가 틀렸습니다.")
else :
    if savePwd == inputPwd:
        print("등록되지 않은 아이디 입니다.")
    else:
        print("아이디, 암호를 확인하세요.")