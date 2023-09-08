# 2023-09-08 (09-09)
import sys
from datetime import datetime

weekday_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
D, M = map(int, sys.stdin.readline().split())
sys.stdout.write(''.join([weekday_list[datetime(year=2009, month=M, day=D).weekday()], '\n']))