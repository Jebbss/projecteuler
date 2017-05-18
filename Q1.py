# Find the sum of all the multiples of 3 or 5 below 1000.
# 1000/3 = 333.33, upper bound for multiplier loop is 334

def main():
    sumMul = 0
    tmpnum = 0
    for x in range (1,334):
        sumMul += 3 * x
        tmpnum = 5 * x
        if x < 200 and tmpnum % 3 != 0: # 200*5 = 1000
            sumMul += tmpnum
    print sumMul
        
        
