# 2024-04-24 (04-25)
N, a, b = map(int, input().split())
L = (a**2 + b**2)**(1/2)
for n in range(N) :
    l = int(input())
    if l <= L :
        print('DA')
    else :
        print('NE')