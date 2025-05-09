print("## 버스 요금 계산기 ##")
distance = int(input("이동 거리 입력 : "))
count = 0

if distance < 0:
    print("이동할 수 없는 거리입니다.")
elif distance < 30:
    count = 3000
else:
    count = 3000
    distance -= 30
    count += distance * 100
print(f"요금 : {count} 원")