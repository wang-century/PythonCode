from aip import AipOcr
from os import listdir

class BaiduOcr:
    def __init__(self):
        """ 你的 APPID AK SK """
        APP_ID = '19994782'
        API_KEY = 'zzcYTBFGlP4kvW3FRTVgt1My'
        SECRET_KEY = 'duGa0iAnRtpjM1Gy4TWcpg2nsD5g0AkD'
        # 初始化client
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    def get_file_content(self,filePath):
        """ 读取图片 """
        with open(filePath, 'rb') as fp:
            return fp.read()

    def recognition_img(self,filePath):
        """ 识别身份证 """
        image = self.get_file_content(filePath)
        idCardSide = "front"
        """ 如果有可选参数 """
        options = {}
        options["detect_direction"] = "true"
        options["detect_risk"] = "true"
        # 调用身份证识别
        result = self.client.idcard(image, idCardSide, options)
        result = result['words_result']
        people = {}

        people['name'] = result['姓名']['words']
        people['id'] = result['公民身份号码']['words']
        people['birthday'] = result['出生']['words']
        people['sex'] = result['性别']['words']
        people['nation'] = result['民族']['words']
        people['address'] = result['住址']['words']
        return people


if __name__ == '__main__':
    ocr = BaiduOcr()
    # ocr.recognition_img('test.jpg')   # 识别单个
    ocr.recognition_directory_imgs('../tools')  # 识别目录内