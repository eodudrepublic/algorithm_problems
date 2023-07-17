import sys

num_testcase = int(sys.stdin.readline())
for i in range(num_testcase) :
    num_note1 = int(sys.stdin.readline())
    note1 = set(map(int, sys.stdin.readline().split()))
    num_note2 = int(sys.stdin.readline())
    note2 = list(map(int, sys.stdin.readline().split()))
    for i in note2 :
        if i in note1 :
            print(1)
        else :
            print(0)