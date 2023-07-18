# 2023-07-18
import sys

N = int(sys.stdin.readline())
for n in range(N) :
    r, e, c = map(int, sys.stdin.readline().split())
    if r > e-c : print('do not advertise')
    elif r == e-c : print('does not matter')
    else : print('advertise')