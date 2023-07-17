# 2023-04-13 (04-14)
# 리스트 복사할때 temp = pn 식의 복사는 pointer의 복사와 같이 같은 주소값을 2개의 이름으로 부르는 식의 copy가 일어난다
# 꼭 읽어볼것 : https://black-hair.tistory.com/49 
import sys

D = 1234567
TD = {
    0: [7], 
    1: [2, 4], 
    2: [1, 3, 5], 
    3: [2, 6], 
    4: [1, 5, 7], 
    5: [2, 4, 6, 8], 
    6: [3, 5, 9], 
    7: [4, 8, 0], 
    8: [5, 7, 9], 
    9: [6, 8]
}

def expand(pn) :
    temp = [0]*10
    for k in range(10) :
        for v in TD[k] :
            temp[k] += pn[v]
    return temp
            
T = int(sys.stdin.readline())

for t in range(T) :
    pn = [1]*10
    N = int(sys.stdin.readline())
    
    for n in range(1, N) :
        pn = expand(pn)
    
    print(sum(pn)%D)