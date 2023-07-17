# 2023-05-08 (05-09)
import sys

board = list(sys.stdin.readline().strip())

ps = '.'
l = len(board)
for i in range(l) :
    if board[i] != 'X' :
        continue
    if i < l-3 and board[i+1] == 'X' and board[i+2] == 'X' and board[i+3] == 'X' :
        for j in range(4) :
            board[i+j] = 'A'
        continue
    if i < l-1 and board[i+1] == 'X' :
        for j in range(2) :
            board[i+j] = 'B'
    else :
        print(-1)
        sys.exit()

for i in board :
    sys.stdout.write(i)
sys.stdout.write('\n')