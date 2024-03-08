# 2024-03-08 (03-09)
import sys

lines = sys.stdin.readlines()
for line in lines :
    for _ in line :
        if _ == 'e' : sys.stdout.write('i')
        elif _ == 'i' : sys.stdout.write('e')
        elif _ == 'E' : sys.stdout.write('I')
        elif _ == 'I' : sys.stdout.write('E')
        else : sys.stdout.write(_)