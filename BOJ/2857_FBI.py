# 2023-09-07
import sys

arr = []
for _ in range(5) : arr.append(sys.stdin.readline().rstrip())
ans = []
for _ in range(5) :
    if 'FBI' in arr[_] : 
        ans.append(_ + 1)

if not ans: sys.stdout.write('HE GOT AWAY!\n')
else : print(*ans)