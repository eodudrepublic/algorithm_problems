# 2023-04-17
import sys
from collections import deque

N = int(sys.stdin.readline())

myDQ = deque()
for n in range(N) :
    op = sys.stdin.readline().strip()
    try :
        op, sn = op.split()
        n = int(sn)
    except :
        pass
    
    try :
        op, dirc = op.split('_')
    except :
        pass
    
    if op == 'push' :
        if dirc == 'back' :
            myDQ.append(n)
        else :
            myDQ.appendleft(n)
            
    elif op == 'pop' :
        try :
            if dirc == 'back' :
                sys.stdout.write(str(myDQ.pop()))
                sys.stdout.write('\n')
            else :
                sys.stdout.write(str(myDQ.popleft()))
                sys.stdout.write('\n')
        except :
            sys.stdout.write("-1\n")
            
    elif op == 'size' :
        sys.stdout.write(str(len(myDQ)))
        sys.stdout.write('\n')
        
    elif op == 'empty' :
        if len(myDQ) == 0 :
            sys.stdout.write("1\n")
        else :
            sys.stdout.write("0\n")
            
    elif op == 'front' :
        try :
            sys.stdout.write(str(myDQ[0]))
            sys.stdout.write('\n')
        except :
            sys.stdout.write("-1\n")
            
    elif op == 'back' :
        try :
            sys.stdout.write(str(myDQ[-1]))
            sys.stdout.write('\n')
        except :
            sys.stdout.write("-1\n")
    else :
        pass