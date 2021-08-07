# PythonCode
Python代码.
<pre>
- tools_source     工具包源代码
    - baiduocr_gui.py           使用tkinter+百度ocr实现简单文字识别程序
    - baidu_ocr_app             使用pyqt5+百度ocr实现简单文字识别程序
    - excel_key_search          批量搜索excel中的关键字(运行excel_tool.py文件)
    - notebook_gui.py           使用tkinter实现简单记事本程序
    - recognize_idcard.py       使用百度识别api实现识别身份证并保存到excel
    - field_survey_photography  使用pyqt5实现对手机“外业调查拍照”app入户调查所拍照片以编号为目录名进行分类保存功能

- spider_code   爬虫代码
    - meizituSpider.py          爬虫爬取妹子图（2020年2月27日测试可用）
    - pixivSpider.py            输入作者id爬取该作者所有pixiv插画（chromedriver.exe为此爬虫所需文件）   # 注：不可用（pixiv新添加人机验证未实现）
    - doubanBookTop250Spider.py 爬取豆瓣图书Top250并保存到json文件
    - QCWYBigDataSpider.py      爬取前程无忧大数据职位信息并保存到csv文件
    - ZhiLianBigDataSpider.py   抓取智联招聘大数据岗位信息  注：不可用（已过时）
    
- advanced_demo    python进阶练习
    - multiprocessing_demo      多进程包multiprocessing的使用
        - demo1.py              创建带参和不带参子进程
        - demo2.py              join()的使用方法
        - demo3.py              进程的属性
        - demo4.py              使用继承方式创建进程
        - demo5.py              进程池的使用(非阻塞)
        - demo6.py              进程池的使用(阻塞)
        - demo7.py              多个进程之间数据不共享案例
        - demo8.py              进程之间通过Queue队列实现通信
        - demo9.py              进程池内进程之间通信
        - demo10.py             Queue队列的常用方法

    - threading_demo            多线程包threading的使用
        - demo1.py              互斥锁的使用

- Script_code   脚本包
    - adb_script                安卓adb自动脚本
        - adb_demo.py           运行此文件
    - Centos7InstallPython3.py  centos7安装python3脚本
    - InstallSSR.py             安装ssr
    - SendEmail.py              发送邮件
    - ShutdownMachine.py        定时关机
    - UsePyMysql.py             使用pymysql
    
- practice_code
    - mathematical_thinking.py  数学思维修炼练习代码
    - practice_leetcode.py      leetcode习题代码

- tank_game    坦克大战（pygame开发,未完成）
    
</pre>