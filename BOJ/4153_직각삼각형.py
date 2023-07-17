# 2023-05-28 (05-29)
import sys

while True :
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0 :
        break
    arr = [a, b, c]
    arr.sort()
    
    if arr[2]**2 == arr[0]**2 + arr[1]**2 :
        sys.stdout.write('right\n')
    else : sys.stdout.write('wrong\n')