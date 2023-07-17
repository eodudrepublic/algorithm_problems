# 2023-04-04
import sys

N, M = map(int, sys.stdin.readline().split())

name_num = {}
num_name = {}
for n in range(N) :
    name = sys.stdin.readline().strip()
    name_num[name] = n+1
    num_name[n+1] = name

for m in range(M) :
    m = sys.stdin.readline().strip()
    
    try :
        int(m)
        print(num_name[int(m)])
    except ValueError :
        print(name_num[m])