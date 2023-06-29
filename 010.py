#list와 tuple의 차이 - 변경 가능/불가능

##list 예시
list1 = [1,2,3, 4, 5,6,11,'a','b'] #어떻게 입력하던지 띄어쓰기 규칙을 가지고 출력된다.
print(type(list1), list1)

##index 예시
print(list1[1], list1[7]) # 2,a
print(list1[2:5]) # res> [3,4,5]
print(list1[:7]) # res> [1,2,3,4,5,6,11]
print(list1[4:]) # res> [5,6,11,'a','b']
print(list1[-1]) # res> b 
print(list1[-4:]) # res> [6,11,'a','b']
print(list1[1+2:]) # res> [4,5,6,11,'a','b']  ##slicing - 인덱스를 이용해서 잘라내는것!

##list 추가
list1 = [1, 2, 3, 4, 5, 6, 11, 'a', 'b']
list1[6] = 'c'
print(list1) # res> [1, 2, 3, 4, 5, 6, 'c', 'a', 'b']

##list 추가 (element 없는 리스트)
list2 = []

for item in range(11, 14, 1):
    list2 += [item] # or list2.appenf(item)

print(list2) # res > [11, 12, 13]

##list와 tuple 예시
list3 = []
list3 += 'python'
print(list3, len(list3)) # res > ['p', 'y', 't', 'h', 'o', 'n'] 6

list3 += ('s', 't', 'u', 'd', 'y')
print(list3, len(list3)) # res > ['p', 'y', 't', 'h', 'o', 'n', 's', 't', 'u', 'd', 'y'] 11

##list 연결
list1 = [1,2,3,4,5,6,11,'a','b']
list2 = [11,12,13]

list12 = list1 + list2
print(list12) # res > [1, 2, 3, 4, 5, 6, 11, 'a', 'b', 11, 12, 13]

#for문을 활용한 인덱싱과 element 확인
for i in range(len(list12)):
    print(f'({i}, {list12[i]})', end = '')
    # res > (0, 1)(1, 2)(2, 3)(3, 4)(4, 5)(5, 6)(6, 11)(7, a)(8, b)(9, 11)(10, 12)(11, 13)

##tuple

t1 = 10, 20 , 30, 'john' #()괄호를 넣어도 되고, 넣지 않아도 가능
t1 += (40, 50)
print(t1)


t3 = 'A', 'B', 'C', '[90, 80, 70]'
print(t3, len(t3), t3[3])
# res > ('A', 'B', 'C', '[90, 80, 70]') 4 [90, 80, 70]

t4 = (('A', 'B', 'C'), [90, 80, 70])
print(len(t4)) # 2개
grade, number = t4 # 타입이 다른 두개를 변수로 할당 할 수 있다
print(grade, number, type(grade), type(number))
# res > ('A', 'B', 'C') [90, 80, 70] <class 'tuple'> <class 'list'>

#unpacking a list 파이선에서 모든 시퀀스(배열)는 언패킹이 가능.
num1, num2, num3 = number
print(num1, num2, num3) # res > 90 80 70

first, second, third, fourth = 'WIFI'
print(first, second, third, fourth) # res > W I F I