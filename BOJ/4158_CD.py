# 2024-02-18
import sys

while True :
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0 : break
    A = [int(sys.stdin.readline()) for n in range(N)]
    B = [int(sys.stdin.readline()) for m in range(M)]
    C = set(A) & set(B)
    sys.stdout.write(''.join([str(len(C)), '\n']))