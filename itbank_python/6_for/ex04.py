sum = 0
start = int(input("시작값 입력 : "))
end = int(input("끝값 입력 : "))
grow = int(input("증감값 입력 : "))

for i in range(start, end+1, grow):
    sum += i

print(f"{start} ~ {end} 합 : {sum}")