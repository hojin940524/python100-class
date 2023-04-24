#python 008

#list - 데이터가 여러개 일때 []대괄호 안에 데이터를 순서대로 넣는다(순서가 중요!!)

HT_student = ['권세희','권용석','박인호','송유정','우현주','정선아','조아라','최호진','안영훈']
print(len(HT_student)) #list 개수 세기 - len()
print(HT_student)
print(HT_student[7]) #0부터 시작
print(HT_student[-2]) #음수이면, 뒤부터 카운트(시작번호 - 1)

HT_student.append('홍길동') #list 추가시(1개) .append() 함수 사용 
print(HT_student) 

HT_student.extend(['김인공','이지능','박융합']) #list 추가시(여러개) .extend() 함수 사용 
print(HT_student) 

#split - 문자열을 특정 구분 기호에 따라 별도의 구성요소로 나누는 역활
name_class = input("아이스크림 내기에 참여할 사람의 이름 입력, 쉼표를 사용해서 이름을 구분해줘: ")
names = name_class.split(", ")
print(names)

#EX> 아이스크림 내기
import random
num_person = len(names) #list에 있는 이름의 개수
random_choice = random.randint(0,num_person-1)

winner = names[random_choice]
print(winner,'!! 아이스크림 사기!!!')

#중첩 list
fruits= ['딸기', '복숭아','배','천도복숭아', '사과', '포도', '체리', '블루베리']
vegetables = ['시금치', '케일', '피망', '강낭콩']

dirty_dozen = [fruits, vegetables]
print(dirty_dozen) 