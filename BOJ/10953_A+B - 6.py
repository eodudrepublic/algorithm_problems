# 2023-07-05 (07-06)
import sys

T = int(sys.stdin.readline())
for t in range(T) :
    A, B = map(int, sys.stdin.readline().split(','))
    sys.stdout.write(''.join([str(A+B), '\n']))