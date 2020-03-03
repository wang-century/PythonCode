""" adb安卓脚本
    详情请参考 https://blog.csdn.net/zhonglunshun/article/details/78362439
"""
import os
from time import sleep
from random import choice

def shuabao_wifi():
    '''刷宝视频脚本 使用无线连接'''
    device_name = '192.168.0.102:5555'
    os.system('adb connect {}'.format(device_name))
    os.system('adb -s {} shell input keyevent 224'.format(device_name))
    sleep_list = [i for i in range(6,7)] # 等待时间列表
    while True:
        print('上滑屏幕',end='\t')
        os.system('adb -s {} shell input swipe 320 882 320 140'.format( device_name))  # 上划屏幕操作(视频)
        #os.system('adb -s {} shell input swipe 882 320 140 320'.format(device_name))  # 左划屏幕操作(阅读小说)
        sleep_time = choice(sleep_list)
        print('等待{}秒'.format(sleep_time))
        sleep(sleep_time)
        # os.system('adb -s {} shell input tap 978 1606'.format(device_name))  # 点击评论
        # for i in range(5):
        #     os.system('adb -s {} shell input swipe 300 1000 300 10'.format(device_name))  # 上划
        #     sleep(10)
        # os.system('adb -s {} shell input keyevent 4'.format(device_name))  # 点击返回键

def shuabao_line():
    """使用usb连接"""
    os.system('adb shell input keyevent 224')
    sleep_list = [i for i in range(6, 7)]  # 等待时间列表
    while True:
        print('上滑屏幕', end='\t')
        os.system('adb shell input swipe 320 882 320 140')  # 上划屏幕操作(视频)
        sleep_time = choice(sleep_list)
        print('等待{}秒'.format(sleep_time))
        sleep(sleep_time)
        os.system('adb shell input keyevent 4')  # 点击返回键

if __name__ == '__main__':
    shuabao_wifi()
    # shuabao_line()
