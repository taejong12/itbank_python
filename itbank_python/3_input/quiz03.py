name = input("이름 입력 : ")
kor = int(input("국어 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))
sum = kor + eng + math
avg = sum / 3 

print("========= 학생정보 ============")
print("이름\t국어\t영어\t수학\t합계\t평균")
print(f"{name}\t{kor}\t{eng}\t{math}\t{sum}\t{avg:.2f}")