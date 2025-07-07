#놀이공원 롤러코스트 제한 키 140 나이 10  둘다 충족시 입장가능 if else로 구분하럿

H = int(input("키를 입력하세요: "))
A = int(input("나이를 입력하세요: "))

if H >= 140 and A >= 10:
    print("탑승 가능합니다.")
else:
    print("탑승이 불가능합니다.")