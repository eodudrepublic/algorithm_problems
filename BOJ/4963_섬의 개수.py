# 2023-03-28
import sys
from collections import deque

dx = (-1, 0, 1, -1, 1, -1, 0, 1)
dy = (-1, -1, -1, 0, 0, 1, 1, 1)

def create_map(w, h) :
    cm = []
    for i in range(0, h) :
        line = list(map(int, sys.stdin.readline().split()))
        cm.append(line)
    return cm

while True :
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0 :
        break
    else :
        tc = create_map(w, h)
        visited = [[0 for col in range(w)] for row in range(h)]
        # print(tc)
        # print(visited)
        
        island_num = 0
        for y in range(0, h) :
            for x in range(0, w) :
                if visited[y][x] == 1 :
                    continue
                else :
                    visited[y][x] = 1
                    if tc[y][x] == 0 :
                        continue
                    else :
                        island_num += 1
                        queue = deque()
                        queue.append([y, x])
                        while queue :
                            temp = queue.popleft()
                            # print(temp, temp[0], temp[1])
                            for i in range(8) :
                                if temp[0]+dy[i] >= 0 and temp[1]+dx[i] >= 0 and temp[0]+dy[i] < h and temp[1]+dx[i] < w :
                                    if visited[temp[0]+dy[i]][temp[1]+dx[i]] == 0 :
                                        visited[temp[0]+dy[i]][temp[1]+dx[i]] = 1
                                        if tc[temp[0]+dy[i]][temp[1]+dx[i]] == 0 :
                                            continue
                                        else :
                                            queue.append([temp[0]+dy[i], temp[1]+dx[i]])
        print(island_num)