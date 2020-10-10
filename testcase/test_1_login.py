#coding=utf-8
import time
import unittest

from public.common import mytest
from public.pages import LoginPage
from ddt import ddt,data,unpack
from loguru import logger
from public.common.datainfo import get_test_case_data, data_info
from public.common.get_img import screenshot_about_case

file = 'login'

@ddt
class TestLogin(mytest.MyTest):
    """登录模块"""

    @screenshot_about_case
    @data(*get_test_case_data(data_info, file, 'test_01_login'))
    def test_01_login(self, data):
        login = LoginPage.Login(self.dr)
        test_data = data['data']
        test_assert = data['assertion']
        ele = login.login(test_data['username'], test_data['pw'], test_data['platform'])
        login.exist_loading()
        username = ele.get_name()
        url = ele.get_url()
        self.assertIn(url,test_assert['title'])
        self.assertIn(test_assert['username'], username)
        self.assertIn('2222', '21222')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestLogin('test_01_login'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # @screenshot_about_case
    # def test_baidu(self):
    #     """百度搜索"""
    #     m = LoginPage.Login(self.dr)
    #     m.input_v()
    #     m.click_btn()
    #     m.click_one()
    #     m.into_newwin()
    #     url = m.get_url()
    #     self.assertIn('http://sz.test.zelinedu.net', url)

