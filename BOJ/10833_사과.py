# 2023-08-06 (08-07)
import sys

N = int(sys.stdin.readline())

A = 0
for n in range(N) :
    a, b = map(int, sys.stdin.readline().split())
    while True : 
        if b - a >= 0 :
            b -= a
        else : 
            A += b
            break
print(A)