# 2023-05-22 (05-23)
import sys

while True :
    N = int(sys.stdin.readline())
    
    stair = [int(sys.stdin.readline()) for _ in range(N)]
    point = [0]*N
    if N == 1 :
        print(stair[0])
        break
    
    point[0] = stair[0]
    point[1] = stair[0] + stair[1]
    for n in range(2, N) :
        point[n] = max(point[n-3]+stair[n-1]+stair[n], point[n-2]+stair[n])
    # for n in range(2, N) :
    #     case1 = stair[n-1]
    #     if n > 3 :    # n이 3보다 같거나 클때(n>=3)로 했어야 했음 => 맞았음 (심지어 더 빠름)
    #         case1 += point[n-3]
    #     case2 = point[n-2]
    #     point[n] = stair[n] + max(case1, case2)
    # 이 코드는 왜 틀렸을까?
    print(point[-1])
    break