name = input("이름 입력 : ")
kor = int(input("국어 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))
sum = kor + eng + math
avg = sum / 3
print(f"{name}님의 합계는 {sum}점이고, 평균은 {avg:.2f}점 입니다.")

if avg <= 100 and avg >= 90:
    print("A")
elif avg < 90 and avg >= 80:
    print("B")
elif avg < 80 and avg >= 70:
    print("C")
elif avg < 70 and avg >= 60:
    print("D")
elif avg >= 0 and avg < 60:
    print("F")
else:
    print("없는 점수 입니다.")

if 90 <= avg <= 100:
    print("A")
elif 80 <= avg < 90:
    print("B")
elif 70 <= avg < 80:
    print("C")
elif 60 <= avg < 70:
    print("D")
elif 0 <= avg < 60:
    print("F")
else:
    print("없는 점수 입니다.")