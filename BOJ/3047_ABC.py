# 2023-11-19 (11-20)
import sys

arr = sorted(map(int, sys.stdin.readline().split()))
l = sys.stdin.readline().rstrip()
for _ in l :
    if _ == 'A' : sys.stdout.write(''.join([str(arr[0]), ' ']))
    elif _ == 'B' : sys.stdout.write(''.join([str(arr[1]), ' ']))
    else : sys.stdout.write(''.join([str(arr[2]), ' ']))
sys.stdout.write('\n')