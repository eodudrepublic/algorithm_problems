# 2023-05-18 (05-19)
import sys

N = int(sys.stdin.readline())
grade = list(map(int, sys.stdin.readline().split()))
M = max(grade)

sum = 0
for i in grade :
    sum += i/M*100

print(sum/N)