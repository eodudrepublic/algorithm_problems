# 2024-03-05 (03-06)
import sys
from collections import deque

dq = deque()
N = int(sys.stdin.readline())
for n in range(N) :
    op = sys.stdin.readline().rstrip()
    if op[0] == '1' :
        a, b = op.split()
        dq.appendleft(b)
    elif op[0] == '2' :
        a, b = op.split()
        dq.append(b)
    elif op[0] == '3' :
        try :
            sys.stdout.write(dq.popleft())
        except :
            sys.stdout.write('-1')
        sys.stdout.write('\n')
    elif op[0] == '4' :
        try :
            sys.stdout.write(dq.pop())
        except :
            sys.stdout.write('-1')
        sys.stdout.write('\n')
    elif op[0] == '5' :
        sys.stdout.write(''.join([str(len(dq)), '\n']))
    elif op[0] == '6' :
        if dq : sys.stdout.write('0\n')
        else : sys.stdout.write('1\n')
    elif op[0] == '7' :
        try :
            sys.stdout.write(dq[0])
        except :
            sys.stdout.write('-1')
        sys.stdout.write('\n')
    elif op[0] == '8' :
        try :
            sys.stdout.write(dq[-1])
        except :
            sys.stdout.write('-1')
        sys.stdout.write('\n')
    else :
        pass