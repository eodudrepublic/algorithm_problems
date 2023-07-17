# 2023-07-11
import sys

while True :
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 : break
    if a > b : sys.stdout.write('Yes\n')
    else : sys.stdout.write('No\n')