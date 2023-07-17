# 2023-06-18 (06-19)
import sys

input = sys.stdin.readline

def space(p1, p2, p3) :
    return (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p1[1]*p2[0] - p2[1]*p3[0] - p3[1]*p1[0])/2

N = int(input())
p = []
for n in range(N) :
    p.append(tuple(map(int, input().split())))

s = 0
for _ in range(2, N) :
    s += space(p[0], p[_-1], p[_])

print(round(abs(s), 1))
# 그래서 오목한 다각형이 뭔데??