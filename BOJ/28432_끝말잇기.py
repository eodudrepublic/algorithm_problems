# 2024-02-22
import sys

N = int(sys.stdin.readline())
arr = []
index = 0
for n in range(N) :
    temp = sys.stdin.readline().rstrip()
    if temp == '?' : index = n
    arr.append(temp)

M = int(sys.stdin.readline())
ans = ''
for m in range(M) :
    temp = sys.stdin.readline().rstrip()
    if (index != 0 and arr[index-1][-1] == temp[0] or index == 0) and (index != N-1 and arr[index+1][0] == temp[-1] or index == N-1) :
        if temp not in arr : ans = temp
sys.stdout.write(''.join([ans, '\n']))
