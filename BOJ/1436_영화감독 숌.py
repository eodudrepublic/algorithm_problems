# 2023-04-23 (04-24)
import sys

N = int(sys.stdin.readline())

i = 666
n = 1

while n != N :
    i += 1
    if '666' in str(i) :
        n += 1

print(i)