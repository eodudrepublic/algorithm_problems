# 2024-01-19
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
if N == 0 : sys.stdout.write('1 0\n')
else : sys.stdout.write(' '.join([str(fib(N-1)), str(fib(N)), '\n']))