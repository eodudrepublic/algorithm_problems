# 2024-03-04 (03-05)
import sys

a, b = sys.stdin.readline().rstrip().split()
len_a = len(a)
len_b = len(b)

ans = len_a
for _ in range(len_b - len_a + 1) :
    temp = b[_:_+len_a]
    diff = 0
    for i in range(len_a) :
        if a[i] != temp[i] : 
            diff += 1
            if diff >= ans : break
    if diff < ans : ans = diff
sys.stdout.write(''.join([str(ans), '\n']))