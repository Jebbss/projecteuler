def main():
    abundant = AbundantNum()
    i = 0
    AbunSum = 0
    j = len(abundant) - 1
    for x in range(1,28123):
        if x < 24:
            AbunSum += x
        else:
            flag = True
            while i <= j:
                num = abundant[i] + abundant[j]
                if num == x:
                    flag = False
                if num < x:
                    i += 1
                else:
                    j -= 1
            if flag:
                AbunSum += x
            i = 0
            j = len(abundant) - 1
    print AbunSum

def AbundantNum():
    tmplist = []
    tmpnum = 0
    for x in range (11,28123):
        tmpnum = sum(factors(x)) - x
        if tmpnum > x:
            tmplist.append(x)
    return tmplist


def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
