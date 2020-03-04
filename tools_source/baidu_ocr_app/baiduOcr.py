from aip import AipOcr

class BaiduOcr():
    '''百度OCR文字识别'''
    def __init__(self):
        """初始化连接"""
        APP_ID = '11386043'
        API_KEY = 'GhRCZnOKIqs6x76osXqZxGM9'
        SECRET_KEY = 'OLEhkqKpjknGzYtPeu0g4I46FRdXBb2m'
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    def return_result(self,filePath):
        '''获取识别结果'''
        # 读取图片
        with open(filePath, 'rb') as fp:
            image_file = fp.read()
        # 调用通用文字识别, 图片参数为本地图片 获取原始结果
        content = self.client.basicGeneral(image_file)
        # 获取文字结果
        result = "\n".join([i['words'] for i in content['words_result']])
        return result

