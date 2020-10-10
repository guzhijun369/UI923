#coding=utf-8
import unittest
import HTMLTestRunner_gu
import time
import os
from loguru import logger
from config import globalparam
from public.common import sendmail
from public.common.mongo_utils import MongoModel
from public.common.send_report import SslSendReport


path = os.path.join(globalparam.log_path,'test_{}.log'.format(time.strftime('%Y-%m-%d')))

logger.add(path, level=globalparam.log_level)  # 日志初始化

def run(method, test=None):
    if method == 'all':
        test_dir = './testcase'
        suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test_1*.py')
        start_time = int(time.time())
        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        reportname = os.path.join(globalparam.report_path, 'TestResult' + now + '.html')
        with open(reportname, 'wb') as f:
            runner = HTMLTestRunner_gu.HTMLTestRunner(
                stream=f,
                title='测试报告',
                description=''
            )
            runner.run(suite)
        time.sleep(3)
        # 发送邮件
        # mail = sendmail.SendMail()
        # mail.send()
        if os.environ.get('RUN_MODE') == 'testpro':
            send_report = SslSendReport()
            send_report.main_pro(start_time)
    if method == 'one':
        suit = unittest.TestSuite()
        suit.addTest(test)  # 把这个类中需要执行的测试用例加进去，有多条再加即可
        runner = unittest.TextTestRunner()
        runner.run(suit)


if __name__ == '__main__':
    # run('one', test_workbench.TestWorkbench("test_luandian"))
    run('all')

# def add_cases():
#     '''加载所有的测试用例'''
#     test_dir = './testcase'
#     discover = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')
#     return discover

# @threads(3)
# def run(test_suit):
#     result = BeautifulReport(test_suit)
#     now = time.strftime('%Y-%m-%d_%H_%M_%S')
#     reportname = 'TestResult' + now + '.html'
#     result.report(filename=reportname, description='测试报告',
#                   log_path='./report/html_report')

# if __name__ == '__main__':
#     cases = add_cases()
#     for case in cases:
#         run(case)
