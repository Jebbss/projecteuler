#What is the largest prime factor of the number 600851475143 ?

from math import sqrt, ceil

#generates primes to n, see Sieve of Eratosthenes for algorithm 
def primes_to(n):
    size = n//2 #floored quotient of n/2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

#finds largest prime factor of start
def main():
    start = 600851475143
    primes = primes_to(int(ceil(sqrt(start))))
    for x in range (len(primes)-1,0,-1):
        if start % primes[x] == 0:
            return primes[x]
