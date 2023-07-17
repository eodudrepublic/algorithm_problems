# 2023-04-13 (04-14)
import sys

li = []
for n in range(9) :
    num = int(sys.stdin.readline())
    li.append(num)

max = max(li)
print(max)
print(li.index(max)+1)
