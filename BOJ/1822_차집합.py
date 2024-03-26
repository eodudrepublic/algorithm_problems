# 2024-03-26 (03-27)
import sys

temp = sys.stdin.readline()
arr1 = set(map(int, sys.stdin.readline().split()))
arr2 = set(map(int, sys.stdin.readline().split()))
set = arr1 - arr2
ans = sorted(list(set))
if not ans :
    sys.stdout.write('0\n')
else :
    sys.stdout.write(''.join([str(len(ans)), '\n']))
    for _ in ans :
        sys.stdout.write(''.join([str(_), ' ']))
    sys.stdout.write('\n')