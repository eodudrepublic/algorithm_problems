import sys

def gets(p1, p2) :
    s = (p1[0] - p2[0]) * (p1[1] - p2[1])
    if s < 0 : return -1 * s
    else : return s
    
    
T = int(sys.stdin.readline())
for t in range(T) :
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
    
    size = 0
    for x in range(x1, x2) :
        pass