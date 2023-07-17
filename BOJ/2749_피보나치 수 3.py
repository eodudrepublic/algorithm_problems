# 2023-04-27

# 피사노 주기 : 피보나치 수를 어떤 수 M으로 나눌 때, 나머지는 항상 주기를 갖는다.
# 주기는 제수(divisor) M = 10**k (k>2) -> 주기 P = 15*10**(k-1)
# M = 1000000 = 10**6 -> P = 15*10**5 = 1500000

import sys

M = 1000000
P = 1500000

N = int(sys.stdin.readline())
n = N % P

fibo = [0]*(n+1)
fibo[1] = 1
for i in range(2, n+1) :
    fibo[i] = (fibo[i-1] + fibo[i-2])%M

sys.stdout.write(str(fibo[n]))
sys.stdout.write('\n')