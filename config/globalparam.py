#coding=utf-8

import os
import time

#项目路径
project_path = os.path.abspath('.')
if 'testcase' in project_path:
    project_path = os.path.join(project_path, "..")
if 'common' in project_path:
    project_path = os.path.join(project_path, "../..")
#调试路径
# project_path = r'D:\workhome\project\TS_uitest'
# 日志路径
log_path = os.path.join(project_path,'report', 'logs')
if not os.path.exists(log_path):  # 如果路径不存在，创建路径
    os.makedirs(log_path)
# 测试报告路径
report_path = os.path.join(project_path, 'report', 'html_report')
if not os.path.exists(report_path):  # 如果路径不存在，创建路径
    os.makedirs(report_path)
# 截图文件路径
img_path = os.path.join(report_path,'images')
if not os.path.exists(img_path):
    os.makedirs(img_path)
# 默认浏览器
browser = 'Chrome'
# 是否开启静默模式,只有在chrome下支持开启 True or False
headless = True
# 日志等级   INFO or DEBUG
log_level = 'INFO'
# 测试数据路径
data_path = os.path.join(project_path, 'data', 'testdata')

