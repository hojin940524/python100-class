# Q> 90살까지 산다면 실제 몇일, 몇주, 몇달이 남았을까요? 
# CF> 1년은 365일, 52주, 12개월

age = input('당신의 나이는> ')

year = 90 - int(age)
days = year * 365
weeks = year * 52
months = year * 12 

message = "당신의 남은 {} 날, {} 주, {} 월 ".format(days,weeks,months)
print(message)

#퀴즈 
print(6 + 4/2 - (1*2)) #나누기 때문에 float
a = int("5") / int(2.7) #나누기 때문에 float

#팁 계산기
order = int(input('총 얼마를 주문하셨습니까? '))
tip = int(input('팁을 몇 % 지불할 예정입니까? '))
tip_100 = tip / 100
tip_res = order * tip_100
people = int(input('몇 명이 지불할까요? '))
per_person = (order + tip_res)/ people
print('1인당 지불해야하는 금액은 ',round(per_person,2),'$ 입니다.')

#if/else
#롤러코스터 매표기 
print('롤러코스터를 타러 오셨군요!')
height = int(input('키가 몇 cm 입니까? '))
if height >= 120:
    print('롤러코스터를 탈 수 있습니다!')
    age = int(input('몇 살 입니까? '))
    if age < 12:
        print('무료입니다')
    elif age <= 18:
        print('7000원 입니다.')
    else:
        print('12000원 입니다.')

else:
    print('롤러코스터를 탈 수 없습니다.')

