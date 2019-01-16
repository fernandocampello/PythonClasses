# a = 3
# b = 2
#
# if a < b:
#     print(a,b)
# else:
#     print(b,a)
#
# def ordene(a,b):
#     if a < b:
#         print(a,b)
#     else:
#         print(b,a)
#
# x = 2
# y = 3
#
# ordene(x,y)
#
# def sorted_two_number(a,b):
#     if a < b:
#         print(a,b)
#     else:
#         print(b,a)

def sorted_numbers(a,b,c):
    """
    >>> sorted_numbers(1,2,3)
    1 2 3
    >>> sorted_numbers(5,2,3)
    2 3 5
    """
    if a < b and  b < c:
        print(a,b,c)
    elif c < b and b < a:
        print(c,b,a)
    elif a < c and c < b:
        print(a,c,b)
    elif b < a and a < c:
        print(b,a,c)
    elif b < c and c < a:
        print(b,c,a)
    elif b < a and a < c:
        print(b,a,c)
import math

x = math.pi
y = math.e
z = (1+(5)**.5)/2

sorted_numbers(x,y,z)

import doctest
doctest.testmod(verbose=True)
