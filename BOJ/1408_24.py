# 2023-08-25 (copy)
current_time = list(map(int, input().split(':')))
start_time = list(map(int, input().split(':')))

current_sec = current_time[0]*3600 + current_time[1]*60 + current_time[2]
start_sec = start_time[0]*3600 + start_time[1]*60 + start_time[2]
res = start_sec - current_sec

if res < 0: res += 24*3600

print(f"{res//3600:02d}:{(res%3600)//60:02d}:{res%60:02d}")