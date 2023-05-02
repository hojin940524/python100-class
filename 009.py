#python 009

# for 반복문
fruits = ['사과', '복숭아', '배'] #리스트 생성
for fruit in fruits:
    print(fruit) #리스트의 항목을 하나씩 출력
    print(fruit + ' 파이')
    print(fruits) 

# 평균키 구하기 - 방법 1
student_heights = input('학생들 키 리스트를 입력하세요! 입력시 띄어쓰기(스페이스키)해서 값을 구분하세요.').split()

student_num = len(student_heights)
print(student_num)

for n in range(0, student_num):
    student_heights[n] = int(student_heights[n])

height_avg = sum(student_heights)/student_num

print(height_avg)

# 평균키 구하기 - 방법 2
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)
num_of_students = len(student_heights)
height_avg = round(total_height/num_of_students)
print(height_avg)

# 평균키 구하기 - 방법 3
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)
num_of_students = 0
for student in student_heights:
    num_of_students += 1
print(num_of_students)
height_avg = round(total_height/num_of_students)
print(height_avg)

#학생들의 점수 중 가장 높은 점수
student_scores = input("점수 리스트를 입력한다(점수는 스페이스로 구분한다): ").split()
# student_score = [78, 65, 89, 86, 55, 91, 64, 89]
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# print(max(student_scores))
# 리스트의 최대값은 max 함수 최소값은 min 함수사용 
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f" 가장 높은 점수는 : {highest_score}")
