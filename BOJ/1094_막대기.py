# 2023-04-01
import sys

l = 64
L = [64]
X = int(sys.stdin.readline())

while l != X :
    temp = int(L[-1]/2)
    if l - temp < X :
        L[-1] = temp
        L.append(temp)
    else :
        L[-1] = temp
        l -= temp

print(len(L))