# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

from math import sqrt

def fibBinet(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

def main():
    n = 1
    tmpnum = 0
    sumEve = 0
    while tmpnum < 4000000:
        tmpnum = int(fibBinet(n))
        if tmpnum % 2 == 0:
            sumEve += tmpnum
        n += 1
    print sumEve

'''
Used Binet's Fibbonoci formula 
'''
