# coding:utf-8

import os
import smtplib
import requests
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from loguru import logger
from config import globalparam
from config.basic_config import ConfigInit

# 测试报告的路径
reportPath = globalparam.report_path
# 163的用户名和密码
sendaddr_name = ConfigInit.sendaddr_name
sendaddr_pswd = ConfigInit.sendaddr_pswd
# 配置收发件人
recvaddress = ['281878321@qq.com']


class SendMail:
    def __init__(self, recver=None):
        """接收邮件的人：list or tuple"""
        if recver is None:
            self.sendTo = recvaddress
        else:
            self.sendTo = recver

    def __get_report(self):
        """获取最新测试报告"""
        dirs = os.listdir(reportPath)
        dirs.sort()
        dirs_html = []
        for filename in dirs:  # 找到文件夹中后缀为.html的最新的那个文件
            file, suffix = os.path.splitext(filename)
            if suffix == '.html':
                dirs_html.append(filename)
        newreportname = dirs_html[-1]
        print('The new report name: {0}'.format(newreportname))
        return newreportname

    def __take_messages(self):
        """生成邮件的内容，和html报告附件"""
        newreport = self.__get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = 'UI测试报告'
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(reportPath, newreport), 'rb') as f:
            mailbody = f.read()
        # self.msg['html'] = mailbody
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')
        self.msg.attach(html)

        # html附件
        att1 = MIMEText(mailbody, 'base64', 'gb2312')
        att1["Content-Type"] = 'multipart/form-data'
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        self.msg.attach(att1)

    # def send_simple_message(self):  # 使用mailgun  API发送
    #     """发送邮件"""
    #     self.__take_messages()
    #     newreport = self.__get_report()
    #     try:
    #         r = requests.post(
    #             "https://api.mailgun.net/v3/{}/messages".format(sendaddr_name),
    #             auth=("api", config.api_key),
    #             data={"from": "gucheng<mailgun@{}>".format(sendaddr_name),
    #                   "to": recvaddress,
    #                   "subject": self.msg['Subject'],
    #                   "html": self.msg['html'].decode()},
    #             files=[("attachment", ("test.html", open(os.path.join(reportPath, newreport), "rb").read()))]
    #         )
    #         logger.info("发送邮件成功")
    #     except Exception:
    #         logger.error('发送邮件失败')
    #         raise
    def send(self):  #使用smtp发送
        """发送邮件"""
        self.__take_messages()
        self.msg['from'] = 'postmaster@{}'.format(sendaddr_name)
        try:
            smtp = smtplib.SMTP('smtp.mailgun.org', 587)
            smtp.login('postmaster@{}'.format(sendaddr_name), sendaddr_pswd)
            smtp.sendmail(self.msg['from'], self.sendTo, self.msg.as_string())
            smtp.close()
            logger.info("发送邮件成功")
        except Exception:
            logger.error('发送邮件失败')
            raise


if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()
