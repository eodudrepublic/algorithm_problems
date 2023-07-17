# 2023-03-31
import sys

S = int(sys.stdin.readline())

n = 1
while True :
    if n*(n+1) <= 2*S < (n+1)*(n+2) :
        print(n)
        break
    else :
        n += 1