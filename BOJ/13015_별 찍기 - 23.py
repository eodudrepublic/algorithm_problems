# 2023-04-12
import sys

N = int(sys.stdin.readline())

gap = 2*N-3
sys.stdout.write(''.join(['*'*N, ' '*gap, '*'*N, '\n']))
for n in range(1, N-1) :
    gap -= 2
    sys.stdout.write(''.join([' '*n, '*', ' '*(N-2), '*']))
    sys.stdout.write(''.join([' '*gap, '*', ' '*(N-2), '*', '\n']))
sys.stdout.write(''.join([' '*(N-1), '*', ' '*(N-2), '*', ' '*(N-2), '*', '\n']))
for rn in range(N-2, 0, -1) :
    sys.stdout.write(''.join([' '*rn, '*', ' '*(N-2), '*']))
    sys.stdout.write(''.join([' '*gap, '*', ' '*(N-2), '*', '\n']))
    gap += 2
sys.stdout.write(''.join(['*'*N, ' '*gap, '*'*N, '\n']))