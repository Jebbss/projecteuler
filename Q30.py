#Find the sum of all the numbers that can be written
#as the sum of fifth powers of their digits.

import math
def SumDigitsTo5thPower(n):
    tmpstr = str(n)
    tmpsum = 0
    for x in range(0,len(tmpstr)):
        tmpsum += math.pow(int(tmpstr[x]),5)
        if tmpsum > n:
            return False
    return tmpsum == n
                   

#Upper limit is 355000 because 9^5 = 59049 and (9^5)*6 = 354294
#So 355000 seems reasonable 
def main():
    SumDigTo5th = 0
    for x in range (2,355000):
        if SumDigitsTo5thPower(x):
            SumDigTo5th += x
    print SumDigTo5th
