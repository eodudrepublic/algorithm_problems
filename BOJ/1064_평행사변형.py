# 2024-04-13 (04-14)
x0, y0, x1, y1, x2, y2 = map(int, input().split())
while True :
    try :
        if (y2 - y1) / (x2 - x1) == (y1 - y0) / (x1 - x0) :
            print("-1.0")
            break
    except :
        if x0 == x1 and x1 == x2 and x2 == x0 :
            print("-1.0")
            break
    arr = [((y1 - y0)**2 + (x1 - x0)**2)**(1/2), ((y2 - y0)**2 + (x2 - x0)**2)**(1/2), ((y2 - y1)**2 + (x2 - x1)**2)**(1/2), ]
    L = max(arr)
    l = min(arr)
    print((L-l)*2)
    break