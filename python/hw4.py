message = "%s시 %s분은 %s초 입니다."

h = int(input("몇시? "))
m = int(input("몇분? "))

s = h * 3600 + m * 60


print(message % (h, m, s))