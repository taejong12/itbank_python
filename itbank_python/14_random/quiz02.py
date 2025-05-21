import random

win, draw, lose = 0, 0, 0

while True:
    com = random.randrange(0,3) + 1
    user = int(input("1.가위 2. 바위 3. 보 : "))

    if user == 1:
        if com == 1:
            print("비겼습니다.")
            draw += 1
        elif com == 2:
            print("컴퓨터가 이겼습니다.")
            lose += 1
        elif com == 3:
            print("사용자가 이겼습니다.")
            win += 1
    if user == 2:
        if com == 1:
            print("사용자가 이겼습니다.")
            win += 1
        elif com == 2:
            print("비겼습니다..")
            draw += 1
        elif com == 3:
            print("컴퓨터가 이겼습니다.")
            lose += 1
    if user == 3:
        if com == 1:
            print("컴퓨터가 이겼습니다.")
            lose += 1
        elif com == 2:
            print("사용자가 이겼습니다.")
            win += 1
        elif com == 3:
            print("비겼습니다.")
            draw += 1
    
    print(f"승 : {win}, 무 : {draw}, 패 : {lose}")

    if(win == 5 or lose == 5):
        print("종료합니다.")
        break