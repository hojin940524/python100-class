#python 챌린지 06
height = float(input('키를 입력하세요(cm)> '))
height_M = height * 0.01
weight = float(input('몸무게를 입력하세요(kg)> '))

BMI = round(weight / (height_M**2),2)

print('키(cm)> {}, 몸무게(kg)> {}, BMI> {}'.format(height,weight,BMI))
if(BMI < 18.5):
    print('저체중입니다.')
elif(BMI < 25):
    print('정상체중입니다.')
elif(BMI < 30):
    print('과체중입니다.')
else:
    print('비만입니다.')