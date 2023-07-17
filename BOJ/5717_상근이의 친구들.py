# 2023-07-02 (07-03)
import sys

while True :
    A, B = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0 : break
    sys.stdout.write(''.join([str(A+B), '\n']))