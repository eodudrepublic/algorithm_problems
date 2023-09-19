# 2023-09-19 (09-20)
# A/B - 2
import sys

a, b = map(int, sys.stdin.readline().split())
sys.stdout.write(str(a//b))

if a % b:
    sys.stdout.write('.')
    i = 0
    while a % b and i < 1000: 
        a = a % b * 10
        i += 1
        sys.stdout.write(str(a//b))
sys.stdout.write('\n')