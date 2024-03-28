# 2024-03-28
import sys

N = int(sys.stdin.readline())
start, end = sys.stdin.readline().rstrip().split('*')
start_len = len(start)
end_len = len(end)
for n in range(N) :
    ans = True 
    temp = sys.stdin.readline().rstrip()

    if start_len + end_len > len(temp) :
        ans = False
    elif temp[:start_len] != start :
        ans = False
    elif temp[len(temp) - end_len:] != end :
        ans = False
    else :
        pass
    
    if ans : 
        sys.stdout.write('DA\n')
    else :
        sys.stdout.write('NE\n')