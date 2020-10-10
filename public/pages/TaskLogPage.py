# coding=utf-8
import time
from public.common import basepage


class TaskLog(basepage.Page):
    """任务日志模块"""

    def click_start_date(self):
        """点击日期控件"""
        self.dr.click("css->input[placeholder='开始日期']")
        time.sleep(1)

    def select_left(self, position='left', num='1'):
        """选择左侧日期
        position：要定位的控件位置（左：left,右:right）
        num: 要点击的日期
        Args:
            select_left('right', '1')
        """
        dates = self.dr.get_elements(
            "xpath->//div[@class='el-picker-panel__content "
            "el-date-range-picker__content is-{}']/table/tbody/tr"
            "[@class='el-date-table__row']/td[contains(@class, 'available')]".format(
                position))
        for i in dates:
            number = i.find_element_by_css_selector('div>span')
            if number.text == num:
                i.click()
                break
