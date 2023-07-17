# 2023-04-05 (04-06)
import sys

T = int(sys.stdin.readline())

for t in range(T) :
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    if x1 == x2 and y1 == y2 and r1 == r2 :
        print(-1)
        continue
    
    d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    if r1 < r2 :
        temp = r1
        r1 = r2
        r2 = temp

    if r1-r2 < d and r1+r2 > d :
        print(2)
    elif r1-r2 > d or r1+r2 < d :
        print(0)
    else :
        print(1)