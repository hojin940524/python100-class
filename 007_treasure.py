#python 007 
#다중 연속 if문
#아스키 코드로 화면 꾸미기

print('*** 하하하! 보물을 찾아 봐라 ***')

ch1 = input('당신은 갈림길에 있습니다. \n오른쪽(r), 왼쪽(l)을 선택하시오 > ').lower()
if(ch1 == 'l'):
    print('통과! \n')
    ch2 = input('호수가 보이네요. \n수영해서 간다(s), 기다린다(w) > ').lower()
    if(ch2 == 'w'):
        print('통과! \n')
        ch3 = input('문이 보입니다. \n어느 문으로 들어갈까요? 빨강(r), 노랑(y), 파랑(b) > ').lower()
        if(ch3 == 'y'):
            print('보물을 찾았습니다.')
            print('''               
                    *******************************************************************************
                            |                   |                  |                     |
                    _________|________________.=""_;=.______________|_____________________|_______
                    |                   |  ,-"_,=""     `"=.|                  |
                    |___________________|__"=._o`"-._        `"=.______________|___________________
                            |                `"=._o`"=._      _`"=._                     |
                    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
                    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
                    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
                    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
                    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
                    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
                    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
                    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                    /______/______/______/______/______/______/______/______/______/______/[TomekK]
                    *******************************************************************************
            ''')
            # print('''아스키 코드''')로 해야 다중 문자열이 보임
            
            name = input('user의 성함을 입력하세요 > ')
            print('우승자는 ',name, '입니다.')

        else:
            print('GAME OVER.') 
    else:
        print('GAME OVER. 물에 빠졌습니다.')  
else:
    print('GAME OVER.  구멍에 빠졌습니다.')