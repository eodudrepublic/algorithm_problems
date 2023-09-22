# 2023-09-22
import sys

arr = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

word = sys.stdin.readline().rstrip()
for _ in arr :
    sys.stdout.write(str(word.count(_)))
    sys.stdout.write(' ')
sys.stdout.write('\n')