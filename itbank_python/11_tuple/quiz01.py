tp = "회사정보","제품이름","가격정보","출시일자"
ls = ['삼성전자', '폴드4', '100만원', '미정']

print("(튜플)\t\t: (리스트)")
for i in range(len(tp)):
    print(f"{tp[i]}\t: {ls[i]}")

# ls.remove("100만원")
# ls.remove("미정")
# ls.append("140만원")
# ls.append("2022.12")
ls.insert(2, "140만원")
ls.insert(3, "2022.12")

print("(튜플)\t\t: (리스트)")
for i in range(len(tp)):
    print(f"{tp[i]}\t: {ls[i]}")