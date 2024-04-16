# 2024-04-16
import sys
from collections import deque

N = int(sys.stdin.readline())
d1 = deque(list(map(int, sys.stdin.readline().split())))
d2 = deque(list(map(int, sys.stdin.readline().split())))

price = d2.popleft()
distance = d1.popleft()
ans = price * distance
while d1 :
    temp = d2.popleft()
    if temp < price :
        price = temp
    distance = d1.popleft()
    ans += price * distance
sys.stdout.write(''.join([str(ans), '\n']))