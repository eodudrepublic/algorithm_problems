# 2023-04-21 (04-22)
import sys

N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

N = 0
for n in num :
    if n == 1 :
        continue
    N += 1
    for i in range(2, n) :
        if n%i == 0 :
            N -= 1
            break

print(N)