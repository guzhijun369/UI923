#coding=utf-8
import time
import unittest

from public.common import mytest
from public.pages import LoginPage
from ddt import ddt,data,unpack
from loguru import logger
from public.common.datainfo import get_test_case_data, data_info
from public.pages.LoginPage import Login
from public.common.get_img import screenshot_about_case


@ddt
class TestTask(mytest.MyAutologinTest):
    """任务日志模块"""

    @screenshot_about_case
    def test_uploadimg(self):
        self.workbench.exist_loading()
        self.workbench.click_menu('设备中心')
        self.workbench.click_menu_child('设备产品')
        time.sleep(1)
        product = self.workbench.renturn_product_page()
        product.click_add()
        time.sleep(1)
        product.js_code()
        product.upload()
        time.sleep(10)
        self.assertIn('2222', '21222')
        # tasklog = workbench.return_task_log_page()
        # tasklog.click_start_date()
        # tasklog.select_left('left', '1')
        # tasklog.select_left('right','1')
        # time.sleep(15)