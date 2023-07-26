# 2023-07-26 (07-27)
import sys

while True :
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 : break
    if a % b == 0 : sys.stdout.write('multiple\n')
    elif b % a == 0 : sys.stdout.write('factor\n')
    else : sys.stdout.write('neither\n')