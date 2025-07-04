num = int(input("숫자를 입력하세요:"))

if num>=100000 and num<10000000:
    moreT=num//1000
    lessT=num%1000
    print(str(moreT)+","+str(lessT))

    #123456 일 경우
    #moreT = 123
    #lessT = 456

    #1000을 나누면 목이 123 이 나오고 나머지가 456이 나오니깐  1000을 나눈다 