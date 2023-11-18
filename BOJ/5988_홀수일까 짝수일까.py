# 2023-11-18
import sys

N = int(sys.stdin.readline())
for n in range(N) :
    k = int(sys.stdin.readline())
    if k % 2 == 0 : sys.stdout.write('even\n')
    else : sys.stdout.write('odd\n')