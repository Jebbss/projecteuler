#Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def main():
    mod = 10000000000
    ans = 0
    for x in range (1,1000):
        ans += (x**x) % mod
    print ans % mod
        
