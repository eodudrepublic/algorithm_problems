import sys
k = 0

def hanoi(now, remain, dest, n) :
    if n < 2 :
        global k
        k += 1
        if k == K :
            print(now, dest)
            sys.exit()
    else :
        hanoi(now, dest, remain, n-1)
        hanoi(now, remain, dest, 1)
        hanoi(remain, now, dest, n-1)

N, K = map(int, sys.stdin.readline().split())

if K == 2**N - 1 :
    if N%2 == 1 :
        print(1, 3)
    else :
        print(2, 3)
    sys.exit()


for n in range(1, N) :
    if n%2 == 1 :
        if K > 2**(N-n) :
            K -= 2**(N-n)
        elif K == 2**(N-n) :
            print(1, 3)
        else :
            hanoi(1, 3, 2, N-n)
    else :
        if K > 2**(N-n) :
            K -= 2**(N-n)
        elif K == 2**(N-n) :
            print(2, 3)
        else :
            hanoi(2, 3, 1, N-n)