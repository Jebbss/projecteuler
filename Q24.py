##A permutation is an ordered arrangement of objects.
##For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
##If all of the permutations are listed numerically or alphabetically,we call it lexicographic order.
##The lexicographic permutations of 0, 1 and 2 are:
##
##012   021   102   120   201   210
##
##What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math

def main():
    Target = 999999 ##because numbers[] is first permutation 
    n = 10
    fact = 0
    pos = 0
    answerStr = ""
    numbers = ['0','1','2','3','4','5','6','7','8','9']

    fact = math.factorial(n)
    if fact < Target:
        print "There are not ",Target," permuations of ",n," digits."
        return -1
    n -= 1
    while numbers:
        fact = math.factorial(n)
        pos = Target/fact
        answerStr += numbers.pop(pos)
        Target = Target - fact * pos
        n-= 1
        
    print answerStr 

