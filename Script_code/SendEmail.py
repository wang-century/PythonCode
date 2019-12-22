import smtplib
from email.mime.text import MIMEText
from email.header import Header

class SEmail:
    def __init__(self):
        # QQ SMTP 服务
        mail_host = "smtp.qq.com"  # 设置服务器
        mail_user = "centuryw@vip.qq.com"  # 用户名
        mail_pass = "mswtkjtuuqadbcag"  # 口令
        self.sender = "centuryw@vip.qq.com"
        print('目前账户为:{}'.format(self.sender))
        self.smtpObj = smtplib.SMTP()
        self.smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        self.smtpObj.login(mail_user, mail_pass)

    def send_message(self):
        receivers = input('请输入收件邮箱:')  # '1649601714@qq.com'  # 接收邮件
        email_subject = input('请输入邮件标题:')
        email_content = input('请输入邮件内容:')
        message = MIMEText('{}'.format(email_content), 'plain', 'utf-8')
        message['From'] = Header("{}".format(self.sender), 'utf-8')   # 邮箱内容：发件人
        message['To'] = Header("{}".format(receivers), 'utf-8')    # 邮箱内容：收件人
        message['Subject'] = Header(email_subject, 'utf-8')
        try:
            self.smtpObj.sendmail(self.sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件:{}".format(e))

if __name__ == '__main__':
    email = SEmail()
    email.send_message()