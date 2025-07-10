#주어진 문장을 얼마나 빠르고 정확하게 입력하는지 측정, 시간및 정확도를 출력
#시작- 랜덤문장 출력 -시간 측청 시작 - 사용자 입력 -시간측정완료 - 정확도 계산 - 결과값출력


#랜덤문장 출력
import random 
import time

sentences = ["안녕하세요","반갑습니다","오늘 날씨 어때요?","역지사지","조삼모사","사필귀정","새옹지마" ] 
             
target = random.choice(sentences)


print("\n다음문장을 그대로 입력하세요\n")
print(target)

input("준비가 되면 Enter를 눌러주세요")

#import time 시간측청    
start_time = time.time()  # 시작 시간 기록


#input("시간측정용")
#사용자 입력받기

typed = input ("따라쓰세요\n")



#종료시간 - 시작 시간

end_time = time.time()

Elapsedtime = end_time-start_time
print(Elapsedtime)      

#정확도 계산
correct = 0 

for i in range(min(len(target),len(typed))):
    if target[i] == typed[i]:
        correct+=1
accuracy = correct / len(target) *100
speed = len(typed) / Elapsedtime* 60      

#출력
print(f" 소요 시간: {Elapsedtime:.2f}초")
print(f" 정확도: {accuracy:.2f}%")
print(f" 타자 속도: {speed:.2f} 글자/분")