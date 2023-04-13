# 3-1 띄어쓰기
print("hello")
print('hello'+'world')
print('hello'+' '+'world') # ' ' 공백도 글씨로 인식

# 3-2 디버깅 연습


# 3-3 입력함수

input("당신의 이름은 무엇입니까?")
print("나는" + input("당신의 이름은 무엇입니까?") + "입니다.")

# 3-4 입력함수 2 

print(len(input("당신의 이름은 무엇입니까?")))

# 3-5 python 변수1
name = input("당신의 이름은 무엇입니까?")
print(name)

length = len(name)
print(length)

# 3-6 python 변수1

a = input("a:")
b = input("b:")

temp = a
a = b
b = temp

print("a = " + a)
print("b = " + b)

# 3-7 챌린지 퀴즈

movie = input("내가 좋아하는 영화: ")
star = input("주인공: ")

print("내가 좋아하는 영화는 " + movie + "이고, 주인공은 " + star + "다.")