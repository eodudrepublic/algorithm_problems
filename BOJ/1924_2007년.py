import sys

month_day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

month, day = map(int, sys.stdin.readline().split())
total_day = day
for i in range(month) :
    if i == 0 :
        pass
    else :
        total_day += month_day[i]
day = total_day % 7

if day == 0 :
    print('SUN')
elif day == 1 :
    print('MON')
elif day == 2 :
    print('TUE')
elif day == 3 :
    print('WED')
elif day == 4 :
    print('THU')
elif day == 5 :
    print('FRI')
else :
    print('SAT')