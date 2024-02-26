# 2024-02-26 (02-27)
import sys

def round(n, k) :
    if (n%k) / k >= 0.5 :
        return (n//k) + 1
    else : 
        return (n//k)

while True :
    N = int(sys.stdin.readline())
    if N == 0 :
        sys.stdout.write('0\n')
        break
    
    cut = round(N*3, 20)
    
    arr = []
    total = 0
    for n in range(N) :
        temp = int(sys.stdin.readline())
        arr.append(temp)
        total += temp
    arr.sort()
    
    for _ in range(cut) :
        total -= arr[_]
        total -= arr[-1-_]
        N -= 2
    
    sys.stdout.write(''.join([str(round(total, N)), '\n']))
    break