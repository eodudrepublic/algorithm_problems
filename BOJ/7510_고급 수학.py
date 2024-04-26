# 2024-04-26 (04-27)
N = int(input())
for n in range(N) :
    arr = sorted(list(map(int, input().split())))
    print(f"Scenario #{n+1}:")
    if arr[0]**2 + arr[1]**2 == arr[2]**2 :
        print("yes\n")
    else : 
        print("no\n")