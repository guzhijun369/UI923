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
class TestCustomer(mytest.MyTest):
    """客户管理模块"""

    @screenshot_about_case
    def test_addcustomer(self):
        """新增客户"""
        workbench = Login(self.dr).login('281878321@qq.com', 'q5310543', '业务平台')
        workbench.exist_loading()
        workbench.click_menu('客户管理')
        customer = workbench.return_customer()
        customer.click_add()
        customer.input_company('中国电信')
        customer.input_contact('谷志军')
        customer.input_phone('13800138011')
        customer.input_email('2525775@qq.com')
        customer.input_account('ui927')
        customer.input_pw('q5310543')
        customer.input_pw_two('q5310543')
        customer.select_platform_type('所属平台', '云车智行')
        customer.select_platform_type('所属类型', '代理商')
        customer.select_position(1, '广东省')
        customer.select_position(2, '深圳')
        customer.select_position(3, '宝安区')
        customer.input_address('这是详细地址')
        customer.click_determine()
        company = customer.get_customer_text()
        self.assertEqual('中国1电信', company)
