# 2023-12-03
import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s = sys.stdin.readline().rstrip()
for _ in alphabet : sys.stdout.write(''.join([str(s.find(_)), ' ']))
sys.stdout.write('\n')