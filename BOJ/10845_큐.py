# 2023-04-17
import sys
from collections import deque

N = int(sys.stdin.readline())

myQ = deque()
for n in range(N) :
    op = sys.stdin.readline().strip()
    if op == 'pop' :
        try :
            sys.stdout.write(str(myQ.popleft()))
            sys.stdout.write('\n')
        except IndexError :
            sys.stdout.write("-1\n")
    elif op == 'size' :
        sys.stdout.write(str(len(myQ)))
        sys.stdout.write('\n')
    elif op == 'empty' :
        if len(myQ) == 0 :
            sys.stdout.write("1\n")
        else :
            sys.stdout.write("0\n")
    elif op == 'front' :
        try :
            sys.stdout.write(str(myQ[0]))
            sys.stdout.write('\n')
        except IndexError :
            sys.stdout.write("-1\n")
    elif op == 'back' :
        try :
            sys.stdout.write(str(myQ[-1]))
            sys.stdout.write('\n')
        except IndexError :
            sys.stdout.write("-1\n")
    else :
        n = int(op[5:])
        myQ.append(n)