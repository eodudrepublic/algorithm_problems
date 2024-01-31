# 2024-01-31
import sys

while True :
    try :
        s, t = sys.stdin.readline().split()
        arr = list(s)
        for _ in t :
            if _ == arr[0] :
                arr.pop(0)
                if not arr : break
        if not arr : sys.stdout.write('Yes\n')
        else : sys.stdout.write('No\n')
        
    except :
        break