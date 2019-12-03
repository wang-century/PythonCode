import os
import time

input_time = input('请输入关机时间，格式如：小时:分钟 ：')

if input_time == 'off':
    os.system('shutdown -a')

h1 = int(input_time[0:2])
m1 = int(input_time[3:5])

print(h1, m1)
mytime = time.strftime('%H:%M:%S')
h2 = int(mytime[0:2])
m2 = int(mytime[3:5])

if h1 > 24:
    h1 = 24
    m2 = 0
if m1 > 60:
    m1 = 60
if h1 < h2:
    h1 = h1 + 24

s1 = (h1 + (m1 / 60.0) - h2 - (m2 / 60.0)) * 3600
if s1 <= 0:
    print("ERROR")
else:
    print('距离关机还有 %d 秒' % s1)
    os.system('shutdown -s -t %d' % s1)
