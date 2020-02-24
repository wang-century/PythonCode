import os
from time import sleep
from random import choice

def shuabao_app():
    '''刷宝视频脚本'''
    device_name = '192.168.0.103:5555'###'emulator-5556'
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
        os.system('adb -s {} shell input keyevent 4'.format(device_name))  # 点击返回键

def shuabao_app1():
    '''刷宝视频脚本'''
    #device_name = '192.168.0.100:5555'###'emulator-5556'
    #os.system('adb connect {}'.format( device_name))
    #os.system('adb -s {} shell input keyevent 224'.format(device_name))
    os.system('adb shell input keyevent 224')
    sleep_list = [i for i in range(6,12,2)] # 等待时间列表
    while True:
        print('上滑屏幕',end='\t')
        #os.system('adb -s {} shell input swipe 320 882 320 140'.format( device_name))  # 上划屏幕操作
        os.system('adb shell input swipe 320 882 320 140')
        sleep_time = choice(sleep_list)
        print('等待{}秒'.format(sleep_time))
        sleep(sleep_time)
        # os.system('adb -s {} shell input tap 978 1606'.format(device_name))  # 点击评论
        # for i in range(5):
        #     os.system('adb -s {} shell input swipe 300 1000 300 10'.format(device_name))  # 上划
        #     sleep(10)
        #os.system('adb -s {} shell input keyevent 4'.format(device_name))  # 点击返回键
        os.system('adb shell input keyevent 4')
# os.system('adb shell screencap -p /sdcard/sc.png') # 屏幕截图
# os.system('adb pull /sdcard/sc.png')    # 导出到电脑
# while True:
#     os.system('adb shell input swipe 300 1000 300 10')  # 上划屏幕操作
#
#     os.system('adb shell input tap 978 1606')   # 点击评论
#     for i in range(6):
#         os.system('adb shell input swipe 300 1000 300 10')  # 上划
#         sleep(2)
#     os.system('adb shell input keyevent 4') # 点击返回键
#     # sleep_time = choice(list(range(10, 40)))  # 在等待时间列表随机选择时间
#     # sleep(sleep_time)  # 休眠随机的时间


def upgrade_farm():
    '''升级农场'''
    base_str = 'adb shell input tap {} {}'
    # os.system('adb shell input tap 88 519')
    os.system(base_str.format(503, 1449))    # 点击第一个
    sleep(1)
    os.system(base_str.format(503, 1449))    # 收获第一个
    os.system(base_str.format(711, 1338))   # 点击第二个
    os.system(base_str.format(925, 1220))   # 第三个
    os.system(base_str.format(336, 1251))   # 四
    os.system(base_str.format(549, 1151))   # 五
    os.system(base_str.format(781, 1043))   # 六

    for i in range(3):
        os.system(base_str.format(100, 522))    # 点击升级
        os.system(base_str.format(538, 1327))    # 立即改造
        sleep(20)   # 等待广告结束
        os.system(base_str.format(915, 119))    # 关闭广告
    os.system(base_str.format(100, 522))  # 点击升级
    os.system(base_str.format(538, 1327))  # 立即改造
    os.system(base_str.format(353, 1304))  # 确认
    sleep(4)
    os.system(base_str.format(526, 1274))   # 获得奖杯
    # os.system('adb shell screencap -p /sdcard/sc.png')  # 屏幕截图
    # os.system('adb pull /sdcard/sc.png')  # 导出到电脑


if __name__ == '__main__':
    # for i in range(5):
    #     upgrade_farm()
    shuabao_app()
