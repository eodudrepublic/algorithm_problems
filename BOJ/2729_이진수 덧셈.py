# 2023-09-18
import sys

N = int(sys.stdin.readline())
for n in range(N) :
    a, b = sys.stdin.readline().rstrip().split()
    ba = int(a, 2)
    bb = int(b, 2)
    print(format(ba+bb, 'b'))