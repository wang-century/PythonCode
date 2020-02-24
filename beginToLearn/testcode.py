def test_logic_operation():
    '''逻辑运算
    逻辑运算符：
        or          x or y      x为true返回true，x为false返回y
        and         x and y     x为true返回y的值，x为false返回false
        not         not x       x为true返回false，x为false返回true
    '''
    a = True
    b = False
    print('a=True\tb=False')
    print('逻辑或:')
    print('\"a or 30\"={}'.format(a or 30))
    print('\"b or 30\"={}'.format(b or 30))
    print('逻辑与:')
    print('\"a and 30\"={}'.format(a and 30))
    print('\"b and 30\"={}'.format(b and 30))
    print('逻辑非:')
    print('\"not a\"={}'.format(not a))

def demo1():
    import turtle
    from math import sqrt
    '''定义多点坐标 绘出折线 并计算起始点和终点距离'''
    # 定义多点坐标
    x1,y1 = 100,100
    x2,y2 = 100,-100
    x3,y3 = -100,-100
    x4,y4 = -100,100
    # 绘制折线
    turtle.up()
    turtle.goto(x1,y1)
    turtle.down()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x4, y4)
    # 计算起始点和终点距离
    distance = sqrt((x1-x4)**2+(y1-y4)**2)
    turtle.write(distance)

def demo2():
    '''同一运算符is 同一运算符用于比较两个对象的存储单元，实际比较的是对象的地址
            is      is是判断两个标识符是不是引用同一个对象
            is not  is not是判断两个标识符是不是引用不同对象
        is与==的区别：
            is用于判断两个变量引用的对象是否为同一个，比较的是地址
            ==用于判断引用变量引用对象的值是否相等，默认调用对象的__eq__()方法
    '''
    a = 101132331
    b = 101132331
    '''注：
        整数缓存问题：
            Python仅仅对比较小的整数对象进行缓存，范围为[-5,256]，而非是所有整数对象。
            需要注意的是，这仅仅是在命令行中实行，而在Pycharm或者保存为文件执行，结果是不一样的，
            因为解释器做了优化，范围变为[-5,任意正整数]。
    '''
    print(a==b)
    print(a is b)
    print(id(a))
    print(id(b))


