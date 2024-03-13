# 2024-03-13 (3-14)
import sys

line = sys.stdin.readline().rstrip()

n = int(sys.stdin.readline())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]

# shift = {}
# for _ in range(ord('a'), ord('z')) :
#     shift[chr(_)] = chr(_ + 1)
# shift['z'] = 'a'

shift = {
    'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 
    'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 
    'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 
    'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 
    'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'
}

ans = True
while ans :
    temp = ''.join([shift[_] for _ in line])
    for _ in arr :
        if _ in temp :
            ans = False
            break
    line = temp
sys.stdout.write(''.join([line, '\n']))