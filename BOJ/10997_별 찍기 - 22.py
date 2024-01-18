# 2024-01-18
import sys
from collections import deque

ans = deque(['*****', '*', '* ***', '* * *', '* * *', '*   *', '*****'])

N = int(sys.stdin.readline())

n = 1
if N == 1 : sys.stdout.write('*\n')    

while n < N :
    n += 1
    if n == N : 
        sys.stdout.write('\n'.join(ans))
        sys.stdout.write('\n')
        break
    ans[0] = ''.join(['* ', ans[0], '**'])
    ans[1] = ''.join([ans[1], ' ' * (n * 4 - 4)])
    for _ in range(1, n * 4 - 1) : ans[_] = ' '.join(['*', ans[_], '*'])
    ans.appendleft('*')
    ans.append(''.join(['*', ' ' * (n * 4 - 1), '*']))
    ans.appendleft('*' * (n * 4 + 1))
    ans.append('*' * (n * 4 + 1))