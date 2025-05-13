i = 1
odd = 0
even = 0

while i <= 10:
    if i % 2 == 0:
        even += i
    else:
        odd += i
    i += 1
print("1 ~ 10까지의 짝수 합 : ", even)
print("1 ~ 10까지의 홀수 합 : ", odd)