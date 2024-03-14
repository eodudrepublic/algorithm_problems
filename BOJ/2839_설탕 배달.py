# 2024-03-14 (03-15)
import sys

N = int(sys.stdin.readline())
K = N // 5
ans = 2000
for k in range(K, -1, -1) :
    if (N - (5 * k)) % 3 == 0 :
        ans = k + (N - (5 * k))//3
        break
if ans == 2000 :
    sys.stdout.write('-1\n')
else :
    sys.stdout.write(''.join([str(ans), '\n']))