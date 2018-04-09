# -*- coding: utf-8 -*-
import math

def ettn(num):
    k= [j for j in range (2,num-1)]
    p=0
    while True:
        for j in k[p+1:]:
            if j % k[p]==0:
                k.remove(j)
        if k[p]**2 >= k[-1]:
            break
        p+=1
    return k
def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num == 3:
        return True
    for i in ettn(num):
        if num in ettn(num):
            return True
        elif num % i==0:
            return False
        else:
            continue
    return True
    


num = int(input("Enter a number: "))
if is_prime(num):
    print(num, 'is a prime number.')
else:
    print(num, 'is not a prime number.')
