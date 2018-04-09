# -*- coding: utf-8 -*-


def compute_fibonacci(num):
    if num==1:
        return 0
    elif num==2:
        return 1
    else:
        return compute_fibonacci(num-1) + compute_fibonacci(num-2)


num = int(input("你想看費氏數列第幾個數字？ "))
print('費氏數列第', num, '個數字是', compute_fibonacci(num))
