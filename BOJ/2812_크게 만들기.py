import sys

n, k = map(int, sys.stdin.readline().split())
num = list(sys.stdin.readline().rstrip())

t = 0
part = num[0:k+1]
while k != 0 :
    # print(part)
    if part[0] != max(part) :
        i = part.index(max(part))
        del part[0:i]
        del num[t:t+i]
        k -= i
    else : 
        t += 1
        if n == t+k : 
            del num[t:]
            break
        part.append(num[t+k])
        del part[0]

for _ in num : sys.stdout.write(_)
sys.stdout.write('\n')