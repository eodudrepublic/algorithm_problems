# 2023-04-06
import sys

def in_P(sp, ep, p) :
    xs = sp[0]
    ys = sp[1]
    xe = ep[0]
    ye = ep[1]
    x = p[0]
    y = p[1]
    d = p[2]
    ls = ((xs-x)**2 + (ys-y)**2)**(1/2)
    le = ((xe-x)**2 + (ye-y)**2)**(1/2)
    
    if ls < d and le < d :
        return False
    elif ls < d :
        return True
    elif le < d :
        return True
    else :
        return False

T = int(sys.stdin.readline())

for t in range(T) :
    x1, y1, x2, y2 = map(int, sys. stdin.readline().split())
    sp = [x1, y1]
    ep = [x2, y2]
    N = int(sys.stdin.readline())
    P = []
    for n in range(N) :
        p = list(map(int, sys.stdin.readline().split()))
        P.append(p)
    tp = 0
    for p in P :
        if in_P(sp, ep, p) :
            tp += 1
    print(tp)