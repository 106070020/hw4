# -*- coding: utf-8 -*-

num = int(input("Enter a number: "))

for i in range(2, num):
    if num % i == 0:
        print("NOT PRIME")
        break
else:
    print("PRIME")
