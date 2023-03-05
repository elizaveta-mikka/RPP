import datetime

s = int(input()) # без использования модуля datetime
k_mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sec = s % 60
s -= sec
mn = s % 3600 // 60
s -= mn
h = s % 86400 // 3600
s -= h
day = s // 86400 + 1
yr = 1970
while day > 365:
    if yr % 4 != 0 or (yr % 100 == 0 and yr % 400 != 0):
        day -= 365
    else:
        day -= 366
    yr += 1
mon = 1
for i in k_mon:
    if day > i:
        if i < 30:
            if not(yr % 4 != 0 or (yr % 100 == 0 and yr % 400 != 0)):
                i += 1
        day -= i
        mon += 1
    else:
        break
print(f'{yr}-{mon:02}-{day:02} {h:02}:{mn:02}:{sec:02}')

s = int(input()) # с использованием модуля datetime
print(datetime.datetime.utcfromtimestamp(s))


