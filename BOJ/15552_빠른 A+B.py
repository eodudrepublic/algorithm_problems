# 2023-09-20
import sys

T = int(sys.stdin.readline())
for t in range(T) :
    a, b = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(a+b))
    sys.stdout.write('\n')