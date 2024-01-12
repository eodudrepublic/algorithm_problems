# 2024-01-12
import sys

i = 0
while True :
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0 : break
    i += 1
    if c % b >= a : ans = a * (c // b) + a
    else : ans = a * (c // b) + (c % b)
    print(f'Case {i}: {ans}')