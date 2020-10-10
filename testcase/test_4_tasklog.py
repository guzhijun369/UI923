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
class TestTask(mytest.MyTest):
    """任务日志模块"""

    @screenshot_about_case
    def test_select_date(self):
        workbench = Login(self.dr).login('281878321@qq.com', 'q5310543', '业务平台')
        workbench.exist_loading()
        workbench.click_menu('日志')
        workbench.click_menu_child('任务日志')
        tasklog = workbench.return_task_log_page()
        tasklog.click_start_date()
        tasklog.select_left('left', '1')
        tasklog.select_left('right','1')
        time.sleep(15)