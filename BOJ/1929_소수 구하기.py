# 2023-05-11 (05-12)
import sys
import math

def is_pnum(n) :
    if n == 1 : return False
    for i in range(2, int(math.sqrt(n))+1) :
        if n % i == 0 : return False
    return True

M, N = map(int, sys.stdin.readline().split())
for n in range(M, N+1) :
    if is_pnum(n) :
        sys.stdout.write(''.join([str(n), '\n']))