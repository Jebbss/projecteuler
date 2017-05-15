##What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import math 
from math import log10, ceil, sqrt

def fibBinet(n):
    a = (1 + 5**0.5)/2.0
    b = 1-a
    f = n*math.log10(a) + math.log10(1-(b/a)**n)
    return int(ceil(f - math.log10(5**0.5)))

def main():
    n = 1
    while int(fibBinet(n)) < 1000:
        n += 1
    fibBinet(n)
    print n

'''
Used differint forms of Binet's Fibbonoci formula with some log() tricks
'''
