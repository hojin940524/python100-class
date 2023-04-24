#python 007 
#다중 연속 if문

#롤러코스터 
print('*** 파이썬 롤러코스터에 오신 걸 환영합니다! ***')
height = int(input('당신의 키는 몇 cm 입니까 > '))
money = 0

if(height >= 120):
    age = int(input('당신의 나이는 몇 살 입니까 > '))
    if(age < 12):
        print('무료입니다.')
    elif(age <= 18):
        money = 7000
        print('7000원 입니다.')
    elif(age >= 65 and age <+70): #논리연산자 and => A and B (A 와 B 둘 다 만족)
        money = 3000
        print('경로 우대 할인되어 3000원 입니다.')
    else:
        money = 12000
        print('12000원 입니다.')

    picture = input('사진 촬영을 원합니까? YES(Y) or NO(N) > ').upper() 
                                                        #upper함수(대문자로 변환 하는 함수)
                                                
    if(picture == 'Y' or picture == 'YES'): 
                    #논리연산자 or => A or B (A 와 B 둘 중 하나만 만족)
        money += 1000
    
    print('총 금액은 {}원 입니다.'.format(money))

else:
    print('롤러코스터를 탈 수 없습니다.')
