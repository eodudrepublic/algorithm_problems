# 2023-04-15 (04-16)
import sys

N, M = map(int, sys.stdin.readline().split())

pwD = {}
for n in range(N) :
    ia, pw = sys.stdin.readline().split()
    pwD[ia] = pw

fia = []
for m in range(M) :
    ia = sys.stdin.readline().strip()
    fia.append(ia)

for m in range(M) :
    ia = fia.pop(0)
    sys.stdout.write(''.join([pwD[ia], '\n']))
