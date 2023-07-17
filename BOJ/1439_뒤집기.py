# 2023-05-06
import sys

S = list(sys.stdin.readline().strip())

sorted = []
c = '-1'
for i in S :
    if i != c :
        sorted.append(int(i))
        c = i

zero = sorted.count(0)
one = sorted.count(1)

if zero < one :
    print(zero)
else :
    print(one)