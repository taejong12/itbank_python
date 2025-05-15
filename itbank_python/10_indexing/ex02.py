aa = [1,2,3]

aa2 = aa

print(aa)
print(aa2)

aa2[1] = 200

print(aa)
print(aa2)

print(id(aa))
print(id(aa2))
print(id(aa[1]))
print(id(aa2[1]))

aa3 = aa.copy()

print(aa)
print(aa3)

aa3[1] = 2000

print(aa)
print(aa3)
print(id(aa))
print(id(aa3))
print(id(aa[1]))
print(id(aa3[1]))
print(id(aa[0]))
print(id(aa3[0]))