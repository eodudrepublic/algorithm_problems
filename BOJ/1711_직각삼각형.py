import sys
from itertools import combinations

input = sys.stdin.readline
print = sys.stdout.write

def isRT(p1, p2, p3) : 
    vector1 = (p2[0]-p1[0], p2[1]-p1[1])
    vector2 = (p3[0]-p2[0], p3[1]-p2[1])
    vector3 = (p1[0]-p3[0], p1[1]-p3[1])
    if vector1[0]*vector2[0] + vector1[1]*vector2[1] == 0 : return True
    if vector2[0]*vector3[0] + vector2[1]*vector3[1] == 0 : return True
    if vector3[0]*vector1[0] + vector3[1]*vector1[1] == 0 : return True
    else : return False

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
arr = list(range(N))
num = 0
for _ in combinations(arr, 3) : 
    if isRT(P[_[0]], P[_[1]], P[_[2]]) : num += 1
print(''.join([str(num), '\n']))