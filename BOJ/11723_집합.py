# 2023-04-14
import sys
allLi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
S = set()

M = int(sys.stdin.readline())

for m in range(M) :
    op = sys.stdin.readline().strip()
    
    try :
        opcode, x = op.split()
        n = int(x)
    except ValueError :
        opcode = op
        
    if opcode == 'add' :
        S.add(n)
    elif opcode == 'remove' :
        try :
            S.remove(n)
        except KeyError :
            pass
    elif opcode == 'check' :
        if n in S :
            sys.stdout.write("1\n")
        else :
            sys.stdout.write("0\n")
    elif opcode == 'toggle' :
        try :
            S.remove(n)
        except KeyError :
            S.add(n)
    elif opcode == 'all' :
        S = set(allLi)
    elif opcode == 'empty' :
        S.clear()
    else :
        sys.stdout.write("잘못된 입력입니다.\n")