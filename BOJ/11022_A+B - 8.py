# 2023-06-30
import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())
for t in range(1, T+1) :
    A, B = map(int, input().split())
    print(''.join(['Case #', str(t), ': ', str(A), ' + ', str(B), ' = ', str(A+B), '\n']))