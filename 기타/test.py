import sys
from collections import deque
from queue import PriorityQueue as PQ

input = sys.stdin.readline
# print = sys.stdout.write

def isRT(p1, p2, p3) :
    L = sorted([
        (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2,
        (p2[0]-p3[0])**2 + (p2[1]-p3[1])**2,
        (p3[0]-p1[0])**2 + (p3[1]-p1[1])**2
    ])
    print(L)
    
isRT((0, 0), (3, 0), (3, 4))