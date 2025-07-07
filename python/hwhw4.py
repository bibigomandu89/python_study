#원의 넓이를 계산하는 프로그램을 만들고 사용자가 '입력한 원의 반지름으로 자동으로 계산 음수입력의 경우 잘못된 값입니다 출력

#area원의 넓이 radius 반지름 

Radius = int(input("반지름을 입력해주세요~!(cm)"))
R = Radius
if  R >=0:
    area = R*R*3.14
    print("반지름이", R ,"cm인 원의 넓이는",area,"cm*2입니다." )
else R < 0 
    print("잘못된입력입니다!")