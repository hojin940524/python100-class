#4일차

#4-1 글자수 세기
print(len('hello'))
#print(len(12345)) 오류 
#why? 숫자는 문자열이 아니기 때문
    

#4-2 데이터 형식과 함수
num_char = len(input("당신의 이름은 무엇입니까?"))
print(type(num_char)) # 결과 - 자료형 int
now_num_char = str(num_char)
print("당신의 이름은 " + now_num_char + " characters.")

#4-2 데이터유형 바꾸기
a = 123
print(type(a)) # 정수 자료형 

a = str(123)
print(type(a)) # 문자열 자료형

a = float(123) # 실수 자료형
print(type(a))


#4-3 사칙연산
    #괄호먼저
    
#4-4 BMI 계산기
height = float(input("키를 입력하세요(m) > "))
weight = float(input("몸무게를 입력하세요(kg) > "))
BMI = weight / height**2
print("BMI지수는 ", round(float(BMI),2), "입니다.")

#4-5 파이썬의 숫자 처리 및 F-string
print(int(8/3)) #정수로 표현
print(round(8/3)) #반올림
print(round(8/3),2) #둘째자리에서 반올림
print(round(3.141592,2))
print(8//3) #버림

#1점씩 더할 때 
score = 0
score += 1

print(score)

# f-string 
score = 0
height = 1.8
earth = True
print("당신의 스코어는 {}, 당신의 키는 {}, 당신은 지구인 입니까 ? {}".format(score,height,earth))
print(f"당신의 스코어는 {score}, 당신의 키는 {height}, 당신은 지구인 입니다.{earth}")