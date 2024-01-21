# 2024-01-21
import sys

gp = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

num = 0
ans = 0
for _ in range(20) :
    name, grade, point = sys.stdin.readline().rstrip().split()
    if point == 'P' : continue
    num += float(grade)
    ans += float(grade) * gp[point]

print(f'{ans/num:6f}')