# 2023-07-25
import sys

T = int(sys.stdin.readline())

if T%10 != 0 : 
    sys.stdout.write('-1\n')
    sys.exit(0)

a = 0
while True :
    if T - 300 >= 0 : 
        T -= 300
        a += 1
    else : break
sys.stdout.write(''.join([str(a), ' ']))

b = 0
while True :
    if T - 60 >= 0 : 
        T -= 60
        b += 1
    else : break
sys.stdout.write(''.join([str(b), ' ']))

c = 0
while True :
    if T - 10 >= 0 : 
        T -= 10
        c += 1
    else : break
sys.stdout.write(''.join([str(c), '\n']))