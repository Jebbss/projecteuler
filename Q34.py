#Find the sum of all numbers which are
#equal to the sum of the factorial of their digits. 
import math
def isSumFactorialDigits(n):
    tmpstr = str(n)
    tmpsum = 0
    for x in range(0,len(tmpstr)):
        tmpsum += math.factorial(int(tmpstr[x]))
        if tmpsum > n:
            return False
    return tmpsum == n
                   

#Upper limit is 2540161 because 9!*7 = 2540160 and 9!*8 < 10,000,000
def main():
    SumFactDig = 0
    for x in range (5,2540161):
        if isSumFactorialDigits(x):
            SumFactDig += x
    print SumFactDig
