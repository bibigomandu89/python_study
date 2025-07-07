
a = int(input("첫 번째 정수를 입력하세요: "))
b = int(input("두 번째 정수를 입력하세요: "))
c = int(input("세 번째 정수를 입력하세요: "))

# 가장 작은값을 구할려면 abc 끼리 각 수의 크기를 구해야함 
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

print("가장 작은 값은:", smallest)
