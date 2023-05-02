#python 009

#for반복문과 range()함수

#for number in range(a, b): - 반복수행을 통해 한 범위의 숫자를 만들고 싶은 경우
for number in range(1,10):
    print(number)

for number in range(1,10,3): # range(a,b,c)- a~b 범위에서 c씩 증가
	print(number)


#1~100더하기
sum_1_100 = 0
for number in range(1,101):  
    sum_1_100 += number
    print(sum_1_100)
#짝수 더하기(1~100) 방법1
even_sum = 0
for even_num in range(2,101,2):
    even_sum += even_num
    print(even_sum)
#짝수 더하기(1~100) 방법2
total = 0
for num1 in range(1,101):
    if num1 % 2 == 0:
        total += num1
#홀수 더하기(1~100)
odd_sum = 0
for odd_num in range(1,101,2):
    odd_sum += odd_num
    print(odd_sum)