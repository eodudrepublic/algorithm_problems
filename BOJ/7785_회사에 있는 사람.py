# 2024-01-24
import sys

N = int(sys.stdin.readline())
arr = set()
for n in range(N) :
    name, op = sys.stdin.readline().rstrip().split()
    if op == 'enter' : 
        arr.add(name)
    elif op == 'leave' :
        arr.remove(name)
    else :
        pass

ans = sorted(arr, reverse=True)
for _ in ans :
    sys.stdout.write(''.join([_, '\n']))

