# upper(), lower()
str = 'Hello World'
print(str.upper()) # 대문자
print(str.lower()) # 소문자
print(str.swapcase()) # 대소문자 변환

# title()
str = "hello world"
print(str.title()) # 단어에 첫 문자 대문자로
# count("찾는 문자") 
print(str.count("l")) # 문자열에 찾는 문자의 수를 출력
# find("찾는 문자")
# 없으면 -1 출력
# find는 왼쪽 부터 검색 rfind는 오른쪽 부터 검색
print(str.find("hello")) # 문자열에 찾는 문자의 위치값 출력
print(str.rfind("hello"))
# index는 없으면 에러가 발생
print(str.index("hello"))

# startswith() endswith()
print(str.startswith("hello"))
print(str.startswith("world"))
print(str.endswith("world"))
print(str.endswith("hello"))

# strip() rstrip() lstrip()
# 공백제거
str = " aaa "
print(str.strip())
print(str.rstrip())
print(str.lstrip())

# replace(기존문자, 대체문자)
print(str.replace(" ", "*"))

# split() 문자열 분리
str = "banana,apple,melon"
print(str.split(","))

# splitlines() : 행을 기준 분리
str = '''안녕하세요.
반갑습니다. 
다음에 만나요'''
print(str.splitlines())

str1 = "hello"
str2 = "*"
print(str2.join(str1))

# isdigit()
str1 = "1234"
str2 = "1234 "
print(str1.isdigit())
print(str2.isdigit())

str1 = "abcde한글"
str2 = "abcde한글123"
str3 = "abcde한글123!!!!"
print(str1.isalpha())
print(str2.isalpha())
print(str2.isalnum())
print(str3.isalnum())
print(str1.islower())
print(str1.isupper())
print(str1.isspace())