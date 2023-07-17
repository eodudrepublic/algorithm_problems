# 2023-04-07
import sys

N, B, C = map(int, sys.stdin.readline().split())
factory = list(map(int, sys.stdin.readline().split()))
money = 0
if C >= B :
    for n in factory :
        money += n
    print(B*money)
else :
    a = B
    b = a+C
    c = b+C

    for n in range(0, N-2) :
        if factory[n] == 0 :
            continue
        
        if factory[n+1] > factory[n+2] :
            m = min(factory[n], factory[n+1]-factory[n+2])
            factory[n] -= m
            factory[n+1] -= m
            money += b*m
        
        if factory[n] > 0 and factory[n+1] > 0 and factory[n+2] > 0 :
            m = min(factory[n], factory[n+1])
            factory[n] -= m
            factory[n+1] -= m
            factory[n+2] -= m
            money += c*m
        
        if factory[n] > 0 :
            money += a*factory[n]
            factory[n] = 0

    if factory[-2] > 0 or factory[-1] > 0 :
        m = min(factory[-2], factory[-1])
        factory[-2] -= m
        factory[-1] -= m
        money += b*m

    money += a*factory[-2]
    money += a*factory[-1]

    print(money)