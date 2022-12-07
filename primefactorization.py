from sympy.ntheory import factorint
import math


def factorsint(num):
    poss_p = math.floor(math.sqrt(num))
    if poss_p % 2 == 0:
        poss_p += 1
    while poss_p < num:
        if num % poss_p == 0:
            return poss_p
        poss_p += 2


# n = 955933250882005692895759
n = 46311455882459324736538177937
# n = int(input("Enter n: "))
print("Given number is : ",n)
print("Prime factors are: ", factorint(n))
