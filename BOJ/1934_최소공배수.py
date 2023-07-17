# 2023-06-22 (06-23)
import sys
from math import lcm

N = int(sys.stdin.readline())
for n in range(N) :
    a, b = map(int, sys.stdin.readline().split())
    sys.stdout.write(''.join([str(lcm(a, b)), '\n']))