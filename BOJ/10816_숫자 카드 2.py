# 2024-03-19 (03-20)
import sys

n = sys.stdin.readline()
arr = list(map(int, sys.stdin.readline().split()))
dict = {}
for _ in arr :
    if _ in dict :
        dict[_] += 1
    else :
        dict[_] = 1
n = sys.stdin.readline()
ans = list(map(int, sys.stdin.readline().split()))
for _ in ans :
    if _ in dict :
        sys.stdout.write(''.join([str(dict[_]), ' ']))
    else :
        sys.stdout.write('0 ')
sys.stdout.write('\n')