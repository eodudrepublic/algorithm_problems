# 2023-07-12 (07-13)
import sys

A, I = map(int, sys.stdin.readline().split())
sys.stdout.write(''.join([str(A*(I-1)+1), '\n']))