# 2023-04-14
import sys
import math

N = int(sys.stdin.readline())
if N == 0 :
    print(0)
    sys.exit()

nf = math.factorial(N)

liN = list(str(nf))
liN.reverse()

num = 0
for i in range(N+1) :
    if liN[i] != '0' :
        break
    else :
        num += 1
print(num)