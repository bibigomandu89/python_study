import random

proverbs = [
    ["호랑이 굴에 가야", "호랑이 새끼를 잡는다"],
    ["가는 말이 고와야", "오는 말이 곱다"],
    ["백문이", "불여일견"],
    ["등잔 밑이", "어둡다"],
    ["낮말은 새가 듣고", "밤말은 쥐가 듣는다"],
    ["원숭이도 나무에서", "떨어진다"],
    ["고래 싸움에", "새우 등 터진다"],
    ["돌다리도 두들겨 보고", "건너라"],
    ["빈 수레가", "요란하다"],
    ["티끌 모아", "태산"]
]

score = 0

for total in range(5):
    front, back = random.choice(proverbs)
    print(f"{total+1}번째 문제입니다.")
    print(f"속담 : \"{front} ___\"")
    answer = input("뒷부분을 입력하세요 : ").strip()

    if answer == back:
        print("정답입니다.\n")
        score += 1
    else:
        hint1 = back[0]
        print(f"오답입니다. 힌트를 드릴게요 → 첫 글자: \"{hint1}\", 총 글자수: {len(back)}")
        answer = input("다시 한번 기회를 드립니다: ").strip()

        if answer == back:
            print("정답입니다!\n")
            score += 1
        else:
            
            hint2 = back[1] 
            print(f"오답입니다. 힌트를 더 드릴게요 → 두 번째 글자: \"{hint2}\", 총 글자수: {len(back)}")
            answer = input("최후의 기회! 다시 입력해주세요: ").strip()

            if answer == back:
                print("정답입니다!\n")
                score += 1
            else:
                print(f"완전 오답입니다. 정답은 \"{back}\"입니다.\n")

print(f"\n출제 개수: {total+1}개, 정답 개수: {score}개")