# 2023-03-29
import sys
from collections import deque

# 1차 
def points(p1, p2) :
    x_v = p1[0] - p2[0]
    y_v = p1[1] - p2[1]
    if x_v == 0 and (y_v == 1 or y_v == -1) :
        return True
    elif y_v == 0 and (x_v == 1 or x_v == -1) :
        return True
    else :
        return False

# 2차 & 3차
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
    
T = int(sys.stdin.readline())
for t in range(T) :
    bugs = 0
    w, h, K = map(int, sys.stdin.readline().split())
    
    # 3차 : 실행 시간 88ms
    field = [[0 for col in range(w)] for row in range(h)]
    visited = [[0 for col in range(w)] for row in range(h)]
    
    for k in range(K) :
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = 1
    for y in range(0, h) :
        for x in range(0, w) :
            if visited[y][x] == 1 :
                continue
            visited[y][x] = 1
            if field[y][x] == 0 :
                continue
            bugs += 1
            queue = deque()
            queue.append([y, x])
            while queue :
                temp = queue.popleft()
                for i in range(4) :
                    if temp[0]+dy[i] >= 0 and temp[1]+dx[i] >= 0 and temp[0]+dy[i] < h and temp[1]+dx[i] < w :
                        if visited[temp[0]+dy[i]][temp[1]+dx[i]] == 0 :
                            visited[temp[0]+dy[i]][temp[1]+dx[i]] = 1
                            if field[temp[0]+dy[i]][temp[1]+dx[i]] == 0 :
                                continue
                            queue.append([temp[0]+dy[i], temp[1]+dx[i]])

    # # 2차 : 실행 시간 456ms
    # nodes = []
    # for k in range(K) :
    #     x, y = map(int, sys.stdin.readline().split())
    #     nodes.append([x, y])
    
    # while nodes :
    #     visited = deque()
    #     visited.append(nodes.pop(0))
    #     bugs += 1
        
    #     while visited :
    #         v = visited.popleft()
    #         for i in range(0, 4) :
    #             if [v[0]+dx[i], v[1]+dy[i]] in nodes :
    #                 visited.append([v[0]+dx[i], v[1]+dy[i]])
    #                 nodes.remove([v[0]+dx[i], v[1]+dy[i]])
                    
    # # # 1차 : 실행 시간 944ms
    # # while nodes :
    # #     visited = deque()
    # #     visited.append(nodes.pop(0))
    # #     bugs += 1
        
    # #     while visited :
    # #         v = visited.popleft()
    # #         rm_list = []
    # #         for node in nodes :
    # #             if points(v, node) :
    # #                 visited.append(node)
    # #                 rm_list.append(node)
    # #         for i in rm_list :
    # #             nodes.remove(i)
    print(bugs)