# 2023-06-27 (06-28)
import sys

input = sys.stdin.readline
print = sys.stdout.write

while True :
    try :
        A, B = map(int, input().split())
        print(''.join([str(A+B), '\n']))
    except :
        break