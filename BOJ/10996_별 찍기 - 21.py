# 2023-04-13 (04-14)
import sys

N = int(sys.stdin.readline())
q = N//2
r = N%2

for n in range(N) :
        sys.stdout.write(''.join(['* '*(q+r), '\n']))
        if N != 1 :
            sys.stdout.write(''.join([' *'*(q), '\n']))