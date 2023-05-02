#Fizzbuzz 게임 - 3의 배수: 피지/ 5의 배수: 버즈 / 둘다: 피지버즈!

for nums in range(1,101):
    if nums % 3 == 0 and nums % 5 ==0 :
        print('피지버즈!')
    elif nums % 3 == 0: 
        print('피지')
    elif nums % 5 ==0:
        print('버즈')
    else:
        print(nums)