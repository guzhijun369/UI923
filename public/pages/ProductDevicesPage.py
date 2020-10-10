# coding=utf-8
import time
from public.common import basepage


class ProductDevices(basepage.Page):
    """设备产品"""

    def click_add(self):
        """点击新建"""
        self.dr.click("xpath->//span[text()='{}']/../..".format('新增'))

    def js_code(self):
        self.dr.js('document.querySelector(".el-upload__input").style.display="block";')
        #document.querySelector("[accept='.ppt,.pptx']").style.display="block";

    def upload(self):
        path = r'C:\Users\谷志军\Desktop\健康圈图片\城市\152594278635798.png'
        self.dr.send_key_text("css->.el-upload__input", path)