#python 007 
#로또번호 생성기


#내가 입력한 로또번호
num1 = int(input('첫번째 숫자를 입력하세요> '))
num2 = int(input('두번째 숫자를 입력하세요> '))
num3 = int(input('세번째 숫자를 입력하세요> '))
num4 = int(input('네번째 숫자를 입력하세요> '))
num5 = int(input('다섯번째 숫자를 입력하세요> '))
num6 = int(input('여섯번째 숫자를 입력하세요> '))

my_nums = [num1,num2,num3,num4,num5,num6]
my_nums.sort()

print(f'당신이 선택한 로또 번호는 {my_nums} 입니다.')

#컴퓨터가 랜덤으로 뽑은 로또번호
import random
nums = random.sample(range(1,46),6)  #random.sample(범위 , 개수) 무작위로 범위에서 개수만큼 요소 추출
nums.sort()

# random 모듈
# 1> 난수 생성
# random.random(): 0부터 1 사이의 난수를 반환
# random.randint(a, b): a부터 b까지의 정수 중 하나를 무작위로 반환
# random.uniform(a, b): a와 b 사이의 실수 중 하나를 무작위로 반환
# 2> 시퀀스 임의 순서화
# random.shuffle(seq): 시퀀스(리스트 등)의 항목을 무작위로 섞습니다.
# random.sample(population, k): population에서 k개의 항목을 무작위로 선택하여 리스트로 반환
# 3> 난수 시드(seed) 설정
# random.seed(a=None): 난수 발생을 위한 시드를 설정. 인자로 정수를 넘기면 항상 같은 난수가 생성

print('추첨된 로또 번호는 ', nums , '입니다. ')

#일치 / 불일치
if(my_nums  == nums):
    print('*** 축!! 당첨 ***')
else:
    print('꽝 다음기회에')