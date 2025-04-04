from random import randint # 의미, 랜덤 모듈에서 다음의 함수들을 임포트한다. 여러개를 임포트해도 된다. 

print("Welcome Python Casino!")
pc_choice = randint(1, 50)

# while은 조건이 참인경우 끊임없이 실행한다.
# 따라서 처음에 참인 조건을 만들어 준 뒤
# 원하는 상황에 이르면 멈추도록 함수를 만들어야 한다.
# 아래 playing = True 은 참인 조건을 위해 임의로 넣은 것이며
# 원하는 값이 나온 경우 멈추기 위해 if 문 안에 playing = False 를 넣었다.

playing = True

while playing: 
    user_choice = int(input("Choose numner."))
    if user_choice == pc_choice:
        print("You win!")
        playing = False
    elif user_choice > pc_choice:
        print("Lower!")
    elif user_choice < pc_choice:
        print("Higher!")



# while 을 알아보는 간단한 함수
# distance = 0

# while distance < 20: # 조건이 참이면 아래를 실행하라
#     print("I'm running:", distance, "km") # 조건이 참이면 출력하라
#     distance = distance + 1 #최초 변수값에 1을 더하라