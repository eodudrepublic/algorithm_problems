# 2023-04-11
import sys

def hanoi(now, remain, dest, n) :
    if n < 2 :
        print(now, dest)
    else :
        hanoi(now, dest, remain, n-1)
        hanoi(now, remain, dest, 1)
        hanoi(remain, now, dest, n-1)

N = int(sys.stdin.readline())
print(2**N - 1)

if N <= 20 :
    tower = hanoi(1, 2, 3, N)