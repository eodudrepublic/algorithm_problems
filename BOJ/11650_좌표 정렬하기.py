# 2023-04-20 (04-21)
import sys

N = int(sys.stdin.readline())

arr = []
for n in range(N) :
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x, y])

arr.sort()
for p in arr :
    sys.stdout.write(''.join([str(p[0]), ' ', str(p[1]), '\n']))