# 2023-06-14 (06-15)
import sys
from queue import PriorityQueue as PQ

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
pq = PQ()

for n in range(N) :
    x = int(input())
    if x == 0 :
        if pq.empty() :
            print('0\n')
        else :
            print(str(pq.get()[1]))
            print('\n')
        continue
    _x = x
    if x < 0 : _x *= -1     # 왜 이것만으로 맞는건지 모르겠음
    pq.put((_x, x))