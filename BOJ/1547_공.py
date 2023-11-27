# 2023-11-27
import sys

N = int(sys.stdin.readline())

now = 1
for n in range(N) :
    a, b = map(int, sys.stdin.readline().split())
    if a == now : now = b
    elif b == now : now = a

sys.stdout.write(''.join([str(now), '\n']))