str1 = "NeVer EvEr giVe up"

str1 = str1.title()
print(f"str1.title() -> {str1}")
str1 = str1.replace(" ", "-")
print(f"str1.replace(' ','-') -> {str1}")

str2 = "2020/01/23"
str2 = str2.split("/")

for i in str2 :
    print(f"{i}")

for i, s in enumerate(str2):
    print(f"{i} 순서 : {s}")

for i in range(len(str2)):
    print(f"{i}번째 : {str2[i]}")