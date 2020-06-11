
"""
    为入户调查所拍照片进行分类保存
以编号为目录名进行保存
"""
from os import mkdir,listdir
from re import findall
from shutil import move

def classify_directory(file_path):
    # 所需分类目录
    file_name_list = listdir(file_path)     # 列出该目录所有文件名

    # 循环取出所有文件并分类保存
    for file_name in file_name_list:
        directory_name = findall('(.*?)栋.*?', file_name)[0]
        try:
            move(file_path + '\\' + file_name, file_path + '\\' + directory_name + '\\' + file_name)
        except Exception as e:
            mkdir(file_path+'\\'+directory_name)
            move(file_path + '\\' + file_name, file_path + '\\' + directory_name + '\\' + file_name)
            print(e)

    print('分类完成！')