# -*- coding: utf-8 -*-

fibo_list = [0, 1]
num = int(input("你想看費氏數列第幾個數字？ "))

for i in range(2, num):
    num = fibo_list[-1] + fibo_list[-2]
    fibo_list.append(num)

print('費氏數列第', num, '個數字是', fibo_list[-1])
