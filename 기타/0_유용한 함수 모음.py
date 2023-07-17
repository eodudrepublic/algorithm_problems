import sys
from collections import deque
# ex3

# arr = [1, 2, 3]
# print(*arr) # -> 1 2 3

# ex0 : 빠른 입력
# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline

# input_str = sys.stdin.readline()
# input_num = int(sys.stdin.readline())
# # 정수들 입력받아 리스트로 저장
# input_num_list = list(map(int, sys.stdin.readline().split()))
# # input_num줄의 문자열을 입력받아 리스트에 저장
# input_lines = [sys.stdin.readline().strip() for i in range(input_num)]

# --------------------------------------------------------------------------------

# ex1 : 2차원 배열(리스트) slicing (list_2D)
# https://programming119.tistory.com/169

list_ex1 = [
    [1, 0, 0, 1], 
    [0, 0, 1, 0], 
    [1, 0, 0, 0], 
    [0, 1, 0, 1]
]
# print([row[0:2] for row in list_ex1[2:4]])

def print_pretty(list_2D) :
    for line in list_2D :
        for i in line :
            print(i, end = ' ')
        print()

def list_2D_slicing(li) :
    n = int(len(li)/2)
    for i in range(0, n*2, n) :
        for j in range(0, n*2, n) :
            print('------------')
            print_pretty([row[j:j+n] for row in li[i:i+n]])
    print('------------')

# list_2D_slicing(list_ex1)

# --------------------------------------------------------------------------------

# ex2 : Closure(중첩된 함수)를 사용한 피보나치
# https://ichi.pro/ko/deo-isang-paisseon-eseo-jaegwileul-sayonghaji-masibsio-160024803739980

def fib():
    a = 0
    b = 1
    def get_next_number():
        nonlocal a, b
        a, b = b, a + b
        return b
    return get_next_number

def fibonacci(n):
    if n == 0 :
        return 0
    # elif n == -1 :
    #     return 1
    elif n == 1 :
        return 1
    else :
        f = fib()
        for i in range(2, n+1):
            num = f()
        return num

# print(fibonacci(10))

# --------------------------------------------------------------------------------

# ex3 : BFS(너비 우선 탐색) 기본 틀
# https://gmlwjd9405.github.io/2018/08/15/algorithm-bfs.html

row = (-1, 0, 1, -1, 1, -1, 0, 1)
col = (-1, -1, -1, 0, 0, 1, 1, 1)
X = Y = 0
# 위 예시같은 경우 상하좌우 + 대각선까지 생각

def bfs(matrix, x, y) :
    queue = deque()
    queue.append((x, y))
    # 시작 노드를 큐에 삽입
    matrix[x][y] = 0 
    # 큐에 삽입한 코드를 0으로 방문 처리
    
    while queue :   # 큐가 빌때까지
        x, y = queue.popleft()
        
        for i in range(8) : # 상하좌우일 시에는 4, 대각선까지 생각하면 8
            nx = x + row[i]
            ny = y + col[i]
            
            if nx < 0 or nx >= X or ny < 0 or ny >= Y : # X, Y를 함수 입력으로 받아야 하는 경우도 생각
                continue
                
            if matrix[nx][ny] == 1 :
                queue.append((nx,ny))
                matrix[nx][ny] = 0

# X, Y, k = map(int, sys.stdin.readline().split())

# # ex) 1012_유기농 배추
# matrix = [[0] * Y for i in range(X)]
# # Y축이 가로축, X축이 세로축이 되지만, matrix[x][y]꼴로 (x, y)의 식으로 좌표를 생각할 수 있음
# # print(matrix)

# for i in range(k) :
#     x, y = map(int, sys.stdin.readline().split())
#     # 방문할 수 있는 노드의 좌표를 입력받아
#     matrix[x][y] = 1
#     # 2차 배열 좌표에 반영

# # # ex) 4963_섬의 개수
# # # 섬의 개수 같은 경우엔 matrix 전체의 경우로 입력을 받게됨
# # X, Y = Y, X
# # # X를 세로축, Y를 가로축으로 만들기 위해 -> bfs라는 함수 틀을 사용하기 위해서!
# # matrix = []
# # for i in range(X) :
# #     line = list(map(int, sys.stdin.readline().split()))
# #     matrix.append(line)

# --------------------------------------------------------------------------------