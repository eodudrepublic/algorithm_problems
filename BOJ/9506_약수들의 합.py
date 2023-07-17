# 2023-07-16
import sys

arr = [(2**(_-1))*((2**_)-1) for _ in (2, 3, 5, 7, 13, 17)]
while True : 
    n = int(sys.stdin.readline())
    if n == -1 : break
    if n in arr : 
        sys.stdout.write(''.join([str(n), ' = ']))
        tmp = []
        for _ in range(1, n) : 
            if n%_ == 0 : tmp.append(str(_))
        sys.stdout.write(' + '.join(tmp))
        sys.stdout.write('\n')
    else : sys.stdout.write(''.join([str(n), ' is NOT perfect.\n']))