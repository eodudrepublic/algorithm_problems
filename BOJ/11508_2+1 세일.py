# 2024-03-20
import sys

N = int(sys.stdin.readline())
arr = sorted(list(int(sys.stdin.readline()) for n in range(N)), reverse=True)
ans = 0
for n in range(N) :
    if n % 3 == 2 :
        pass
    else :
        ans += arr[n]
sys.stdout.write(''.join([str(ans), '\n']))