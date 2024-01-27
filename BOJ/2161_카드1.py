# 224-01-27
import sys
from collections import deque

n = int(sys.stdin.readline())
arr = deque(range(1, n+1))

while True :
    tmp = arr.popleft()
    if not arr : 
        sys.stdout.write(''.join([str(tmp), '\n']))
        break
    sys.stdout.write(''.join([str(tmp), ' ']))
    tmp = arr.popleft()
    arr.append(tmp)