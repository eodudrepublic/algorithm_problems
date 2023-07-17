# 2023-04-22 (04-23)
import sys

N = int(sys.stdin.readline())

num = [0]*10000
for n in range(N) :
    i = int(sys.stdin.readline())
    num[i-1] += 1

for i in range(10000) :
    if num[i] == 0 :
        continue
    for n in range(num[i]) :
        sys.stdout.write(str(i+1))
        sys.stdout.write('\n')