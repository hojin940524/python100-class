#python 008

#가위바위보 게임
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

img_hands = [rock, paper, scissors]

user = int(input('무엇을 내겠습니까? 바위(0), 보(1), 가위(2) > '))
if(user >= 3 or user < 0):
    print('잘못된 숫자를 입력했습니다.')
else:
    print(f'나의 선택은 > ')
    print(img_hands[user])
    
    computer = random.randint(0,2)
    print(f'컴퓨터의 선택은 > ')
    print(img_hands[computer])
    if (user == 2 and computer == 0):
        print("컴퓨터 WIN")
    elif (user == 0 and computer == 2):
        print("user WIN")
    elif (user == 0 and computer == 0):
        print("비겼다!")
    elif (user > computer):
        print("user WIN")
    elif (user < computer):
        print("컴퓨터 WIN")

