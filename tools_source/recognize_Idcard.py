"""
    识别身份证并保存到excel
"""
from os import listdir
from baiduOcr import BaiduOcr

# 创建百度ocr client并识别目录
ocr = BaiduOcr()

# 尝试打开保存身份证信息的文件，如果文件存在则追加，如果不存在则创建文件并添加列名
try:
    with open('idcard_info.csv','r'):
        pass
    save_file = open('idcard_info.csv', 'a+')
except Exception as e:
    # 创建文件
    save_file = open('idcard_info.csv','a+')     # 打开csv文件
    # 添加列名
    save_file.write(','.join(['姓名','公民身份号码','出生','性别','民族','住址'])+'\n')


def recognition_directory_imgs(filePath):
    """ 识别某个目录的所有图片 """
    # 列出目录内所有文件
    directory_imgs = listdir(filePath)
    # 如果文件为图片则进行识别操作
    for img in directory_imgs:
        if img.endswith('.jpg'):
            filePath = filePath + '/' + img
            people = ocr.recognition_img(filePath)
            save_file.write(','.join([people['name'],people['id']+'\t',people['birthday'],people['sex'],people['nation'],people['address']])+'\n')

recognition_directory_imgs('../tools')    # 在此输入文件名进行识别操作

save_file.close()   # 关闭csv文件