# 2023-12-13 (12-14)
N = int(input())
f = int(input())
N = N - (N % 100)
while True :
    if N % f == 0 : break
    N += 1
print(format(N % 100, '02'))