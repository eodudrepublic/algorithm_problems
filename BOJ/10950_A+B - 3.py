import sys

N = int(sys.stdin.readline())
for n in range(N) :
    A, B = map(int, sys.stdin.readline().split())
    sys.stdout.write(''.join([str(A+B), '\n']))