#coding=utf-8
from public.common import basepage
from public.pages.WorkBenchPage import WorkBench


class Login(basepage.Page):
    """登录页面"""

    def input_account(self, account):
        """输入账号"""
        self.dr.clear_type("css->[placeholder='请输入登录账号/邮箱/手机号码']", account)

    def input_pw(self, pw):
        """输入密码"""
        self.dr.clear_type("css->[placeholder='请输入密码']", pw)

    def click_login_btn(self):
        """点击登录按钮"""
        self.dr.click("class->el-button")

    def click_operation(self, platform):
        """选择平台"""
        self.dr.click("xpath->//div[contains(text(), '{}')]/../button/span".format(platform))

    def get_url(self):
        """获取url"""
        url = self.dr.get_url()
        return url

    def get_title(self):
        """获取登录框上的大标题"""
        text = self.dr.get_text("class->title")
        return text

    def login(self, account, pw, platform):
        """封装登录函数"""
        self.input_account(account)
        self.input_pw(pw)
        self.click_login_btn()
        self.click_operation(platform)

        return WorkBench(self.dr)

