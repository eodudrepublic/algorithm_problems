# 2023-04-07
import sys

def change(sx, sy, board) :
    c = 0
    start = board[sy][sx]
    if start == 'B' :
        rest = 'W'
    else :
        rest = 'B'
    for y in range(sy, sy+8, 2) :
        for x in range(sx, sx+8, 2) :
            if board[y][x] != start :
                c += 1
            if board[y+1][x+1] != start :
                c += 1
    for y in range(sy, sy+8, 2) :
        for x in range(sx+1, sx+8, 2) :
            if board[y][x] != rest :
                c += 1
            if board[y+1][x-1] != rest :
                c += 1
    if c > 32 :
        return 64 - c
    else :
        return c

Y, X = map(int, sys.stdin.readline().split())

board = []
for y in range(Y) :
    line = list(sys.stdin.readline().strip())
    board.append(line)

change_num = 32
for y in range(Y-7) :
    for x in range(X-7) :
        c = change(x, y, board)
        if c < change_num :
            change_num = c

print(change_num)