def demo3():
    ''' 字符串的编码
        使用内置函数ord()可以把字符转换成对应的Unicode码
        使用内置函数chr()可以把十进制数字转换成对应的字符
    '''
    print('字符串的编码:')
    print(ord('王'))
    print(chr(66))

    ''' 字符串的拼接
        1.可以使用+将多个字符串拼接  注：+两边类型需要相同
        2.可以将多个字符串直接放到一起实现拼接
    '''
    print('\n字符串的拼接:')
    print('你好' + '世界！')
    print('你好''世界！')

    ''' 字符串的复制
        可以使用*号
    '''
    print('\n字符串的复制:')
    print('你好' * 10)

    ''' 不换行打印
        通过参数end='任意字符串'实现末尾添加任何内容
    '''
    print('\n不换行打印:')
    print('你好', end='')
    print('世界!')

    ''' 从控制台读取字符串
        使用input()从控制台读取键盘输入的内容
    '''
    # print('\n从控制台读取字符串:')
    # username = input('请输入姓名:')
    # print('我的名字:'+username)

    ''' replace()实现字符串替换(注：该方法生成新字符串，并不改变原有字符串) '''
    a = 'abcdefgh'
    print(a)
    print(a.replace('c', '世'))

    ''' 字符串切片 
    str[开始:结束:步长]
        注：起始偏移量和终止偏移量不在[0,字符串长度-1]这个范围，也不会报错，如果起始偏移量小于0则默认0，终止偏移量大于长度-1默认为-1
    '''
    print('\n字符串切片:')
    a = 'abcdefgh'
    print('a=abcdefgh')
    print('a[1:5:2]={}'.format(a[1:5:2]))
    print('a[-3:]={}'.format(a[-3:]))
    print('a[::-1]={}'.format(a[::-1]))
    print('a[0:100]={}'.format(a[-3:100]))

    ''' split()字符串分割
        可以基于指定分隔符将字符串分隔成多个子字符串，默认以空白字符分割
    '''
    print('\n字符串分割:')
    a = "Hello world!"
    print(a.split())

    ''' join()字符串拼接
        与split()作用相反，用于将一系列子字符串

        注：
            使用过字符串拼接符“+”会生成新的字符串对象，因此不推荐使用+来拼接字符串，
            推荐使用join函数，因为join函数在拼接字符串之前会计算所有字符串的长度，然后逐一拷贝，仅新建一次对象
    '''
    print('\n字符串拼接:')
    a = ['你', '好', '啊']
    print(''.join(a))
    print('-'.join(a))
    ''' join函数与字符串连接符'+'效率测试 '''
    start_time = time.time()  # 起始时刻
    for i in range(10000):
        a += '你好'
    end_time = time.time()  # 终止时刻
    print('”+“运算符耗时:{}毫秒'.format(end_time - start_time))
    start_time = time.time()  # 起始时刻
    str_list = []
    for i in range(10000):
        str_list.append('你好')
    a = ''.join(str_list)
    end_time = time.time()  # 终止时刻
    print('join函数耗时:{}毫秒'.format(end_time - start_time))

    ''' 字符串驻留机制和字符串比较
    字符串驻留：仅保存一份相同且不可变字符串的方法，不同的值被存放在字符串驻留池中。
    Python支持字符串驻留机制，对于符合标识符规则的字符串(仅包含下划线、字母和数字)会启用字符串驻留机制。
    '''
    # 注意：在pycharm中运行结果与命令行不同  以命令行为准
    print('\n字符串驻留机制和字符串比较:')
    a = 'abc_11'
    b = 'abc_11'
    print(a is b)
    c = 'dd#'
    d = 'dd#'
    print(c is d)

    ''' 去除首尾信息
    	strip()去除字符串首尾指定信息。
    	lstrip()去除字符串左边指定信息。
    	rstrip()去除字符串右边指定信息。
    '''
    a = ' 你好啊 '
    print(a.strip())
    print(a.lstrip())
    print(a.rstrip())

    print("{:*^9}".format("245"))
    print("我是{0}，我喜欢数字{1:*^9}".format("小七", 520))
    print("我是{0}，我有{1:.2f}亿存款".format("王健林", 200.321))

    ''' 可变字符串 
    用于需要频繁修改的字符串
    '''
    import io

    s = 'hello,world'
    sio = io.StringIO(s)
    print(sio)
    print(sio.getvalue())
    sio.seek(7)
    sio.write('g')
    print(sio.getvalue())

    for i in range(5):
        for j in range(5):
            print(i, end='\t')
        print()
    # 打印9*9乘法表
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{:^2d}*{:^2d}={:^2d}".format(j, i, j * i), end='\t')
        print()

    r1 = {'name': '小二', 'age': 18, 'salary': 30000, 'city': '北京'}
    r2 = {'name': '小六', 'age': 19, 'salary': 40000, 'city': '上海'}
    r3 = {'name': '小七', 'age': 20, 'salary': 10000, 'city': '深圳'}
    grammer = [r1, r2, r3]
    for i in grammer:
        if i['salary'] > 15000:
            print(i)
    import time
    # 循环代码效率测试
    start_time = time.time()
    for i in range(1000):
        result = []
        for j in range(10000):
            result.append(i * 1000 + j * 100)
    end_time = time.time()

    start_time2 = time.time()
    result = []
    for i in range(1000):
        c = i * 1000
        for j in range(10000):
            result.append(c + j * 100)
    end_time2 = time.time()
    print('time1={}\ntime2={}'.format(end_time - start_time, end_time2 - start_time2))

def test_return_time_now():
    '''返回当前时刻'''
    import time
    date_now_msecs = int(time.time())
    date_now_minutes = date_now_msecs//60
    date_now_hours = date_now_minutes//60
    date_now_days = date_now_hours//24
    print("毫秒:{}".format(date_now_msecs))
    print("分钟:{}".format(date_now_minutes))
    print("小时:{}".format(date_now_hours))
    print("天数:{}".format(date_now_days))


def test_copy_deepcopy():
    '''测试浅拷贝和深拷贝'''
    import copy
    # 浅拷贝
    a = [10,20,[1,2]]
    print('---浅拷贝---')
    b = copy.copy(a)    # 浅拷贝  注：浅拷贝只拷贝个体，对于其引用不进行拷贝（例如：父->子->孙    拷贝只拷贝了"父"）
    print('拷贝结果：')
    print('a:',a)
    print('b:',b)
    # 对b进行操作
    print('对浅拷贝对象操作：')
    b.append(30)
    b[2].append(3)
    print('操作后结果：')
    print('a:', a)
    print('b:', b)

    # 深拷贝
    a = [10, 20, [1, 2]]
    print('\n---深拷贝---')
    b = copy.deepcopy(a)  # 浅拷贝  注：深拷贝拷贝所有
    print('拷贝结果：')
    print('a:', a)
    print('b:', b)
    # 对b进行操作
    print('对浅拷贝对象操作：')
    b.append(30)
    b[2].append(3)
    print('操作后结果：')
    print('a:', a)
    print('b:', b)

def calculating_factorial(n):
    '''计算n的阶乘（递归）'''
    if n == 1:
        return 1
    else:
        return n * calculating_factorial(n - 1)

