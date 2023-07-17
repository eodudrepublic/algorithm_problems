# 소요시간 : 1시간 반
# 어려웠던 점 : break는 반복문을 벗어나는 거란걸 항상 기억합시다...

import math
import sys

def int_square(n) :
    if int(math.sqrt(n)) == math.sqrt(n) :
        return True
    else :
        return False

while True :
    try_num = 4
    target_num = int(sys.stdin.readline())
    if int_square(target_num) :
        print(1)
        break
    for i in range(int(math.sqrt(target_num)) + 1) :
        temp1 = target_num - (i**2)
        if int_square(temp1) :
            try_num = 2
            break
        if try_num == 4 :
            for j in range(int(math.sqrt(temp1)) + 1) :
                temp2 = temp1 - (j**2)
                if int_square(temp2) :
                    try_num = 3
    print(try_num)
    break
            