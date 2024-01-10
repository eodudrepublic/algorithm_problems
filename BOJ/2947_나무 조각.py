# 2024-01-10
import sys

def print(arr) :
    sys.stdout.write(' '.join(str(_) for _ in arr))
    sys.stdout.write('\n')

ans = [1, 2, 3, 4, 5]
arr = list(map(int, sys.stdin.readline().split()))
while True :
    if arr[0] > arr[1] : 
        arr[0], arr[1] = arr[1], arr[0]
        print(arr)
    if arr[1] > arr[2] : 
        arr[1], arr[2] = arr[2], arr[1]
        print(arr)
    if arr[2] > arr[3] : 
        arr[2], arr[3] = arr[3], arr[2]
        print(arr)
    if arr[3] > arr[4] : 
        arr[3], arr[4] = arr[4], arr[3]
        print(arr)
    if arr == ans : break