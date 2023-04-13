import random

lotto_nums = random.sample(range(1, 46), 6)
lotto_nums.sort()

print("로또 번호: ", end="")
for num in lotto_nums:
    print(num, end=" ")