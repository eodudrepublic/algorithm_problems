import sys

M = 1000000007

def fib(K) :
    if fibo[K] == -1 :
        if K % 2 == 0 :
            n = K // 2
            fibo[K] = ((2*fib(n-1) + fib(n))*fib(n)) % M
        else :
            n = (K+1) // 2
            fibo[K] = (fib(n-1) * fib(n-1) + fib(n) * fib(n)) % M
    return fibo[K]

N = int(sys.stdin.readline())
fibo = [-1] * (N+1)
fibo[0] = 0
fibo[1] = 1
fibo[2] = 1

print(fib(N))