# 2023-05-27 (05-28)
import sys
from collections import deque

N = int(sys.stdin.readline())
if N == 1 :
    print(N)
    sys.exit()
    
deck = deque(range(1, N+1))
while True :
    pop = deck.popleft()
    card = deck.popleft()
    if not deck : 
        print(card)
        break
    deck.append(card)