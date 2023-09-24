# 2023-09-24 (09-25)
import sys

input = sys.stdin.readline

rec = int(input())
N = int(input())

total = 0
for n in range(N) :
    a, b = map(int, input().split())
    total += a * b

if rec == total : sys.stdout.write('Yes\n')
else : sys.stdout.write('No\n')