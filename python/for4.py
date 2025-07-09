#사용자가 입력한 정수의 모든 약수를 화면에 출력하는 프로그램

num = int(input("정수를 입력하세요: "))

print(f"{num}의 약수는 다음과 같습니다:")


for i in range(1, num + 1):
    if num % i == 0:
        print(i)