def test_property():
    '''测试装饰器的使用'''
    class Employee:
        def __init__(self):
            self.__salary = 50000

        @property
        def salary(self):
            return self.__salary

        @salary.setter
        def salary(self,salary):
            if 1000<salary<50000:
                self.__salary = salary
            else:
                print('输入错误，请重新输入！')


    emp = Employee()
    print(emp.salary)
    emp.salary = -2000
    emp.salary = 2000
    print(emp.salary)

def test_except():
    '''测试错误捕获机制'''
    try:
        a = input('请输入被除数：')
        b = input('请输入除数：')
        c = float(a)/float(b)
    except BaseException as e:
        print(e)
    else:
        print("结果为{:.2f}".format(c))
    finally:
        print('程序结束！（finally语句，无论是否发生异常都会执行！）')

def test_traceback():
    '''测试traceback模块的使用   异常写入日志文件'''
    import traceback
    try:
        a = input('请输入被除数：')
        b = input('请输入除数：')
        c = float(a) / float(b)
    except:
        traceback.print_exc()   # 异常输出到控制台
        with open('error_log.txt','a') as f:
            traceback.print_exc(file=f) # 异常输出到指定文件
    else:
        print("结果为{:.2f}".format(c))
    finally:
        print('程序结束！')

def test_define_exception_class():
    class AgeError(Exception):  # 继承Exception类
        def __init__(self,errorInfo):
            Exception.__init__(self)
            self.errorInfo = errorInfo

        def __str__(self):
            return "年龄 {} 错误！应为1-140！".format(self.errorInfo)

    # 测试自定义异常类
    age = int(input('请输入年龄：'))
    if age<1 or age>150:
        raise AgeError(age)
    else:
        print('年龄正常：',age)

def test_enumerate():
    '''测试函数和推导式生成列表，操作每行增加行号'''
    # 普通方法
    a = ['我','爱','你']
    result = [i+'#{}'.format(a.index(i)) for i in a]
    print(result)

    # 使用enumerate
    result = [element+'#{}'.format(index) for index,element in enumerate(a)]
    print(result)

def test_pickle():
    '''测试序列化与反序列化'''
    import pickle
    # 序列化
    with open('test_pickle.data','wb') as f:
        a1 = '世纪'
        a2 = 18
        a3 = [1,3,4]
        pickle.dump(a1,f)
        pickle.dump(a2,f)
        pickle.dump(a3,f)
    # 反序列化
    with open('test_pickle.data', 'rb') as f:
        a1 = pickle.load(f)
        a2 = pickle.load(f)
        a3 = pickle.load(f)
        print(a1,a2,a3)


def test_csv():
    '''测试csv文件的读取与写入'''
    import csv
    # csv文件的写入
    a1 = ['ID','姓名','年龄']
    a2 = ['001','小七',17]
    a3 = ['002','小八',18]
    with open('test_csv.csv','w',newline='') as f:  # 加了一个newline参数
        writer = csv.writer(f)
        writer.writerows([a1,a2,a3])
        # writer.writerow(a2)
        # writer.writerow(a3)
    # 读取
    with open('test_csv.csv') as f:
        reader = csv.reader(f)
        for line in reader:
            print(line)

def test_shutil():
    '''测试shutil模块  文件和目录拷贝'''
    import shutil
    import zipfile
    shutil.copyfile('test_csv.csv','copy_test_csv.csv')   # 拷贝文件
    # 拷贝目录  参数：原目录路径，拷贝路径，忽略拷贝的文件
    shutil.copytree('源目录路径','目标路径',ignore=shutil.ignore_patterns('*.txt','*.html'))
    # 压缩和解压缩
    shutil.make_archive('压缩包放置位置','压缩的格式','要压缩的内容（路径）') # 压缩
    # 另一种压缩方式 使用zipfile模块
    z1 = zipfile.ZipFile('压缩文件名','w')
    z1.write('要压缩的路径')
    z1.close()
    # 解压缩  使用zipfile模块
    z2 = zipfile.ZipFile('要解压的压缩包位置','r')
    z2.extractall('解压的位置')
    z2.close()

def get_all_files(path):
    '''递归打印所有的目录和文件'''
    import os
    childFiles = os.listdir(path)
    for file in childFiles:
        filepath = os.path.join(path,file)
        if os.path.isdir(filepath):
            get_all_files(filepath)
        print(filepath)


if __name__ == '__main__':
    #test_copy_deepcopy()   # 测试拷贝
    #a = calculating_factorial(4)    # 计算4的阶乘
    #test_property()  # 测试装饰器的使用
    #test_except()   # 测试错误捕获
    #test_traceback()   # 测试traceback模块的使用
    #test_define_exception_class() # 测试自定义错误类
    #test_enumerate()   # 测试enumerate的使用
    #test_pickle()  # 测试序列化与反序列化
    #test_csv() # 测试csv文件读取与写入
    #test_shutil()   # 测试文件的压缩与解压缩
    get_all_files('../beginToLearn')