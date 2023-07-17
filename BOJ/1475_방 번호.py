# 2023-05-21 (05-22)
import sys

N = list(sys.stdin.readline().strip())

tn = [0]*9
for i in range(len(N)) :
    n = int(N[i])
    if n == 9 : n = 6
    tn[n] += 1

tn[6] = tn[6]//2 + tn[6]%2

print(max(tn))