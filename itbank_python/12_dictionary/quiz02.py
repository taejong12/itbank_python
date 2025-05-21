import collections
info={};  bl = True;  num = 0;number=0;gr = '';addr=''
info2= collections.OrderedDict()

while bl:
    print("1.인적사항 등록"); print("2.검색");  print("3.수정");
    print("4.삭제");print("5.전체학생 보기");print("6.종료")
    num=int(input(">>> "))
    if num == 1:
        number = input("학번 입력 : ");
        name = input("이름 입력 : ");
        gr = input("등급 입력 : ")
        addr = input("주소 입력 : ")
        info2["학번"]=number;info2["이름"]=name;info2["등급"]=gr;info2["주소"]=addr
        info[number] = info2.copy()
        info2.clear()
        print("등록 완료")
    elif num == 2:
        number = input("찾고자하는 학생 학번 입력 : ")
        if info.get(number) == None:   print("찾고자 하는 학생이 없습니다")
        else:        print(info[number])
    elif num==3:
        number = input("수정할 학번 입력")
        if info.get(number) == None:   print("찾고자 하는 학생이 없습니다")
        else:
            print(info.get(number))
            val = input("수정할 항목 : ")
            change = input("수정할 값 : ")
            info[number][val] = change
            print("수정 완료 되었습니다")
    elif num == 4:
        number = input("삭제할 학번 입력")
        if info.get(number) == None:   print("삭제할 학생이 없습니다")
        else:
            print(info.pop(number),"삭제 되었습니다")
    elif num ==5:
        for k,v in info.items():
            for i,j in v.items():
                print(i,":",j)
    elif num ==6:
        print("프로그램 종료 합니다")
        bl = False
