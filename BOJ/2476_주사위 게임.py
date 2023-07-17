# 2023-07-13 (07-14)
import sys

N = int(sys.stdin.readline())

point = []
for n in range(N) :
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b and b == c : point.append(10000+a*1000)
    elif a != b and b != c and c != a : point.append((max([a, b, c])*100))
    else :
        if a == b : point.append(1000 + a*100)
        elif b == c : point.append(1000 + b*100)
        else : point.append(1000 + c*100)

print(max(point))