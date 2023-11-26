# 2023-11-26 (11-27)
N = int(input())
while True :
    if N == 1 : 
        print(1)
        break
    if N % 2 != 0 :
        print(0)
        break
    else : N /= 2