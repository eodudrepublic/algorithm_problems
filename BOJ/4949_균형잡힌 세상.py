# 2024-03-12
import sys
from collections import deque

while True :
    line = sys.stdin.readline()
    if line == '.\n' : break
    ans = True
    dq = deque()
    for _ in line :
        if _ == '(' or _ == '[' :
            dq.append(_)
        elif _ == ')' :
            try :
                temp = dq.pop()
                if temp != '(' :
                    ans = False
                    break
            except :
                ans = False
                break
        elif _ == ']' :
            try :
                temp = dq.pop()
                if temp != '[' :
                    ans = False
                    break
            except :
                ans = False
                break
        else :
            pass
    if not ans or dq :
        sys.stdout.write('no\n')
        
    else :
        sys.stdout.write('yes\n')