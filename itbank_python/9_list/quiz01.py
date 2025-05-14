ls = [10, 5, 20, 7, 9, 31, 12, 11, 19, 32]

odd = []
even = []
oddSum = 0
evenSum = 0

for i in range(len(ls)):
    if i % 2 == 0:
        even.append(ls[i])
        evenSum += ls[i]
    elif i % 2 != 0:
        odd.append(ls[i])
        oddSum += ls[i]

print(f"odd list : {odd}")
print(f"even list : {even}")

print(f"홀수 인덱스 값의 합 : {oddSum}")
print(f"짝수 인덱스 값의 합 : {evenSum}")
print(f"두 합의 차이 : {oddSum - evenSum}")

ls.reverse()
invertLs = ls
print(f"invertLs : {invertLs}")

ls.sort()
sortLs = ls
print(f"sortLs : {sortLs}")

ls.reverse()
reverseLs = ls
print(f"reverseLs : {reverseLs}")