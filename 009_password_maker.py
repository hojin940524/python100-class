#비밀번호 생성기
# 문자를 몇개를 넣을까요? 
# 기호는 몇개를 넣을까요?
# 숫자는 몇개를 넣을까요?
# 생성된 비밀번호 :

print('*** 비밀번호 생성기 입니다 ***')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
           'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
           'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random
ct_letters = int(input('몇자리 비밀번호를 원하십니까?\n'))
ct_symbols = int(input('기호는 몇개를 넣을까요?\n'))
ct_numbers = int(input('숫자는 몇개를 넣을까요?\n'))

make_letters = random.sample(letters,ct_letters-(ct_symbols+ct_numbers)) #문자 랜덤 뽑기(입력한 개수 만큼)
make_symbols = random.sample(symbols,ct_symbols) #기호 랜덤 뽑기(입력한 개수 만큼)
make_numbers = random.sample(numbers,ct_numbers) #숫자 랜덤 뽑기(입력한 개수 만큼)

password_list = [] # 빈 리스트을 만듬. 

for make_letter in make_letters: #랜덤으로 뽑은 문자를 하나씩 리스트에 .append 하기
    password_list.append(make_letter) 
for make_symbol in make_symbols:
    password_list.append(make_symbol)
for make_number in make_numbers:
    password_list.append(make_number)

## print(password_chars) 문자, 기호, 숫자 순으로 랜덤으로 뽑은 비밀번호
random.shuffle(password_list) # 문자, 기호, 숫자를 랜덤으로 섞음.
password = password_list[:ct_letters] #비밀번호 = 원하는 개수만큼 
print('생성된 비밀번호는 ', password, '입니다.')

    

