# 2023-11-23
N = int(input())

clap = 0
for n in range(1, N+1) :
    arr = str(n)
    if '3' in arr: 
        clap += arr.count('3')
    if '6' in arr: 
        clap += arr.count('6')
    if '9' in arr: 
        clap += arr.count('9')
print(clap)