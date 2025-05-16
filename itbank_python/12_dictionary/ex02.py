site = {}
site['네이버'] = 'https://www.naver.com'
site['구글'] = 'https://www.google.com'
site['다음'] = 'https://www.daum.net'

print(site)
print(site['네이버'])
print(site['구글'])
print(site['다음'])

key = input("사이트 이름 입력 : ")
value = input("사이트 주소 입력 : ")
site[key] = value
print(site[key])