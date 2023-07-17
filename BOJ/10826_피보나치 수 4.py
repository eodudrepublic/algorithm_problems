# 2023-04-01
import sys

def fib(n) :
    result = [0]
    for i in range(0, n) :
        if i == 0 :
            result.append(1)
        else :
            result.append(result[i-1]+result[i])
    return result[-1]
        

N = int(sys.stdin.readline())
print(fib(N))