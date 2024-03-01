# 2024-03-01 (03-02)
import sys
from collections import deque

N = int(sys.stdin.readline())

stack = deque()
for n in range(N) :
    op = sys.stdin.readline().rstrip()
    if op[0] =='1' :
        a, b = op.split()
        stack.append(int(b))
    elif op[0] == '2' :
        if not stack : sys.stdout.write('-1\n')
        else : sys.stdout.write(''.join([str(stack.pop()), '\n']))
    elif op[0] == '3' :
        sys.stdout.write(''.join([str(len(stack)), '\n']))
    elif op[0] == '4' :
        if not stack : sys.stdout.write('1\n')
        else : sys.stdout.write('0\n')
    elif op[0] == '5' :
        if not stack : sys.stdout.write('-1\n')
        else : sys.stdout.write(''.join([str(stack[-1]), '\n']))
    else :
        pass