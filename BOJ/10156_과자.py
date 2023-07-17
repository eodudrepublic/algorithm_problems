# 2023-06-23
import sys

K, N, M = map(int, sys.stdin.readline().split())
if K*N <= M :
    sys.stdout.write('0\n')
else :
    sys.stdout.write(''.join([str(K*N-M), '\n']))