# 2024-04-09
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
_index = n - k
num = deque(sys.stdin.readline().rstrip())
ans = deque([num.popleft()])
while num :
    temp1 = num.popleft()
    temp2 = ans.pop()
    if temp1 < temp2 :
        ans.append(temp2)
        ans.append(temp1)
    elif temp1 == temp2 :
        ans.append(temp2)
        ans.append(temp1)
    else :
        if ans :
            num.appendleft(temp1)
        else :
            ans.append(temp1)
        k -= 1
        if k == 0 : break

_ = 0
while ans :
    sys.stdout.write(str(ans.popleft()))
    _ += 1
    if _ == _index : break
while num :
    if _ == _index : break
    sys.stdout.write(str(num.popleft()))
    _ += 1
sys.stdout.write('\n')