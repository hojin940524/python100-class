#python 007 

# lower() / upper() 
print('생각나는 영 단어 2개를 입력하세요> ')
word1 = input('영 단어 1 > \n')
word2 = input('영 단어 2 > \n')
word3 = input('영 단어 3> \n')

eng_word = word1 + word2 + word3
upper_string = eng_word.upper()
lower_string = eng_word.lower()

print(upper_string)
print(lower_string)

# count() - 괄호 안에 있는 특정 알파벳의 개수를 셀 수 있다
word_count_upper = upper_string.count('A')
word_count_lower = lower_string.count('a')
print(word_count_upper)
print(word_count_lower)



#랜덤 
import random #모듈 불러오기
                #모듈이란? 라이브러리(사람들이 개발 해놓은 or 직접 만든 프로그램을 사용할 수 있도록 불러온다)

random_int = random.randint(1,10)  #random.randint(a,b) a~b 사이의 수를 랜덤으로 보여줌
print(random_int)

random_float1 = random.random()  #random.random() 0 ~ 1 사이의 부동 소수점 랜덤 출력
print(random_float1)
random_float2 = random.random() * 5 #random.random() 0 ~ 4.9999999 사이의 부동 소수점 랜덤 출력
print(random_float2)

