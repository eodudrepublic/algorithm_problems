# 2024-04-12
import sys
    
T = int(sys.stdin.readline())
for t in range(T) :
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
    
    size = 0
    h = y2 - y1
    for x in range(x1, x2) :
        if x3 <= x and x < x4 :
            for y in range(y1, y2) :
                if y3 > y or y >= y4 :
                    size += 1
        else :
            size += h
    sys.stdout.write(''.join([str(size), '\n']))