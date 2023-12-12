# 2023-12-12
import sys

a, b = map(int, sys.stdin.readline().split())
if a > b : a, b = b, a
elif a == b : 
    sys.stdout.write('0\n')
    sys.exit()
sys.stdout.write(''.join([str(b-a-1), '\n']))
for _ in range(a+1, b) : sys.stdout.write(''.join([str(_), ' ']))
sys.stdout.write('\n')