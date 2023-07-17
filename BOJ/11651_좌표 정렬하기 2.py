# 2023-04-26 (04-27)
import sys

N = int(sys.stdin.readline())

plane = []
for n in range(N) :
    x, y = map(int, sys.stdin.readline().split())
    plane.append([y, x])

plane.sort()
for p in plane :
    sys.stdout.write(''.join([str(p[1]), ' ', str(p[0]), '\n']))