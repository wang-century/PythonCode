"""
数学思维修炼
"""

def convert_decimalism_to_binary(number):
    """ 十进制转二进制
    除二取余，逆序排列
    """
    result = []     # 用于保存余数
    original_number = number   # 保存原数（用于结尾输出）
    while True:
        # 除二取余
        number_resu = divmod(number,2)
        print('{}除以2商{}余{}'.format(number,number_resu[0],number_resu[1]))
        number = number_resu[0]
        result.append(number_resu[1])
        if number == 0:
            break
    # 逆序排列
    result.reverse()
    result = ''.join([str(i) for i in result])
    print('{}的二进制为:{}'.format(original_number,result))
    return int(result)

def convert_binary_to_decimalism(number):
    """ 二进制转十进制
    按权展开
    """
    content = [int(i) for i in str(number)]   # 将二进制数转为列表
    count_number = len(content)-1     # 求长度，用于最终计算的次方数
    # 计算结果
    result = 0  # 用于保存结果
    # 按权展开求结果
    for i in content:
        # 数为1计算，为0则跳过，但次方需减一
        if i == 1:
            result += 2 ** count_number
        count_number -= 1   # 每次循环次方减一
    print('二进制{}的十进制结果为{}'.format(number,result))
    return result

def judge_prime_number_method_1(number):
    """判断素数（试除法）
    函数说明：传入一个数，判断是否为素数，是则返回True，否则返回False。
    素数：又称质数，是指在一个大于1的自然数中，除了1和它本身外，无法被其它自然数整除的数。（比一大但不是素数的数被称为合数，1和0既非素数也非合数）
    """
    # 判断是否为整数，是否大于1
    if type(number) == type(int()) and number > 1:
        # 从2开始(包括2)循环到该数(不包括该数)，若该数能被整除且被整除的数不是它本身则不是素数，否则为素数
        for i in range(2,number):
            if number % i == 0:
                return False
        return True
    # 如果不是整数或者小于等于1则不是素数
    else:
        return False

def judge_prime_number_method_2(number):
    """判断素数（判断平方法减少计算次数）
    函数说明：传入一个数，判断是否为素数，是则返回True，否则返回False。
    素数：又称质数，是指在一个大于1的自然数中，除了1和它本身外，无法被其它自然数整除的数。（比一大但不是素数的数被称为合数，1和0既非素数也非合数）
    说明：判断number是否为素数，不需要一直除到number-1才能确认，只需要除到“ 根号n ”就可以了。
    """
    # 判断是否为整数，是否大于1
    if type(number) == type(int()) and number > 1:
        # 从2开始(包括2)循环，若i的平方大于number则停止循环；若该数能被整除则不是素数，否则为素数
        for i in range(2, number):
            if i*i > number:
                break
            if number % i == 0:
                return False
        return True
    # 如果不是整数或者小于等于1则不是素数
    else:
        return False

def judge_prime_number_method_3(number):
    """判断素数
    Eratosthenes算法：假设有一个筛子，用来存放2-100之间的所有数，由于偶数都能被2整除，所以偶数不是素数（2除外），接着再将3的倍数筛除，
    再将5的倍数筛除，再将7的倍数筛除，即可得到100以内的所有素数
    注：此处未使用该算法
    """
    # 判断是否为整数，是否大于1
    if type(number) == type(int()) and number > 1:
        # 筛除
        if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
            return True
        return False
    # 如果不是整数或者小于等于1则不是素数
    else:
        return False




if __name__ == '__main__':
    # 判断是否为素数
    for number in range(1000):
        if judge_prime_number_method_3(number):
            print(number)

    # 十进制转二进制
    # convert_decimalism_to_binary(8)

    # 二进制转十进制
    # convert_binary_to_decimalism(1001)