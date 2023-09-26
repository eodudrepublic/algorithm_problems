# 2023-09-26
import sys

arr = ['a', 'e', 'i', 'o', 'u']

while True : 
    tc = sys.stdin.readline().rstrip().lower()
    if tc == '#' : break
    total = 0
    for _ in arr : total += tc.count(_)
    print(total) 