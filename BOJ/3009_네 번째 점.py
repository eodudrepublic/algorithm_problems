# 2023-07-14 (07-15)
import sys

X = []
Y = []
for n in range(3) :
    x, y = map(int, sys.stdin.readline().split())
    if x in X : X.remove(x)
    else : X.append(x)
    if y in Y : Y.remove(y)
    else : Y.append(y)
print(X[0], Y[0])