# 2023-04-04
import sys

def fib(n) :
    result = [0, 1]
    for i in range(1, n) :
        result.append((result[i-1]+result[i])%1000000007)
    return result[n]
        

N = int(sys.stdin.readline())
print(fib(N))