# 랜덤으로 주어지는 한글 단어를 2초안에 입력
# 2초안에 입력하면 점수가 더해지고 2초가 넘으면 생명이 감소 
# 생명이 없으면 게임 종료 

import random
import time

words = [
    "가방", "나무", "하늘", "바다", "사랑",
    "고양이", "자동차", "컴퓨터", "핸드폰", "물고기",
    "연필", "도서", "학교", "친구", "음악",
    "비행기", "지하철", "냉장고", "아이스크림", "신문지"
]

score = 0 
life = 3 
time_limit = 2  # 2초가 지나면 실패

while True:
    if life <= 0:
        print(f"생명이 다 떨어졌습니다. 총 스코어는 {score}점입니다.    게임종료" )
        break    
    
    word = random.choice(words)
    print(f"단어: {word}")

    start_time = time.time()
    answer = input("입력하세요: ")
    elapsed = time.time() - start_time

    if elapsed > time_limit:
        print("시간초과! life 1 감소")
        life -= 1
    elif answer == word:
        score += 1
        print(f"정답! 점수 1점 추가. 현재 점수: {score}")
    else:
        print("틀렸습니다. 생명 1 감소")
        life -= 1  
