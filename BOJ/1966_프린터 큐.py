import sys
from collections import deque

T = int(sys.stdin.readline())
for t in range(T) :
    N, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    docs = deque([(n, arr[n]) for n in range(N)])
    importances = deque(sorted(arr, reverse=True))
    ans = 1
    while importances :
        i = importances.popleft()
        while True :
            doc = docs.popleft()
            if doc[1] == i :
                break
            else :
                docs.append(doc)
        if doc[0] == m :
            print(ans)
            # sys.stdout.write(''.join([str(ans), '\n'])) -> 이거보다 왜 print가 더 빠르냐;;;
            break
        else :
            ans += 1
