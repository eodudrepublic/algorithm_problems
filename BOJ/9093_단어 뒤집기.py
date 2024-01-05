# 2024-01-05 (01-06)
import sys

N = int(sys.stdin.readline())
for n in range(N) :
    arr = list(sys.stdin.readline().rstrip().split())
    for _ in arr :
        tmp = reversed(_)
        for t in tmp : sys.stdout.write(t)
        sys.stdout.write(' ')
    sys.stdout.write('\n')