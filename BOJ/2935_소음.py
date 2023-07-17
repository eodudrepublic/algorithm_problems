# 2023-07-09 (07-10)
import sys

A = int(sys.stdin.readline())
op = sys.stdin.readline().strip()
B = int(sys.stdin.readline())

if op == '+' : sys.stdout.write(''.join([str(A+B), '\n']))
else : sys.stdout.write(''.join([str(A*B), '\n']))