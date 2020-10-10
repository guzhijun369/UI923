#coding=utf-8
from public.common import basepage
import time


class Customer(basepage.Page):
    """客户管理页面"""

    def click_add(self):
        self.dr.click("css->button.simple")

    def select_position(self, index, pcd):
        self.dr.click("css->div.my-area>div:nth-child({})>div.el-input.el-input--small".format(index))
        time.sleep(1)
        self.dr.click("xpath->//span[text()='{}']/..".format(pcd))

    def input_address(self, text):
        self.dr.clear_type('css->div.el-textarea>textarea', text)

    def input_company(self, company):
        self.dr.clear_type("css->input[placeholder^='长度1-20个字符']", company)

    def input_contact(self, contact):
        self.dr.clear_type("css->input[placeholder='请输入联系人名称']", contact)

    def input_phone(self, phone):
        self.dr.clear_type("css->input[placeholder='请输入客户手机号']", phone)

    def input_email(self, email):
        self.dr.clear_type("css->input[placeholder='请输入客户的邮箱地址']", email)

    def input_account(self, account):
        self.dr.clear_type("css->input[placeholder='登录账号']", account)

    def input_pw(self, pw):
        self.dr.clear_type("css->input[placeholder^='长度6-18个字符']", pw)

    def input_pw_two(self, pw):
        self.dr.clear_type("css->input[placeholder='请再次输入密码']", pw)

    def select_platform_type(self, placeholder, pt):
        self.dr.click("xpath->//input[@placeholder='{}']/..".format(placeholder))
        time.sleep(1)
        self.dr.click("xpath->//span[text()='{}']/..".format(pt))

    def click_determine(self):
        self.dr.click("xpath->//span[text()='确 定']/..")

    def get_customer_text(self):
        """获取第一个客户名称"""
        time.sleep(1.5)  # 等待弹窗消失，加载出最新数据
        text = self.dr.get_text('css->tbody>tr:nth-child(1)>td>div')
        return text




