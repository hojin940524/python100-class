#4일차 QUIZ

#1. 잘못된 설명은 무엇일까요?   
    #- a. 932는 정수다.
    #- b. "false"는 부울값이다
    #- c. 857.25 는 실수다
    #- d. "523"은 문자열이다

 # 답 -> b ("" 큰따옴표를 사용하면 문자열)

#2. 변수 mystery의 데이터 형식은 무엇일까요? 

mystery = 734_529.678

    # - a. 정수
    # - b. 문자열
    # - c. 부울값
    # - d. 실수

 # 답 -> d 실수
print(type(mystery)) #답 확인 <class 'float'>

#3. 다음 코드로 출력하게 될 값은? 
street_name = "동산면 영서로 1290-31"
print(street_name[4] + street_name[9])

# 답 -> 영2

#4. 2자리의 숫자를 입력받아 앞자리와 뒷자리의 값을 더하세요.
num = input("두자리 수 입력> ")
num_sum = int(num[0])+int(num[1])
print("얖자리와 뒷자리의 합 = ", num_sum)
