# 중첩 반복문을 사용하여 입력된 정수만큼 *를 순차적으로 출력
a =int(input("층수를 입력해주세용~"))

for i in range(1,a+1):
    for b in range(i):
        print("*",end="")   
    print()