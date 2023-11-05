# 2023-11-05
import sys

N, M = map(int, sys.stdin.readline().split())
for n in range(N) :
    l = sys.stdin.readline().rstrip()
    for m in range(M-1, -1, -1) : sys.stdout.write(l[m])
    sys.stdout.write('\n')