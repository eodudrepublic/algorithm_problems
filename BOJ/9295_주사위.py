# 2023-08-08 (08-09)
import sys

T = int(sys.stdin.readline())
for t in range(1, T+1) :
    a, b = map(int, sys.stdin.readline().split())
    sys.stdout.write(''.join(['Case ', str(t), ': ', str(a+b), '\n']))