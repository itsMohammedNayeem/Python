import random

a = [1,1,1,6,7,8,9,4,9]
b = [1,6,87,98,67,45,10,11,12,13,14,15,16]


print(set(a) & set(b))



__author__ = 'Nayeem'

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [number for number in a if number % 2 == 0]

print(b)