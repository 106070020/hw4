# -*- coding: utf-8 -*-

num_a = int(input("輸入第一個數字: "))
num_b = int(input("輸入第二個數字: "))
gcd = 1

for i in range(gcd+1, min(num_a, num_b)+1):
    if num_a % i == 0 and num_b % i == 0:
        gcd = i

print(num_a, '和', num_b, '的最大公因數是', gcd)
