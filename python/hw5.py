#화씨의 온도를 읽어서 섭씨를 온도로 변환 하라 
# C=(f-32.0)*5/9

F = int(input("화씨 몇 도입니까? "))
C = round(F - 32.0) * 5 / 9

print(f"화씨 {F}도는 섭씨 {C:.1f}도 입니다.")